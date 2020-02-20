from enum import Enum, auto
from collections import defaultdict

#
# Enums

class Character(Enum):
  RYU   = auto()
  REI   = auto()
  TEEPO = auto()
  NINA  = auto()
  MOMO  = auto()
  PECO  = auto()
  GARR  = auto()


class SkillInk(Enum):
  PICK_UP = auto()
  BUY     = auto()
  USE     = auto()
  CURRENT = auto()


class Zenny(Enum):
  PICK_UP     = auto()
  BOSS_DROP   = auto()
  ENEMY_DROP  = auto()
  SALES       = auto()
  CURRENT     = auto()


class Weapon(Enum):
  MELTED_BLADE  = auto()
  DAGGER        = auto()
  BALLOCK_KNIFE = auto()
  BENT_SWORD    = auto()
  BRONZE_SWORD  = auto()
  POINTED_STICK = auto()
  SILVER_KNIFE  = auto()
  BROAD_SWORD   = auto()
  OAKEN_STAFF   = auto()
  MACE          = auto()
  SCRAMASAX     = auto()
  MAGICIAN_ROD  = auto()
  RIPPERS       = auto()
  ICE_CHRYSM    = auto()      
  FIRE_CHRYSM   = auto()


#
#
# Helper functions

def add_key_value_to_dict(d, k, v):
  '''
  Mutates dict
  '''
  old_val = 0
  if k in d:
    old_val = d[k]
  d[k] = v + old_val

def add_dicts(d1, d2):
  '''
  Returns a new dict
  '''
  new_dict = dict(d1)
  for k in d2:
    add_key_value_to_dict(new_dict, k, d2[k])
  return new_dict 


class DataTracker:

  #
  # Static fields

  # Chracter starting levels
  STARTING_LEVELS = {
    Character.RYU:    1,
    Character.REI:    5,
    Character.TEEPO:  1,
    Character.NINA:   5,
    Character.MOMO:   10,
    Character.PECO:   1,
    Character.GARR:   13,
  }

  # Weapon requirments for D'Lonzo
  def make_weapon_requirements():
    duplicates = [Weapon.DAGGER, Weapon.BALLOCK_KNIFE, Weapon.BENT_SWORD, Weapon.POINTED_STICK]
    return dict(map(lambda w: (w, 2 if w in duplicates else 1), list(Weapon)))
  WEAPON_REQUIREMENTS = make_weapon_requirements()

  #
  #
  # Constructor

  def __init__(self):
    self.entries = [DataTracker.Entry()]
    self.current_entry = self.entries[0]
    self.totals = []
    self.gain_character(Character.RYU)

  #
  #
  # Interface methods

  #
  # Incrementing methods

  # Character
  def gain_character(self, character):
    p = self.current_entry.party
    assert(not character in p)
    p.add(character)
    self.current_entry.party_levels[character] = self.STARTING_LEVELS[character]

  def level_up(self, character, levels=1):
    assert(character in self.current_entry.party)
    pl = self.current_entry.party_levels
    add_key_value_to_dict(pl, character, levels)

  # Skill Ink
  def pick_up_skill_ink(self):
    sk = self.current_entry.skill_ink
    add_key_value_to_dict(sk, SkillInk.PICK_UP, 1)

  def buy_skill_ink(self, amt=1):
    sk = self.current_entry.skill_ink
    add_key_value_to_dict(sk, SkillInk.BUY, amt)

  def use_skill_ink(self):
    sk = self.current_entry.skill_ink
    add_key_value_to_dict(sk, SkillInk.USE, 1)

  # Zenny
  def pick_up_zenny(self, amt):
    pass

  def boss_drop_zenny(self, amt):
    pass

  def sell(self, item, amt):
    pass

  def set_current_zenny(self, amt):
    pass

  # Weapon
  def pick_up_weapon(self, weapon):
    pass 

  def buy_weapon(self, weapon):
    pass

  #
  # Split
  def split(self, name):
    # Finalize current entry
    self.current_entry.name = str(name)
    self.current_entry.finalize()
    # Compute totals
    previous_totals = self.get_previous_totals()
    totals_entry = DataTracker.Entry.new_totals_entry(self.current_entry, previous_totals)
    self.totals.append(totals_entry)
    # Make new entry
    self.current_entry = DataTracker.Entry.new_current_entry(totals_entry)
    self.entries.append(self.current_entry)

  def get_previous_totals(self):
    if not self.totals:
      return DataTracker.Entry()
    else:
      return self.totals[len(self.totals) - 1]

  #  
  # Getting methods

  def get_party_levels(self, split=None):
    if split:
      return dict(self.totals[split].party_levels)
    return add_dicts(
        self.get_previous_totals().party_levels, 
        self.current_entry.party_levels)

  def get_gain(self, attribute, split):
    return self.entries[split].get(attribute)

  def get_total(self, attribute, split=-1):
    if (split == -1) or (split == len(self.entries) - 1):
      gain = self.get_current(attribute)
      prev_total = self.get_previous_totals().get(attribute)
      return gain + prev_total
    return self.totals[split].get(attribute)

  def get_current(self, attribute):
    return self.current_entry.get(attribute)

  # General get method
  def get(self, attribute, split):
    if attribute == "name":
      return self.entries[split].name




  class Entry:
    def __init__(self, entry=None):
      if entry:
        assert(isinstance(entry, DataTracker.Entry))
      self.finalized = False
      self.name = None
      self.party = set()
      self.party_levels = dict()
      self.skill_ink = dict(map(lambda a : (a, 0), list(SkillInk)))

    def new_totals_entry(current_entry, previous_totals):
      e = DataTracker.Entry()
      # set name
      e.name = current_entry.name
      # set party
      e.party = set(current_entry.party)
      current_gains = current_entry.party_levels
      previous_levels = previous_totals.party_levels
      e.party_levels = add_dicts(current_gains, previous_levels)
      # set skill ink
      e.skill_ink = add_dicts(current_entry.skill_ink, previous_totals.skill_ink)
      # Finalize
      e.finalize()
      return e

    def new_current_entry(totals_entry):
      e = DataTracker.Entry()
      e.party = set(totals_entry.party)
      return e

    def finalize(self):
      self.skill_ink[SkillInk.CURRENT] = self.current_skill_ink()
      self.finalized = True


    #
    # Getting methods
    def get(self, attribute):
      if isinstance(attribute, SkillInk):
        if attribute == SkillInk.CURRENT:
          return self.current_skill_ink()
      return self.skill_ink.get(attribute, 0)

    # derived fields
    def current_skill_ink(self):
      sk = self.skill_ink
      if self.finalized:
        return sk[SkillInk.CURRENT]
      return sk[SkillInk.PICK_UP] + sk[SkillInk.BUY] - sk[SkillInk.USE]




