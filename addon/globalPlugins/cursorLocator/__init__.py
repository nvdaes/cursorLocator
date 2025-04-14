# -*- coding: UTF-8 -*-

# cursorLocator: Global plugin to know the cursor position when typing on multiline edit controls
# Copyright (C) 2017-2022 Noelia Ruiz Martínez
# Released under GPL 2

import wx

import addonHandler
import globalPluginHandler
import controlTypes
import textInfos
from browseMode import BrowseModeDocumentTreeInterceptor
import api
import ui
import tones
import config
import gui
from gui import guiHelper, nvdaControls
from gui.settingsDialogs import NVDASettingsDialog, SettingsPanel
from scriptHandler import script
from globalCommands import SCRCAT_SYSTEMCARET, SCRCAT_CONFIG

from . import utils

addonHandler.initTranslation()

# Constants
ADDON_SUMMARY = addonHandler.getCodeAddon().manifest["summary"]
ADDON_PANEL_TITLE = ADDON_SUMMARY

confspec = {
	"reportLineLength": "integer(default=80)",
	"maxStartNotificationNumber": "integer(default=0)",
	"maxEndNotificationNumber": "integer(default=0)",
	"startLinePitch": "integer(default=400)",
	"startLineLength": "integer(default=50)",
	"endLinePitch": "integer(default=1000)",
	"endLineLength": "integer(default=50)",
}


