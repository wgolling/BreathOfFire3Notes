import datatracker
from datatracker import *

import unittest

class TestConstructor(unittest.TestCase):

  def test_constructor(self):
    dt = DataTracker()
    assert(dt)


if __name__ == "__main__":
  unittest.main()

