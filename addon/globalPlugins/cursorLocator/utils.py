# -*- coding: UTF-8 -*-

# cursorLocator/utils.py
# Copyright (C) 2022 Noelia Ruiz Martínez
# Released under GPL 2

import config


def getReportLineLength() -> int:
	return config.conf["cursorLocator"]["reportLineLength"]


def getMaxStartNotificationNumber() -> int:
	return config.conf["cursorLocator"]["maxStartNotificationNumber"]


def getMaxEndNotificationNumber() -> int:
	return config.conf["cursorLocator"]["maxEndNotificationNumber"]


def shouldReportStartOfLine(text: str) -> bool:
	reportLineLength = 1
	if len(text) < reportLineLength:
		return False
	if shouldReportEndOfLine(text):
		return False
	maxStartNotificationNumber = getMaxStartNotificationNumber()
	if len(text) < (reportLineLength + maxStartNotificationNumber):
		return True
	return False


def shouldReportEndOfLine(text: str) -> bool:
	reportLineLength = getReportLineLength()
	if not reportLineLength or len(text) < reportLineLength:
		return False
	maxEndNotificationNumber = getMaxEndNotificationNumber()
	if len(text) < (reportLineLength + maxEndNotificationNumber):
		return True
	return False