class AddonSettingsPanel(SettingsPanel):

	title = ADDON_PANEL_TITLE

	# Translators: Description of the Cursor Locator panel.
	panelDescription = _("Configure {}").format(ADDON_SUMMARY)

	def makeSettings(self, settingsSizer):
		sHelper = guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		sHelper.addItem(wx.StaticText(self, label=self.panelDescription))

		# Translators: Label for a group of Cursor Locator options.
		lineGroupText = _("Line properties")
		lineGroup = guiHelper.BoxSizerHelper(
			self, sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=lineGroupText), wx.VERTICAL)
		)
		sHelper.addItem(lineGroup)

		self.LengthEdit = lineGroup.addLabeledControl(
			# Translators: Label for the Cursor Locator panel.
			_("Report &line length:"), nvdaControls.SelectOnFocusSpinCtrl,
			min=0, max=600, initial=config.conf["cursorLocator"]["reportLineLength"]
		)

		self.maxRepeatStartEdit = lineGroup.addLabeledControl(
			# Translators: Label for the Cursor Locator panel.
			_("Ma&ximum number of beeps for start of line notification:"), nvdaControls.SelectOnFocusSpinCtrl,
			min=0, max=600, initial=config.conf["cursorLocator"]["maxStartNotificationNumber"]
		)

		self.maxRepeatEndEdit = lineGroup.addLabeledControl(
			# Translators: Label for the Cursor Locator panel.
			_("Max&imum number of beeps for end of line notification:"), nvdaControls.SelectOnFocusSpinCtrl,
			min=0, max=600, initial=config.conf["cursorLocator"]["maxEndNotificationNumber"]
		)

		# Translators: Label for a group of Cursor Locator options.
		startGroupText = _("Sound for start of line")
		startGroup = guiHelper.BoxSizerHelper(
			self, sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=startGroupText), wx.VERTICAL)
		)
		sHelper.addItem(startGroup)

		self.startHzEdit = startGroup.addLabeledControl(
			# Translators: Label for the Cursor Locator panel.
			_("&Pitch of sound for start of line:"), nvdaControls.SelectOnFocusSpinCtrl,
			min=20, max=20000, initial=config.conf["cursorLocator"]["startLinePitch"]
		)

		self.startLengthEdit = startGroup.addLabeledControl(
			# Translators: Label for the Cursor Locator panel.
			_("L&ength of sound for start of line:"), nvdaControls.SelectOnFocusSpinCtrl,
			min=20, max=2000, initial=config.conf["cursorLocator"]["startLineLength"]
		)

		# Translators: Label for the Cursor Locator panel.
		label = _("&Test sound for start of line")
		self.testStartSoundButton = startGroup.addItem(wx.Button(self, label=label))
		self.testStartSoundButton.Bind(wx.EVT_BUTTON, self.onTestStartSound)

		# Translators: Label for a group of Cursor Locator options.
		endGroupText = _("Sound for end of line")
		endGroup = guiHelper.BoxSizerHelper(
			self, sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=endGroupText), wx.VERTICAL)
		)
		sHelper.addItem(endGroup)

		self.endHzEdit = endGroup.addLabeledControl(
			# Translators: Label for the Cursor Locator panel.
			_("P&itch of sound for end of line:"), nvdaControls.SelectOnFocusSpinCtrl,
			min=20, max=20000, initial=config.conf["cursorLocator"]["endLinePitch"]
		)

		self.endLengthEdit = endGroup.addLabeledControl(
			# Translators: Label for the Cursor Locator panel.
			_("Le&ngth of sound for end of line:"), nvdaControls.SelectOnFocusSpinCtrl,
			min=20, max=2000, initial=config.conf["cursorLocator"]["endLineLength"]
		)

		# Translators: Label for the Cursor Locator panel.
		label = _("Test s&ound for end of line")
		self.testEndSoundButton = endGroup.addItem(wx.Button(self, label=label))
		self.testEndSoundButton.Bind(wx.EVT_BUTTON, self.onTestEndSound)

	def onTestStartSound(self, evt):
		tones.beep(self.startHzEdit.GetValue(), self.startLengthEdit.GetValue())

	def onTestEndSound(self, evt):
		tones.beep(self.endHzEdit.GetValue(), self.endLengthEdit.GetValue())

	def onSave(self):
		config.conf["cursorLocator"]["reportLineLength"] = self.LengthEdit.GetValue()
		config.conf["cursorLocator"]["maxStartNotificationNumber"] = self.maxRepeatStartEdit.GetValue()
		config.conf["cursorLocator"]["maxEndNotificationNumber"] = self.maxRepeatEndEdit.GetValue()
		config.conf["cursorLocator"]["startLinePitch"] = self.startHzEdit.GetValue()
		config.conf["cursorLocator"]["startLineLength"] = self.startLengthEdit.GetValue()
		config.conf["cursorLocator"]["endLinePitch"] = self.endHzEdit.GetValue()
		config.conf["cursorLocator"]["endLineLength"] = self.endLengthEdit.GetValue()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = SCRCAT_SYSTEMCARET

	def __init__(self):
		super().__init__()
		config.conf.spec["cursorLocator"] = confspec
		NVDASettingsDialog.categoryClasses.append(AddonSettingsPanel)

	def terminate(self):
		NVDASettingsDialog.categoryClasses.remove(AddonSettingsPanel)

	def onSettings(self, evt):
		gui.mainFrame.popupSettingsDialog(NVDASettingsDialog, AddonSettingsPanel)

	@script(
		# Translators: Message presented in input mode.
		description=_("Shows the {} settings.").format(ADDON_SUMMARY),
		category=SCRCAT_CONFIG
	)
	def script_settings(self, gesture):
		wx.CallAfter(self.onSettings, None)

	def removeCarriageReturn(self, text):
		try:
			if ord(text[-1]) == 13 or ord(text[-1]) == 10:
				text = text[:-1]
			if ord(text[-1]) == 13 or ord(text[-1]) == 10:
				text = text[:-1]
		except IndexError:
			pass
		return text

	def event_typedCharacter(self, obj, nextHandler, ch):
		nextHandler()
		states = obj.states
		if controlTypes.State.MULTILINE not in states and obj.role != controlTypes.Role.DOCUMENT:
			return
		if not ord(ch) >= 32:
			return
		try:
			info = obj.makeTextInfo(textInfos.POSITION_CARET)
			info.expand(textInfos.UNIT_LINE)
			text = self.removeCarriageReturn(info.text)
			if utils.shouldReportStartOfLine(text):
				startPitch = config.conf["cursorLocator"]["startLinePitch"]
				startLength = config.conf["cursorLocator"]["startLineLength"]
				tones.beep(startPitch, startLength)
			if utils.shouldReportEndOfLine(text):
				endPitch = config.conf["cursorLocator"]["endLinePitch"]
				endLength = config.conf["cursorLocator"]["endLineLength"]
				tones.beep(endPitch, endLength)
		except Exception as e:
			raise e

	@script(
		# Translators: Message presented in input help mode.
		description=_("Reports the length of the current line."),
		speakOnDemand=True,
		gesture="kb:NVDA+control+shift+l"
	)
	def script_reportLineLength(self, gesture):
		obj = api.getFocusObject()
		ti = obj.treeInterceptor
		if isinstance(ti, BrowseModeDocumentTreeInterceptor) and not ti.passThrough:
			obj = ti
		try:
			info = obj.makeTextInfo(textInfos.POSITION_CARET)
			info.expand(textInfos.UNIT_LINE)
			lineLen = len(self.removeCarriageReturn(info.text))
			# Translators: message to report line length.
			ui.message(_("Linelength: %d") % lineLen)
		except Exception:
			pass
