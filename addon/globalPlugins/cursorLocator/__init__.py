# -*- coding: UTF-8 -*-
#cursorLocator: Global plugin to know the cursor position when typing on multiline edit controls
 #Copyright (C) 2016 Noelia Ruiz Martínez, Alberto Buffolino
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
from gui import guiHelper, nvdaControls
from gui.settingsDialogs import SettingsDialog
from NVDAObjects.window.edit import Edit
from globalCommands import SCRCAT_SYSTEMCARET, SCRCAT_CONFIG

addonHandler.initTranslation()

confspec = {
	"reportStartOfLine": "boolean(default=True)",
	"reportLineLength": "integer(default=80)",
}
config.conf.spec["cursorLocator"] = confspec

class AddonSettingsDialog(SettingsDialog):

	# Translators: title of a dialog.
	title = _("Cursor Locator settings")

	def makeSettings(self, settingsSizer):
		sHelper = guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Translators: label of a dialog.
		self.reportStartCheckBox = sHelper.addItem(wx.CheckBox(self, label=_("&Report start of line")))
		self.reportStartCheckBox.SetValue(config.conf["cursorLocator"]["reportStartOfLine"])

				# Translators: Label of a dialog.
		self.LengthEdit = sHelper.addLabeledControl(_("Report &line length:"), nvdaControls.SelectOnFocusSpinCtrl,
			min=0, max=600, initial=config.conf["cursorLocator"]["reportLineLength"])

	def postInit(self):
		self.reportStartCheckBox.SetFocus()

	def onOk(self,evt):
		config.conf["cursorLocator"]["reportStartOfLine"] = self.reportStartCheckBox.GetValue()
		config.conf["cursorLocator"]["reportLineLength"] = self.LengthEdit.GetValue()
		super(AddonSettingsDialog, self).onOk(evt)

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = SCRCAT_SYSTEMCARET

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		self.prefsMenu = gui.mainFrame.sysTrayIcon.preferencesMenu
		self.settingsItem = self.prefsMenu.Append(wx.ID_ANY,
			# Translators: name of a menu item.
			_("C&ursor locator settings..."))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onSettings, self.settingsItem)

	def terminate(self):
		try:
			self.prefsMenu.RemoveItem(self.settingsItem)
		except wx.PyDeadObjectError:
			pass

	def onSettings(self, evt):
		gui.mainFrame._popupSettingsDialog(AddonSettingsDialog)

	def script_settings(self, gesture):
		wx.CallAfter(self.onSettings, None)
	script_settings.category = SCRCAT_CONFIG
	# Translators: message presented in input mode.
	script_settings.__doc__ = _("Shows the Cursor Locator settings dialog.")

	def event_typedCharacter(self, obj, nextHandler, ch):
		nextHandler()
		states = obj.states
		if not controlTypes.STATE_MULTILINE in states or controlTypes.STATE_READONLY in states:
			return
		if not ord(ch)>=32:
			return
		reportStart = config.conf["cursorLocator"]["reportStartOfLine"]
		reportLineLength = config.conf["cursorLocator"]["reportLineLength"]
		if not reportStart and not reportLineLength:
			return
		try:
			info=obj.makeTextInfo(textInfos.POSITION_CARET)
			info.expand(textInfos.UNIT_LINE)
			if reportStart and len(info.text) == 1:
				tones.beep(400, 50)
			if reportLineLength and len(info.text) == reportLineLength:
				tones.beep(1000, 50)
		except (NotImplementedError, RuntimeError):
			pass

	def script_reportLineLength(self, gesture):
		obj=api.getFocusObject()
		treeInterceptor=obj.treeInterceptor
		if isinstance(treeInterceptor,treeInterceptorHandler.DocumentTreeInterceptor) and not treeInterceptor.passThrough:
			obj=treeInterceptor
		try:
			info=obj.makeTextInfo(textInfos.POSITION_CARET)
			info.expand(textInfos.UNIT_LINE)
			l = len(info.text)
			ui.message("Line length: %d" % l)
		except (NotImplementedError, RuntimeError):
			pass
	# Translators: Message presented in input help mode.
	script_reportLineLength.__doc__ = _("Reports the length of the current line.")
