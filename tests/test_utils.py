#!/usr/bin/env python

# Copyright (C) 2022 Noelia Ruiz Martínez
# This file may be used under the terms of the GNU General Public License, version 2 or later.
# For more details see: https://www.gnu.org/licenses/gpl-2.0.html

import os
import sys
from unittest import TestCase
from unittest.mock import MagicMock, patch

TOP_DIR = os.path.abspath(os.path.dirname(__file__))
SOURCE_DIR = os.path.dirname(TOP_DIR)
PLUGIN_DIR = os.path.join(SOURCE_DIR, "addon", "globalPlugins", "cursorLocator")

config = MagicMock
config.conf = dict()
sys.modules['config'] = config
sys.path.append(PLUGIN_DIR)
import utils  # NOQA: E402
del sys.path[-1]

confspec = {
	"reportLineLength": 0,
		"maxStartNotificationNumber": 0,
	"maxEndNotificationNumber": 0
}
config.conf["cursorLocator"] = confspec

class TestUtilsConfigFunctions(TestCase):

	def test_getReportLineLength(self):
		reportLineLength = config.conf["cursorLocator"]["reportLineLength"]
		self.assertEqual(utils.getReportLineLength(), reportLineLength, f"should be {reportLineLength}")

	def test_getMaxStartNotificationNumber(self):
		maxStartNotificationNumber = config.conf["cursorLocator"]["maxStartNotificationNumber"]
		self.assertEqual(utils.getMaxStartNotificationNumber(), maxStartNotificationNumber, f"shold be {maxStartNotificationNumber}")

	def test_getMaxEndNotificationNumber(self):
		maxEndNotificationNumber = config.conf["cursorLocator"]["maxEndNotificationNumber"]
		self.assertEqual(utils.getMaxEndNotificationNumber(), maxEndNotificationNumber, f"shold be {maxEndNotificationNumber}")


class TestUtilsReportStart(TestCase):

	def setUp(self):
		self.text = "H"
		self.reportLineLength = 1
		config.conf["cursorLocator"]["maxStartNotificationNumber"] =  1

	def tearDown(self):
		self.text = None
		self.reportLineLength = 0
		config.conf["cursorLocator"]["maxStartNotificationNumber"]= 0

	def test_valid(self):
		self.assertTrue(utils.shouldReportStartOfLine(self.text), "should be true")

	def test_lenText0(self):
		self.text = ""
		self.assertFalse(utils.shouldReportStartOfLine(self.text), "should be false")

	def test_MaxStartNotificationNumber2(self):
		config.conf["cursorLocator"]["maxStartNotificationNumber"] = 2
		self.assertTrue(utils.shouldReportStartOfLine(self.text), "should be true")
		self.text= "He"
		self.assertTrue(utils.shouldReportStartOfLine(self.text), "should be true")
		self.text = "Hel"
		self.assertFalse(utils.shouldReportStartOfLine(self.text), "should be false")

	def test_MaxStartNotificationNumber0(self):
		config.conf["cursorLocator"]["maxStartNotificationNumber"] = 0
		self.assertFalse(utils.shouldReportStartOfLine(self.text), "should be false")

	@patch("utils.shouldReportEndOfLine")
	def test_reportEndOfLineIsTrue(self, mockShouldReportEndOfLine):
		mockShouldReportEndOfLine.return_value = True
		self.assertEqual(utils.shouldReportStartOfLine(self.text), False, "should be false")


class TestUtilsReportEnd(TestCase):

	def setUp(self):
		self.text = "Hello"
		config.conf["cursorLocator"]["reportLineLength"] = 5
		config.conf["cursorLocator"]["maxEndNotificationNumber"] =  1

	def tearDown(self):
		self.text = None
		config.conf["cursorLocator"]["reportLineLength"] = 0
		config.conf["cursorLocator"]["maxEndNotificationNumber"]= 0

	def test_valid(self):
		self.assertTrue(utils.shouldReportEndOfLine(self.text), "should be true")

	def test_lenTextMinorThanReportLineLength(self):
		self.text = "Hell"
		self.assertFalse(utils.shouldReportEndOfLine(self.text), "should be false")

	def reportLineLengthZero(self):
		config.conf["cursorLocator"]["reportLineLength"] = 0
		self.assertFalse(utils.shouldReportEndOfLine(self.text), "should be false")

	def test_maxEndNotificationNumber2(self):
		config.conf["cursorLocator"]["maxEndNotificationNumber"] = 2
		self.assertTrue(utils.shouldReportEndOfLine(self.text), "should be true")
		self.text = "Hello,"
		self.assertTrue(utils.shouldReportEndOfLine(self.text), "should be true")
		self.text = "Hello, "
		self.assertFalse(utils.shouldReportEndOfLine(self.text), "should be true")

	def test_MaxEndNotificationNumber0(self):
		config.conf["cursorLocator"]["maxEndNotificationNumber"] = 0
		self.assertFalse(utils.shouldReportEndOfLine(self.text), "should be false")
