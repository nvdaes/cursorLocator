# -*- coding: UTF-8 -*-

# cursorLocator: Global plugin to know the cursor position when typing on multiline edit controls
# Copyright (C) 2017-2021 Noelia Ruiz Martínez
# Released under GPL 2

import addonHandler
import globalPluginHandler
import controlTypes
import textInfos
import treeInterceptorHandler
import api
import ui
import tones
import config
import wx
import gui
from gui import SettingsPanel, NVDASettingsDialog, guiHelper, nvdaControls
from scriptHandler import script
from globalCommands import SCRCAT_SYSTEMCARET, SCRCAT_CONFIG

addonHandler.initTranslation()

# Constants
ADDON_SUMMARY = addonHandler.getCodeAddon().manifest["summary"]
ADDON_PANEL_TITLE = ADDON_SUMMARY

confspec = {
	"reportStartOfLine": "boolean(default=True)",
	"reportLineLength": "integer(default=80)",
	"startLinePitch": "integer(default=400)",
	"startLineLength": "integer(default=50)",
	"endLinePitch": "integer(default=1000)",
	"endLineLength": "integer(default=50)",
}
config.conf.spec["cursorLocator"] = confspec


class AddonSettingsPanel(SettingsPanel):

	title = ADDON_PANEL_TITLE

	# Translators: Description of the Cursor Locator panel.
	description = _("Configure {}").format(ADDON_SUMMARY)

	def makeSettings(self, settingsSizer):
		sHelper = guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		sHelper.addItem(wx.StaticText(self, label=self.panelDescription))

		# Translators: Label for a group of Cursor Locator options.
		lineGroupText = _("Line properties")
		lineGroup = guiHelper.BoxSizerHelper(
			self, sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=lineGroupText), wx.VERTICAL)
		)
		sHelper.addItem(lineGroup)

		# Translators: Label for the Cursor Locator panel.
		self.reportStartCheckBox = lineGroup.addItem(wx.CheckBox(self, label=_("&Report start of line")))
		self.reportStartCheckBox.SetValue(config.conf["cursorLocator"]["reportStartOfLine"])

		# Translators: Label for the Cursor Locator panel.
		self.LengthEdit = lineGroup.addLabeledControl(
			_("Report &line length:"), nvdaControls.SelectOnFocusSpinCtrl,
			min=0, max=600, initial=config.conf["cursorLocator"]["reportLineLength"]
		)

		# Translators: Label for a group of Cursor Locator options.
		startGroupText = _("Sound for start of line")
		startGroup = guiHelper.BoxSizerHelper(
			self, sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=startGroupText), wx.VERTICAL)
		)
		sHelper.addItem(startGroup)

		# Translators: Label for the Cursor Locator panel.
		self.startHzEdit = startGroup.addLabeledControl(
			_("Pitch of sound for start of line:"),
			nvdaControls.SelectOnFocusSpinCtrl,
			min=20, max=20000, initial=config.conf["cursorLocator"]["startLinePitch"]
		)

		# Translators: Label for the Cursor Locator panel.
		self.startLengthEdit = startGroup.addLabeledControl(
			_("Length of sound for start of line:"), nvdaControls.SelectOnFocusSpinCtrl,
			min=20, max=5000, initial=config.conf["cursorLocator"]["startLineLength"]
		)

		# Translators: Label for the Cursor Locator panel.
		label = _("Test sound for start of line")
		self.testStartSoundButton = startGroup.addItem(wx.Button(self, label=label))
		self.testStartSoundButton.Bind(wx.EVT_BUTTON, self.onTestStartSound)

		# Translators: Label for a group of Cursor Locator options.
		endGroupText = _("Sound for end of line")
		endGroup = guiHelper.BoxSizerHelper(
			self, sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=endGroupText), wx.VERTICAL)
		)
		sHelper.addItem(endGroup)

		# Translators: Label for the Cursor Locator panel.
		self.endHzEdit = endGroup.addLabeledControl(
			_("Pitch of sound for end of line:"),
			nvdaControls.SelectOnFocusSpinCtrl,
			min=20, max=20000, initial=config.conf["cursorLocator"]["endLinePitch"]
		)

		# Translators: Label for the Cursor Locator panel.
		self.endLengthEdit = endGroup.addLabeledControl(
			_("Length of sound for end of line:"), nvdaControls.SelectOnFocusSpinCtrl,
			min=20, max=5000, initial=config.conf["cursorLocator"]["endLineLength"]
		)

		# Translators: Label for the Cursor Locator panel.
		label = _("Test sound for end of line")
		self.testEndSoundButton = endGroup.addItem(wx.Button(self, label=label))
		self.testEndSoundButton.Bind(wx.EVT_BUTTON, self.onTestEndSound)

	def postInit(self):
		self.reportStartCheckBox.SetFocus()

	def onTestStartSound(self, evt):
		tones.beep(self.startHzEdit.GetValue(), self.startLengthEdit.GetValue())

	def onTestEndSound(self, evt):
		tones.beep(self.endHzEdit.GetValue(), self.endLengthEdit.GetValue())

	def onSave(self):
		config.conf["cursorLocator"]["reportStartOfLine"] = self.reportStartCheckBox.GetValue()
		config.conf["cursorLocator"]["reportLineLength"] = self.LengthEdit.GetValue()
		config.conf["cursorLocator"]["startLinePitch"] = self.startHzEdit.GetValue()
		config.conf["cursorLocator"]["startLineLength"] = self.startLengthEdit.GetValue()
		config.conf["cursorLocator"]["endLinePitch"] = self.endHzEdit.GetValue()
		config.conf["cursorLocator"]["endLineLength"] = self.endLengthEdit.GetValue()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = SCRCAT_SYSTEMCARET

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		NVDASettingsDialog.categoryClasses.append(AddonSettingsPanel)

	def terminate(self):
		NVDASettingsDialog.categoryClasses.remove(AddonSettingsPanel)

	def onSettings(self, evt):
		gui.mainFrame._popupSettingsDialog(NVDASettingsDialog, AddonSettingsPanel)

	@script(
		# Translators: Message presented in input mode.
		description=_("Shows the {} settings.").format(ADDON_SUMMARY),
		category=SCRCAT_CONFIG
	)
	def script_settings(self, gesture):
		wx.CallAfter(self.onSettings, None)

	def removeCarriageReturn(self, text):
		try:
			if ord(text[-1]) == 13:
				text = text[:-1]
		except IndexError:
			pass
		return text

	def event_typedCharacter(self, obj, nextHandler, ch):
		nextHandler()
		states = obj.states
		if not controlTypes.STATE_MULTILINE in states or controlTypes.STATE_READONLY in states:
			return
		if not ord(ch) >= 32:
			return
		reportStart = config.conf["cursorLocator"]["reportStartOfLine"]
		reportLineLength = config.conf["cursorLocator"]["reportLineLength"]
		startPitch = config.conf["cursorLocator"]["startLinePitch"]
		startLength = config.conf["cursorLocator"]["startLineLength"]
		endPitch = config.conf["cursorLocator"]["endLinePitch"]
		endLength = config.conf["cursorLocator"]["endLineLength"]
		if not reportStart and reportLineLength == 0:
			return
		try:
			info=obj.makeTextInfo(textInfos.POSITION_CARET)
			info.expand(textInfos.UNIT_LINE)
			text = self.removeCarriageReturn(info.text)
			if reportStart and len(text) == 1:
				tones.beep(startPitch, startLength)
			if reportLineLength > 0 and len(text) == reportLineLength:
				tones.beep(endPitch, endLength)
		except Exception as e:
			raise e

	@script(
		# Translators: Message presented in input help mode.
		description=_("Reports the length of the current line."),
		gesture="kb:NVDA+control+shift+l"
	)
	def script_reportLineLength(self, gesture):
		obj = api.getFocusObject()
		ti = obj.treeInterceptor
		if isinstance(ti, treeInterceptorHandler.DocumentTreeInterceptor) and not ti.passThrough:
			obj = ti
		try:
			info = obj.makeTextInfo(textInfos.POSITION_CARET)
			info.expand(textInfos.UNIT_LINE)
			lineLen = len(self.removeCarriageReturn(info.text))
			ui.message("Line length: %d" % lineLen)
		except Exception:
			pass
