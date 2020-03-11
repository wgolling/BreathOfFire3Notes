from datatracker import *

import unittest

#
#
# Enums

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
    assert(len(list(Weapon)) == 16)

#
#
# Helper methods

class TestHelperMethods(unittest.TestCase):

  #
  # Add key/value to dict

  def test_add_key_value_to_dict(self):
    d = {"buh": 1, DAGGER: 2}
    add_key_value_to_dict(d, 7, 8)
    add_key_value_to_dict(d, DAGGER, 1)
    assert(d == {"buh": 1, DAGGER: 3, 7: 8})

  def test_add_key_value_to_dict_wrong_dict_type(self):
    with self.assertRaises(TypeError):
      add_dicts(0, 0, 0)    

  def test_add_key_value_to_dict_wrong_value_type(self):
    with self.assertRaises(TypeError):
      add_dicts(dict(), 0, "buh")    

  #
  # Add dicts

  def test_add_dicts(self):
    d1 = {"buh": 1, DAGGER: 2}
    d2 = {DAGGER: 1, 7: 8}
    d3 = add_dicts(d1, d2)
    assert(d3 == {"buh": 1, DAGGER: 3, 7: 8})

  def test_add_dicts_wrong_type(self):
    with self.assertRaises(TypeError):
      add_dicts(0, dict())    
    with self.assertRaises(TypeError):
      add_dicts(dict(), 0)    

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
    assert(levels[RYU]    == 1)
    assert(levels[REI]    == 5)
    assert(levels[TEEPO]  == 1)
    assert(levels[NINA]   == 5)
    assert(levels[MOMO]   == 10)
    assert(levels[PECO]   == 1)
    assert(levels[GARR]   == 13)

  def test_weapon_requirements(self):
    reqs = DataTracker.WEAPON_REQUIREMENTS
    for w in Weapon:
      if w in [DAGGER, BALLOCK_KNIFE, BENT_SWORD, POINTED_STICK]:
        assert(reqs[w] == 2)
      else:
        assert(reqs[w] == 1)

