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
    assert(len(list(Zenny)) == 6)


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
    self.dt.gain_character(Character.RYU)

  def test_level_up(self):
    self.dt.level_up(Character.RYU)
    assert(self.dt.get_party_levels()[Character.RYU] == 2)
    self.dt.level_up(Character.RYU, levels=4)
    assert(self.dt.get_party_levels()[Character.RYU] == 6)

  @unittest.expectedFailure
  def test_level_up_missing_character(self):
    self.dt.level_up(Character.NINA)


class TestSkillInkInterface(unittest.TestCase):

  def setUp(self):
    self.dt = DataTracker()

  def test_pick_up_skill_ink(self):
    self.dt.pick_up_skill_ink()
    current_pick_up = self.dt.get_current(SkillInk.PICK_UP)
    assert(current_pick_up == 1)

  def test_buy_skill_ink(self):
    self.dt.buy_skill_ink()
    current_buy = self.dt.get_current(SkillInk.BUY)
    assert(current_buy == 1)

  def test_use_skill_ink(self):
    self.dt.use_skill_ink()
    current_use = self.dt.get_current(SkillInk.USE)
    assert(current_use == 1)

  def test_current_skill_ink(self):
    self.dt.pick_up_skill_ink()
    self.dt.buy_skill_ink()
    self.dt.use_skill_ink()
    current_sk = self.dt.get_current(SkillInk.CURRENT)
    assert(current_sk == 1)


