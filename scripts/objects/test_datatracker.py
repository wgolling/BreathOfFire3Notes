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

  def setUp(self):
    self.dt = DataTracker()

  def test_split_name(self):
    dt = self.dt
    assert(len(dt.entries) == 1)
    dt.split("Test split")
    assert(len(dt.entries) == 2)
    assert(dt.get("name", 0) == "Test split")
    assert(dt.get("name", 1) == None)

  def test_party_levels(self):
    dt = self.dt
    assert(Character.RYU in dt.current_entry.party)
    dt.level_up(Character.RYU)
    assert(dt.get_party_levels()[Character.RYU] == 2)
    dt.split("Level Up Ryu")
    assert(Character.RYU in dt.current_entry.party)
    assert(dt.get_party_levels()[Character.RYU] == 2)
    dt.level_up(Character.RYU)
    assert(dt.get_party_levels()[Character.RYU] == 3)


  #
  # Test Skill Ink
  def skill_ink_helper(self, cc=0, tc=0, cp=0, tp=0, cb=0, tb=0, cu=0, tu=0):
    assert(self.dt.get_current(SkillInk.CURRENT) == cc)
    assert(self.dt.get_total(SkillInk.CURRENT)   == tc)
    assert(self.dt.get_current(SkillInk.PICK_UP) == cp)
    assert(self.dt.get_total(SkillInk.PICK_UP)   == tp)
    assert(self.dt.get_current(SkillInk.BUY)     == cb)
    assert(self.dt.get_total(SkillInk.BUY)       == tb)
    assert(self.dt.get_current(SkillInk.USE)     == cu)
    assert(self.dt.get_total(SkillInk.USE)       == tu)

  def skill_ink_helper_with_split(self, split, gc=0, tc=0, gp=0, tp=0, gb=0, tb=0, gu=0, tu=0):
    assert(self.dt.get_gain(SkillInk.CURRENT, split)   == gc)
    assert(self.dt.get_total(SkillInk.CURRENT, split)  == tc)
    assert(self.dt.get_gain(SkillInk.PICK_UP, split)   == gp)
    assert(self.dt.get_total(SkillInk.PICK_UP, split)  == tp)
    assert(self.dt.get_gain(SkillInk.BUY, split)       == gb)
    assert(self.dt.get_total(SkillInk.BUY, split)      == tb)
    assert(self.dt.get_gain(SkillInk.USE, split)       == gu)
    assert(self.dt.get_total(SkillInk.USE, split)      == tu)

  def test_skill_ink(self):
    dt = self.dt
    # Check default state.
    self.skill_ink_helper()
    # Pick up a skill ink.
    dt.pick_up_skill_ink()
    self.skill_ink_helper(cc=1, tc=1, cp=1, tp=1)
    # Split 1.
    dt.split("Pick Up Skill Ink")
    self.skill_ink_helper(tc=1, tp=1)
    # Buy skill ink
    dt.buy_skill_ink()
    self.skill_ink_helper(cc=1, tc=2, tp=1, cb=1, tb=1)
    # Split 2
    dt.split("Buy Skill Ink")
    self.skill_ink_helper(tc=2, tp=1, tb=1)
    # Use skill ink
    dt.use_skill_ink()
    self.skill_ink_helper(cc=-1, tc=1, tp=1, tb=1, cu=1, tu=1)
    # Split
    dt.split("Use Skill Ink")
    self.skill_ink_helper(tc=1, tp=1, tb=1, tu=1)

    # Check previous splits
    self.skill_ink_helper_with_split(0, gc=1, tc=1, gp=1, tp=1)
    self.skill_ink_helper_with_split(1, gc=1, tc=2, tp=1, gb=1, tb=1)
    self.skill_ink_helper_with_split(2, gc=-1, tc=1, tp=1, tb=1, gu=1, tu=1)




#
# 
# DataTracker.Entry

class TestEntry(unittest.TestCase):

  def test(self):
    pass


if __name__ == "__main__":
  unittest.main()

