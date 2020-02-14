from enum import Enum, auto


class Character(Enum):
  RYU   = auto()
  REI   = auto()
  TEEPO = auto()
  NINA  = auto()
  MOMO  = auto()
  PECO  = auto()
  GARR  = auto()

STARTING_LEVELS = {
  Character.RYU:    1,
  Character.REI:    5,
  Character.TEEPO:  1,
  Character.NINA:   5,
  Character.MOMO:   10,
  Character.PECO:   1,
  Character.GARR:   13,
}


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


class DataTracker:

  def __init__(self):
    pass