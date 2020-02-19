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
# 
# DataTracker
 
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


class TestCharacterInterface(unittest.TestCase):

  def setUp(self):
    self.dt = DataTracker()

  def test_get_party_levels(self):
    pl = self.dt.get_party_levels()
    assert(pl[Character.RYU] == 1)
    assert(not Character.NINA in pl)

  def test_gain_character(self):
    self.dt.gain_character(Character.NINA)
    assert(self.dt.get_party_levels()[Character.NINA] == 5)

  @unittest.expectedFailure
  def test_gain_duplicate_character(self):
    self.dt.gain_character(C.RYU)

  def test_level_up(self):
    self.dt.level_up(Character.RYU)
    assert(self.dt.get_party_levels()[Character.RYU] == 2)
    self.dt.level_up(Character.RYU, levels=4)
    assert(self.dt.get_party_levels()[Character.RYU] == 6)



class TestSplitting(unittest.TestCase):

  def test_split_name(self):
    dt = DataTracker()
    assert(len(dt.entries) == 1)
    dt.split("Test split")
    assert(len(dt.entries) == 2)
    assert(dt.get("name", 0) == "Test split")
    assert(dt.get("name", 1) == None)

  def test_party_levels(self):
    dt = DataTracker()
    assert(Character.RYU in dt.current_entry.party)
    dt.level_up(Character.RYU)
    assert(dt.get_party_levels()[Character.RYU] == 2)
    dt.split("Level Up Ryu")
    assert(Character.RYU in dt.current_entry.party)
    assert(dt.get_party_levels()[Character.RYU] == 2)
    dt.level_up(Character.RYU)
    assert(dt.get_party_levels()[Character.RYU] == 3)


#
# 
# DataTracker.Entry

class TestEntry(unittest.TestCase):

  def test(self):
    pass


if __name__ == "__main__":
  unittest.main()

