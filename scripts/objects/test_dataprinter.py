from dataprinter import *
from datatracker import DataTracker

import unittest

class TestConstructor(unittest.TestCase):

  def test_constructor(self):
    dp = DataPrinter("Test", DataTracker())


class TestOutput(unittest.TestCase):

  def test_print_entry(self):
    dt = DataTracker()
    dp = DataPrinter("Test", dt)
    dt.split("Test")
    with self.assertRaises(IndexError):
      dp.print_entry(-1)
    with self.assertRaises(IndexError):
      dp.print_entry(1)
    dp.print_entry(0)

