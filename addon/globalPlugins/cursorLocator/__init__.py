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
from NVDAObjects.window.edit import Edit
from globalCommands import SCRCAT_SYSTEMCARET

addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = SCRCAT_SYSTEMCARET

	def event_typedCharacter(self, obj, nextHandler, ch):
		nextHandler()
		states = obj.states
		if not controlTypes.STATE_MULTILINE in states or controlTypes.STATE_READONLY in states:
			return
		if not ord(ch)>=32:
			return
		try:
			info=obj.makeTextInfo(textInfos.POSITION_CARET)
			info.expand(textInfos.UNIT_LINE)
			if len(info.text) == 1:
				tones.beep(400, 50)
			elif len(info.text) == 80:
				tones.beep(1000, 50)
		except (NotImplementedError, RuntimeError):
			pass

	def script_reportLenToCaret(self, gesture):
		obj=api.getFocusObject()
		treeInterceptor=obj.treeInterceptor
		if isinstance(treeInterceptor,treeInterceptorHandler.DocumentTreeInterceptor) and not treeInterceptor.passThrough:
			obj=treeInterceptor
		try:
			info=obj.makeTextInfo(textInfos.POSITION_CARET)
			info.expand(textInfos.UNIT_LINE)
			l = len(info.text)
			ui.message("%d" % l)
		except (NotImplementedError, RuntimeError):
			pass
	# Translators: Message presented in input help mode.
	script_reportLenToCaret.__doc__ = _("Reports the len of the current line until the caret position")

	__gestures = {
		"kb:NVDA+shift+l": "reportLenToCaret",
	}
