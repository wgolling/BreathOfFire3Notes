from enum import Enum, auto


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

  STARTING_LEVELS = {
    Character.RYU:    1,
    Character.REI:    5,
    Character.TEEPO:  1,
    Character.NINA:   5,
    Character.MOMO:   10,
    Character.PECO:   1,
    Character.GARR:   13,
  }

  def make_weapon_requirements():
    duplicates = [Weapon.DAGGER, Weapon.BALLOCK_KNIFE, Weapon.BENT_SWORD, Weapon.POINTED_STICK]
    reqs = dict()
    for w in Weapon:
      reqs[w] = 2 if w in duplicates else 1
    return reqs
  WEAPON_REQUIREMENTS = make_weapon_requirements()

  #
  #
  # Constructor

  def __init__(self):
    pass

  #
  #
  # Interface methods

  #
  # Incrementing methods

  # Character
  def gain_character(character):
    pass

  def level_up(character):
    pass

  # Skill Ink
  def pick_up_skill_ink():
    pass

  def buy_skill_ink():
    pass

  def use_skill_ink():
    pass

  # Zenny
  def pick_up_zenny(amt):
    pass

  def boss_drop_zenny(amt):
    pass

  def sell(item, amt):
    pass

  def set_current_zenny(amt):
    pass

  # Weapon
  def get_weapon(weapon):
    pass 

  # Split
  def split(name):
    pass

  #  
  # Getting methods

  # General get method
  def get(attribute, split):
    pass