class TestCharacterInterface(unittest.TestCase):

  def setUp(self):
    self.dt = DataTracker()

  def test_get_party_levels(self):
    pl = self.dt.get_party_levels()
    for c in list(Character):
      assert(c in pl)
      assert(pl[c] == DataTracker.STARTING_LEVELS[c])

  def test_gain_character(self):
    self.dt.gain_character(NINA)
    assert(NINA in self.dt.get_party())
    assert(self.dt.get_party_levels()[NINA] == 5)

  def test_gain_duplicate_character(self):
    with self.assertRaises(KeyError):
      self.dt.gain_character(RYU)

  def test_gain_character_wrong_type(self):
    with self.assertRaises(TypeError):
      self.dt.gain_character("buh")

  def test_lose_character(self):
    self.dt.level_up(RYU)
    self.dt.lose_character(RYU)
    assert(RYU not in self.dt.get_party())
    assert(self.dt.get_party_levels()[RYU] == 2)
    self.dt.gain_character(RYU)
    assert(RYU in self.dt.get_party())
    assert(self.dt.get_party_levels()[RYU] == 2)

  def test_lose_character_wrong_type(self):
    with self.assertRaises(TypeError):
      self.dt.lose_character("buh")

  def test_lose_character_missing(self):
    with self.assertRaises(KeyError):
      self.dt.lose_character(NINA)

  def test_level_up(self):
    self.dt.level_up(RYU)
    assert(self.dt.get_party_levels()[RYU] == 2)
    self.dt.level_up(RYU, levels=4)
    assert(self.dt.get_party_levels()[RYU] == 6)

  def test_level_up_wrong_type(self):
    with self.assertRaises(TypeError):
      self.dt.level_up("buh")

  def test_level_up_missing_character(self):
    with self.assertRaises(KeyError):
      self.dt.level_up(NINA)

  def test_level_up_nonpositive_level(self):
    with self.assertRaises(ValueError):
      self.dt.level_up(RYU, levels=0)

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

  def test_buy_skill_ink_nonpositive_amount(self):
    with self.assertRaises(ValueError):
      self.dt.buy_skill_ink(amt=0)

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
    current_zenny = self.dt.get_current_raw(Zenny.PICK_UP)
    assert(len(current_zenny) == 2)
    assert(current_zenny[0] == 100)
    assert(current_zenny[1] == 50)

  def test_pick_up_zenny_nonpositive_amount(self):
    with self.assertRaises(ValueError):
      self.dt.pick_up_zenny(amt=0)

  def test_boss_drop_zenny(self):
    self.dt.boss_drop_zenny(100)
    self.dt.boss_drop_zenny(50)
    current_zenny = self.dt.get_current_raw(Zenny.BOSS_DROP)
    assert(len(current_zenny) == 2)
    assert(current_zenny[0] == 100)
    assert(current_zenny[1] == 50)
    assert(current_zenny == [100, 50])

  def test_boss_drop_zenny_nonpositive_amount(self):
    with self.assertRaises(ValueError):
      self.dt.boss_drop_zenny(amt=0)

  def test_sell(self):
    self.dt.sell(100)
    self.dt.sell(50)
    current_zenny = self.dt.get_current_raw(Zenny.SALES)
    assert(len(current_zenny) == 2)
    assert(current_zenny[0] == 100)
    assert(current_zenny[1] == 50)

  def test_sell_nonpositive_amount(self):
    with self.assertRaises(ValueError):
      self.dt.sell(amt=0)

  def test_buy(self):
    self.dt.buy(100)
    self.dt.buy(50)
    current_zenny = self.dt.get_current_raw(Zenny.BUY)
    assert(len(current_zenny) == 2)
    assert(current_zenny[0] == 100)
    assert(current_zenny[1] == 50)

  def test_buy_nonpositive_amount(self):
    with self.assertRaises(ValueError):
      self.dt.buy(amt=0)

  def test_set_current_zenny(self):
    self.dt.set_current_zenny(100)
    current_zenny = self.dt.get_current(Zenny.CURRENT)
    assert(current_zenny == 100)
    self.dt.set_current_zenny(50)
    current_zenny = self.dt.get_current(Zenny.CURRENT)
    assert(current_zenny == 50)

  def test_set_current_zenny(self):
    with self.assertRaises(ValueError):
      self.dt.set_current_zenny(amt=-1)

  def test_get_enemy_drop(self):
    self.dt.pick_up_zenny(100)  # total 100
    self.dt.boss_drop_zenny(50) # total 150
    self.dt.sell(5)             # total 155
    self.dt.buy(75)             # total 80
    self.dt.set_current_zenny(100)
    enemy_drops = self.dt.get_current(Zenny.ENEMY_DROP)
    assert(enemy_drops == 20)

class TestWeaponInterface(unittest.TestCase):

  def setUp(self):
    self.dt = DataTracker()

  def test_pick_up_weapon(self):
    dt = self.dt
    dt.pick_up_weapon(DAGGER)
    weapons = dt.get_weapons()
    assert(weapons[DAGGER] == 2)

  def test_pick_up_weapon_wrong_type(self):
    with self.assertRaises(TypeError):
      self.dt.pick_up_weapon("buh")

  def test_buy_weapon(self):
    dt = self.dt
    dt.buy_weapon(DAGGER, 50)
    weapons = dt.get_weapons()
    assert(weapons[DAGGER] == 2)
    assert(dt.get_current(Zenny.BUY) == 50)
    assert(dt.get_current_raw(Zenny.BUY) == [50])

  def test_buy_weapon_wrong_type(self):
    with self.assertRaises(TypeError):
      self.dt.buy_weapon("buh")

  def test_buy_weapon_nonpositive_amount(self):
    with self.assertRaises(ValueError):
      self.dt.buy_weapon(DAGGER, cost=0)

  def test_have_all_weapons(self):
    dt = self.dt
    assert(not dt.have_all_weapons())
    for w in list(Weapon):
      assert(not dt.have_all_weapons())
      while dt.get_weapons()[w] < DataTracker.WEAPON_REQUIREMENTS[w]:
        dt.pick_up_weapon(w)
    assert(dt.have_all_weapons())

