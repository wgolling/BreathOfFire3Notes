from enum import Enum, auto

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
    self.gain_character(Character.RYU)

  #
  #
  # Interface methods

  #
  # Incrementing methods

  # Character
  def gain_character(self, character):
    pl = self.current_entry.party_levels
    assert(not character in pl)
    pl[character] = self.STARTING_LEVELS[character]

  def level_up(self, character, levels=1):
    pl = self.current_entry.party_levels
    assert(character in pl)
    pl[character] = pl[character] + levels

  # Skill Ink
  def pick_up_skill_ink(self):
    pass

  def buy_skill_ink(self):
    pass

  def use_skill_ink(self):
    pass

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
    self.current_entry.finalized = True
    # Make new entry
    self.current_entry = DataTracker.Entry()
    self.entries.append(self.current_entry)

  #  
  # Getting methods

  def get_party_levels(self, split=None):
    if not split:
      split = len(self.entries) - 1
    return dict(self.entries[split].party_levels)

  def get_gain(self, attribute, total):
    pass

  def get_total(self, attribute, split):
    pass

  def get_current(self, attribute):
    pass

  # General get method
  def get(self, attribute, split):
    if attribute == "name":
      return self.entries[split].name




  class Entry:
    def __init__(self):
      self.finalized = False
      self.name = None
      self.party_levels = dict()

    def finalize(self):
      self.finalized = True