class TestZennyInterface(unittest.TestCase):

  def setUp(self):
    self.dt = DataTracker()

  def test_pick_up_zenny(self):
    self.dt.pick_up_zenny(100)
    self.dt.pick_up_zenny(50)
    current_zenny = self.dt.get_current(Zenny.PICK_UP)
    assert(len(current_zenny) == 2)
    assert(current_zenny[0] == 100)
    assert(current_zenny[1] == 50)

  def test_boss_drop_zenny(self):
    self.dt.boss_drop_zenny(100)
    self.dt.boss_drop_zenny(50)
    current_zenny = self.dt.get_current(Zenny.BOSS_DROP)
    assert(len(current_zenny) == 2)
    assert(current_zenny[0] == 100)
    assert(current_zenny[1] == 50)

  def test_sell(self):
    self.dt.sell(100)
    self.dt.sell(50)
    current_zenny = self.dt.get_current(Zenny.SALES)
    assert(len(current_zenny) == 2)
    assert(current_zenny[0] == 100)
    assert(current_zenny[1] == 50)

  def test_buy(self):
    self.dt.buy(100)
    self.dt.buy(50)
    current_zenny = self.dt.get_current(Zenny.BUY)
    assert(len(current_zenny) == 2)
    assert(current_zenny[0] == 100)
    assert(current_zenny[1] == 50)

  def test_set_current_zenny(self):
    self.dt.set_current_zenny(100)
    current_zenny = self.dt.get_current(Zenny.CURRENT)
    assert(len(current_zenny) == 1)
    assert(current_zenny[0] == 100)
    self.dt.set_current_zenny(50)
    current_zenny = self.dt.get_current(Zenny.CURRENT)
    assert(len(current_zenny) == 1)
    assert(current_zenny[0] == 50)

  def test_get_enemy_drop(self):
    self.dt.pick_up_zenny(100)  # total 100
    self.dt.boss_drop_zenny(50) # total 150
    self.dt.sell(5)             # total 155
    self.dt.buy(75)             # total 80
    self.dt.set_current_zenny(100)
    enemy_drops = self.dt.get_current(Zenny.ENEMY_DROP)
    assert(len(enemy_drops) == 1)
    assert(enemy_drops[0] == 20)





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

  def test_skill_ink(self):
    dt = DataTracker()
    # Check default state.
    assert(dt.get_current(SkillInk.CURRENT) == 0)
    assert(dt.get_total(SkillInk.CURRENT) == 0)
    assert(dt.get_current(SkillInk.PICK_UP) == 0)
    assert(dt.get_total(SkillInk.PICK_UP) == 0)
    assert(dt.get_current(SkillInk.BUY) == 0)
    assert(dt.get_total(SkillInk.BUY) == 0)
    assert(dt.get_current(SkillInk.USE) == 0)
    assert(dt.get_total(SkillInk.USE) == 0)
    # Pick up a skill ink.
    dt.pick_up_skill_ink()
    assert(dt.get_current(SkillInk.CURRENT) == 1)
    assert(dt.get_total(SkillInk.CURRENT) == 1)
    assert(dt.get_current(SkillInk.PICK_UP) == 1)
    assert(dt.get_total(SkillInk.PICK_UP) == 1)
    assert(dt.get_current(SkillInk.BUY) == 0)
    assert(dt.get_total(SkillInk.BUY) == 0)
    assert(dt.get_current(SkillInk.USE) == 0)
    assert(dt.get_total(SkillInk.USE) == 0)
    # Split 1.
    dt.split("Pick Up Skill Ink")
    assert(dt.get_current(SkillInk.CURRENT) == 0)
    assert(dt.get_total(SkillInk.CURRENT) == 1)
    assert(dt.get_current(SkillInk.PICK_UP) == 0)
    assert(dt.get_total(SkillInk.PICK_UP) == 1)
    assert(dt.get_current(SkillInk.BUY) == 0)
    assert(dt.get_total(SkillInk.BUY) == 0)
    assert(dt.get_current(SkillInk.USE) == 0)
    assert(dt.get_total(SkillInk.USE) == 0)
    # Buy skill ink
    dt.buy_skill_ink()
    assert(dt.get_current(SkillInk.CURRENT) == 1)
    assert(dt.get_total(SkillInk.CURRENT) == 2)
    assert(dt.get_current(SkillInk.PICK_UP) == 0)
    assert(dt.get_total(SkillInk.PICK_UP) == 1)
    assert(dt.get_current(SkillInk.BUY) == 1)
    assert(dt.get_total(SkillInk.BUY) == 1)
    assert(dt.get_current(SkillInk.USE) == 0)
    assert(dt.get_total(SkillInk.USE) == 0)
    # Split 2
    dt.split("Buy Skill Ink")
    assert(dt.get_current(SkillInk.CURRENT) == 0)
    assert(dt.get_total(SkillInk.CURRENT) == 2)
    assert(dt.get_current(SkillInk.PICK_UP) == 0)
    assert(dt.get_total(SkillInk.PICK_UP) == 1)
    assert(dt.get_current(SkillInk.BUY) == 0)
    assert(dt.get_total(SkillInk.BUY) == 1)
    assert(dt.get_current(SkillInk.USE) == 0)
    assert(dt.get_total(SkillInk.USE) == 0)
    # Use skill ink
    dt.use_skill_ink()
    assert(dt.get_current(SkillInk.CURRENT) == -1)
    assert(dt.get_total(SkillInk.CURRENT) == 1)
    assert(dt.get_current(SkillInk.PICK_UP) == 0)
    assert(dt.get_total(SkillInk.PICK_UP) == 1)
    assert(dt.get_current(SkillInk.BUY) == 0)
    assert(dt.get_total(SkillInk.BUY) == 1)
    assert(dt.get_current(SkillInk.USE) == 1)
    assert(dt.get_total(SkillInk.USE) == 1)
    # Split
    dt.split("Use Skill Ink")
    assert(dt.get_current(SkillInk.CURRENT) == 0)
    assert(dt.get_total(SkillInk.CURRENT) == 1)
    assert(dt.get_current(SkillInk.PICK_UP) == 0)
    assert(dt.get_total(SkillInk.PICK_UP) == 1)
    assert(dt.get_current(SkillInk.BUY) == 0)
    assert(dt.get_total(SkillInk.BUY) == 1)
    assert(dt.get_current(SkillInk.USE) == 0)
    assert(dt.get_total(SkillInk.USE) == 1)

    # Check previous splits
    assert(dt.get_gain(SkillInk.CURRENT, 0) == 1)
    assert(dt.get_total(SkillInk.CURRENT, 0) == 1)
    assert(dt.get_gain(SkillInk.PICK_UP, 0) == 1)
    assert(dt.get_total(SkillInk.PICK_UP, 0) == 1)
    assert(dt.get_gain(SkillInk.BUY, 0) == 0)
    assert(dt.get_total(SkillInk.BUY, 0) == 0)
    assert(dt.get_gain(SkillInk.USE, 0) == 0)
    assert(dt.get_total(SkillInk.USE, 0) == 0)

    assert(dt.get_gain(SkillInk.CURRENT, 1) == 1)
    assert(dt.get_total(SkillInk.CURRENT, 1) == 2)
    assert(dt.get_gain(SkillInk.PICK_UP, 1) == 0)
    assert(dt.get_total(SkillInk.PICK_UP, 1) == 1)
    assert(dt.get_gain(SkillInk.BUY, 1) == 1)
    assert(dt.get_total(SkillInk.BUY, 1) == 1)
    assert(dt.get_gain(SkillInk.USE, 1) == 0)
    assert(dt.get_total(SkillInk.USE, 1) == 0)

    assert(dt.get_gain(SkillInk.CURRENT, 2) == -1)
    assert(dt.get_total(SkillInk.CURRENT, 2) == 1)
    assert(dt.get_gain(SkillInk.PICK_UP, 2) == 0)
    assert(dt.get_total(SkillInk.PICK_UP, 2) == 1)
    assert(dt.get_gain(SkillInk.BUY, 2) == 0)
    assert(dt.get_total(SkillInk.BUY, 2) == 1)
    assert(dt.get_gain(SkillInk.USE, 2) == 1)
    assert(dt.get_total(SkillInk.USE, 2) == 1)


#
# 
# DataTracker.Entry

class TestEntry(unittest.TestCase):

  def test(self):
    pass


if __name__ == "__main__":
  unittest.main()