class TestSplitting(unittest.TestCase):

  def setUp(self):
    self.dt = DataTracker()

  def test_number_of_splits(self):
    for x in range(10):
      assert(self.dt.number_of_splits() == x)
      self.dt.split(str(x), 0)
    assert(self.dt.number_of_splits() == 10)

  def test_split_name(self):
    dt = self.dt
    dt.split("Test split", 0)
    assert(dt.get_name(0) == "Test split")

  def test_party_levels(self):
    dt = self.dt
    assert(RYU in dt.current_entry.party)
    dt.level_up(RYU)
    assert(dt.get_party_levels()[RYU] == 2)
    dt.split("Level Up Ryu", 0)
    assert(RYU in dt.current_entry.party)
    assert(dt.get_party_levels()[RYU] == 2)
    dt.level_up(RYU)
    assert(dt.get_party_levels()[RYU] == 3)

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
    dt.split("Pick Up Skill Ink", 0)
    self.skill_ink_helper(tc=1, tp=1)
    # Buy skill ink
    dt.buy_skill_ink()
    self.skill_ink_helper(cc=1, tc=2, tp=1, cb=1, tb=1)
    # Split 2
    dt.split("Buy Skill Ink", 0)
    self.skill_ink_helper(tc=2, tp=1, tb=1)
    # Use skill ink
    dt.use_skill_ink()
    self.skill_ink_helper(cc=-1, tc=1, tp=1, tb=1, cu=1, tu=1)
    # Split
    dt.split("Use Skill Ink", 0)
    self.skill_ink_helper(tc=1, tp=1, tb=1, tu=1)

    # Check previous splits
    self.skill_ink_helper_with_split(0, gc=1, tc=1, gp=1, tp=1)
    self.skill_ink_helper_with_split(1, gc=1, tc=2, tp=1, gb=1, tb=1)
    self.skill_ink_helper_with_split(2, gc=-1, tc=1, tp=1, tb=1, gu=1, tu=1)

  #
  # Test Zenny

  def test_zenny(self):
    dt = self.dt
    dt.pick_up_zenny(100)
    dt.pick_up_zenny(50) # 150
    dt.boss_drop_zenny(500) # 650
    dt.sell(120) 
    dt.sell(50) # 820
    dt.buy(600) # 220
    dt.split("Pick up zenny", 250)
    assert(dt.get_gain_raw(Zenny.PICK_UP    , 0) == [100, 50])
    assert(dt.get_total(Zenny.PICK_UP   , 0) == 150)
    assert(dt.get_gain_raw(Zenny.BOSS_DROP  , 0) == [500])
    assert(dt.get_total(Zenny.BOSS_DROP , 0) == 500)
    assert(dt.get_gain_raw(Zenny.SALES      , 0) == [120, 50])
    assert(dt.get_total(Zenny.SALES     , 0) == 170)
    assert(dt.get_gain_raw(Zenny.BUY        , 0) == [600])
    assert(dt.get_total(Zenny.BUY       , 0) == 600)
    assert(dt.get_gain_raw(Zenny.CURRENT    , 0) == 250)
    assert(dt.get_total(Zenny.CURRENT   , 0) == 250)
    assert(dt.get_gain_raw(Zenny.ENEMY_DROP , 0) == 30)
    assert(dt.get_total(Zenny.ENEMY_DROP, 0) == 30)

    assert(dt.get_current_raw(Zenny.PICK_UP    ) == [])
    assert(dt.get_total(Zenny.PICK_UP   , 1) == 150)
    assert(dt.get_current_raw(Zenny.BOSS_DROP  ) == [])
    assert(dt.get_total(Zenny.BOSS_DROP , 1) == 500)
    assert(dt.get_current_raw(Zenny.SALES      ) == [])
    assert(dt.get_total(Zenny.SALES     , 1) == 170)
    assert(dt.get_current_raw(Zenny.BUY        ) == [])
    assert(dt.get_total(Zenny.BUY       , 1) == 600)
    assert(dt.get_current_raw(Zenny.CURRENT    ) == 0)
    assert(dt.get_total(Zenny.CURRENT   , 1) == 250)
    assert(dt.get_current_raw(Zenny.ENEMY_DROP ) == 0)
    assert(dt.get_total(Zenny.ENEMY_DROP, 1) == 30)

    dt.split("Another split", 250)
    assert(dt.get_gain_raw(Zenny.PICK_UP    , 1) == [])
    assert(dt.get_total(Zenny.PICK_UP   , 1) == 150)
    assert(dt.get_gain_raw(Zenny.BOSS_DROP  , 1) == [])
    assert(dt.get_total(Zenny.BOSS_DROP , 1) == 500)
    assert(dt.get_gain_raw(Zenny.SALES      , 1) == [])
    assert(dt.get_total(Zenny.SALES     , 1) == 170)
    assert(dt.get_gain_raw(Zenny.BUY        , 1) == [])
    assert(dt.get_total(Zenny.BUY       , 1) == 600)
    assert(dt.get_gain_raw(Zenny.CURRENT    , 1) == 0)
    assert(dt.get_total(Zenny.CURRENT   , 1) == 250)
    assert(dt.get_gain_raw(Zenny.ENEMY_DROP , 1) == 0)
    assert(dt.get_total(Zenny.ENEMY_DROP, 1) == 30)
  #
  # Test Weapons

  def test_weapons(self):
    dt = self.dt
    dt.pick_up_weapon(DAGGER)
    dt.buy_weapon(BALLOCK_KNIFE, 50)
    dt.split("Get stuff", 0)
    dt.pick_up_weapon(DAGGER)
    weapons = dt.get_weapons()
    assert(weapons[DAGGER] == 3)
    assert(weapons[BALLOCK_KNIFE] == 1)
    assert(dt.get_total(Zenny.BUY) == 50)

