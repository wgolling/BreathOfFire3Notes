from dataprinter import *
from datatracker import DataTracker

import unittest

class TestConstructor(unittest.TestCase):

  def test_constructor(self):
    dp = DataPrinter("Test", DataTracker().get_strings())


class TestOutput(unittest.TestCase):

  def test_print_entry(self):
    dt = DataTracker()
    dt.split("Test")
    dp = DataPrinter("Test", dt.get_strings())
    with self.assertRaises(IndexError):
      dp.print_entry(-1)
    with self.assertRaises(IndexError):
      dp.print_entry(1)
    dp.print_entry(0)

