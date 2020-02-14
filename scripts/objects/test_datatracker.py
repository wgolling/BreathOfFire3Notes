import datatracker
from datatracker import *

import unittest


#
# Enums
#

class TestCharacter(unittest.TestCase):

  def test_character_enum(self):
    assert(Character)
    assert(len(list(Character)) == 7)


class TestSkillInk(unittest.TestCase):

  def test_skill_ink_enum(self):
    assert(SkillInk)
    assert(len(list(SkillInk)) == 4)


class TestZenny(unittest.TestCase):

  def test_zenny_enum(self):
    assert(Zenny)
    assert(len(list(Zenny)) == 5)


class TestWeapon(unittest.TestCase):

  def test_weapon_enum(self):
    assert(Weapon)
    assert(len(list(Weapon)) == 15)


#
# DataTracker
#
 
class TestConstructor(unittest.TestCase):

  def test_constructor(self):
    dt = DataTracker()
    assert(dt)


class TestStaticFields(unittest.TestCase):

  def test_starting_levels(self):
    levels = DataTracker.STARTING_LEVELS
    assert(levels[Character.RYU]    == 1)
    assert(levels[Character.REI]    == 5)
    assert(levels[Character.TEEPO]  == 1)
    assert(levels[Character.NINA]   == 5)
    assert(levels[Character.MOMO]   == 10)
    assert(levels[Character.PECO]   == 1)
    assert(levels[Character.GARR]   == 13)

  def test_weapon_requirements(self):
    reqs = DataTracker.WEAPON_REQUIREMENTS
    for w in Weapon:
      if w in [Weapon.DAGGER, Weapon.BALLOCK_KNIFE, Weapon.BENT_SWORD, Weapon.POINTED_STICK]:
        assert(reqs[w] == 2)
      else:
        assert(reqs[w] == 1)



if __name__ == "__main__":
  unittest.main()

