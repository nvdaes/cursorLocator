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
}
config.conf.spec["cursorLocator"] = confspec


class AddonSettingsPanel(SettingsPanel):

	title = ADDON_PANEL_TITLE

	def makeSettings(self, settingsSizer):
		sHelper = guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Translators: Label of a dialog.
		self.reportStartCheckBox = sHelper.addItem(wx.CheckBox(self, label=_("&Report start of line")))
		self.reportStartCheckBox.SetValue(config.conf["cursorLocator"]["reportStartOfLine"])

		# Translators: Label of a dialog.
		self.LengthEdit = sHelper.addLabeledControl(_("Report &line length:"), nvdaControls.SelectOnFocusSpinCtrl,
			min=0, max=600, initial=config.conf["cursorLocator"]["reportLineLength"])

	def postInit(self):
		self.reportStartCheckBox.SetFocus()

	def onSave(self):
		config.conf["cursorLocator"]["reportStartOfLine"] = self.reportStartCheckBox.GetValue()
		config.conf["cursorLocator"]["reportLineLength"] = self.LengthEdit.GetValue()

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
		if not reportStart and not reportLineLength:
			return
		try:
			info=obj.makeTextInfo(textInfos.POSITION_CARET)
			info.expand(textInfos.UNIT_LINE)
			text = self.removeCarriageReturn(info.text)
			if reportStart and len(text) == 1:
				tones.beep(400, 50)
			if reportLineLength and len(text) == reportLineLength:
				tones.beep(1000, 50)
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