class TestGetterMethodErrors(unittest.TestCase):

  def setUp(self):
    self.dt = DataTracker()

  #
  # Helper methods

  def out_of_bounds(self, function):
    with self.assertRaises(IndexError):
      function(-1)
    with self.assertRaises(IndexError):
      function(0)
    self.dt.split("Test split", 0)
    with self.assertRaises(IndexError):
      function(1)

  def wrong_key_type(self, function):
    with self.assertRaises(KeyError):
      function("buh")

  #
  # Split name
  
  def test_split_name_out_of_bounds(self):
    self.out_of_bounds(self.dt.get_name)

  #
  # Party levels

  def test_party_levels_out_of_bounds(self):
    self.out_of_bounds(lambda split: self.dt.get_party_levels(split=split))

  #
  # Weapons

  def test_get_weapons_out_of_bounds(self):
    self.out_of_bounds(lambda split: self.dt.get_weapons(split=split))

  #
  # Gain

  def test_get_gain_out_of_bounds(self):
    self.out_of_bounds(lambda split: self.dt.get_gain(Zenny.PICK_UP, split))

  def test_get_gain_wrong_type(self):
    self.dt.split("Test", 0)
    self.wrong_key_type(lambda att: self.dt.get_gain(att, 0))

  #
  # Total

  def test_get_total_out_of_bounds(self):
    with self.assertRaises(IndexError):
      self.dt.get_total(Zenny.PICK_UP, -1)
    with self.assertRaises(IndexError):
      self.dt.get_total(Zenny.PICK_UP, 1)
    self.dt.split("Test split", 0)
    with self.assertRaises(IndexError):
      self.dt.get_total(Zenny.PICK_UP, 2)

  def test_get_total_wrong_type(self):
    self.wrong_key_type(lambda att: self.dt.get_total(att, 0))

  #
  # Current

  def test_get_current_wrong_type(self):
    self.wrong_key_type(self.dt.get_current)

  #
  # Strings

  def test_get_strings(self):
    dt = self.dt
    dt.gain_character(NINA)
    dt.level_up(RYU)
    dt.split("First split", 0)
    strings = dt.get_strings()
    gains = strings[0]['party_levels']['gain']
    assert(gains[RYU] == '2')

if __name__ == "__main__":
  unittest.main()
