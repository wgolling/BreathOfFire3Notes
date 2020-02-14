import datatracker
from datatracker import *

import unittest

class TestCharacter(unittest.TestCase):

  def test_character_enum(self):
    assert(Character)
    assert(len(list(Character)) == 7)
    levels = datatracker.STARTING_LEVELS
    assert(levels[Character.RYU]    == 1)
    assert(levels[Character.REI]    == 5)
    assert(levels[Character.TEEPO]  == 1)
    assert(levels[Character.NINA]   == 5)
    assert(levels[Character.MOMO]   == 10)
    assert(levels[Character.PECO]   == 1)
    assert(levels[Character.GARR]   == 13)


class TestSkillInk(unittest.TestCase):

  def test_skill_ink_enum(self):
    assert(SkillInk)
    assert(len(list(SkillInk)) == 4)


class TestZenny(unittest.TestCase):

  def test_zenny_enum(self):
    assert(Zenny)
    assert(len(list(Zenny)) == 5)

class TestConstructor(unittest.TestCase):

  def test_constructor(self):
    dt = DataTracker()
    assert(dt)


if __name__ == "__main__":
  unittest.main()

