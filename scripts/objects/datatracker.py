from enum import Enum, auto
from copy import copy

#
#
# Enums

class Character(Enum):
  """Enum representing characters."""
  RYU   = auto()
  REI   = auto()
  TEEPO = auto()
  NINA  = auto()
  MOMO  = auto()
  PECO  = auto()
  GARR  = auto()

class SkillInk(Enum):
  """Enum representing Skill Ink attributes."""
  PICK_UP = auto()
  BUY     = auto()
  USE     = auto()
  CURRENT = auto()

class Zenny(Enum):
  """Enum representing Zenny attributes."""
  PICK_UP     = auto()
  BOSS_DROP   = auto()
  ENEMY_DROP  = auto()
  SALES       = auto()
  BUY         = auto()
  CURRENT     = auto()

class Weapon(Enum):
  """Enum representing weapons."""
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
  """Add add a key/value pair to a dict.

  Args:
    d (dict of ?: int): A dictionary.
    k (?): A key.
    v (int): An int value.

  Raises:
    TypeError: If `v` cannot be converted to int.
    TypeError: If `d` is not subscriptable.

  """
  old_val = 0
  if k in d:
    old_val = d[k]
  d[k] = int(v) + old_val

def add_dicts(d1, d2):
  """Return a dict which is the sum of the given dicts.

  Args:
    d1 (dict of ?: int): The first dict.
    d2 (dict of ?: int): The second dict.

  Returns:
    A new dict whose value at k is d1[k] + d2[k].

  Raises:
    TypeError: If either argument cannot be converted to dict.

  """
  new_dict = dict(d1)
  other_dict = dict(d2)
  for k in other_dict:
    add_key_value_to_dict(new_dict, k, d2[k])
  return new_dict 

def absolute_value(arg):
  """Return a numerical value representing the argument.

  Args:
    arg (int or list of int): Pseudo-numerical input.

  Returns:
    The value `arg` if `arg` is int, or `sum(arg)` if arg is a summable.

  Raises:
    TypeError: If `arg` is not int or a summable list.

  """
  try: 
    return int(arg)
  except:
    pass

  try:
    return sum(list(arg))
  except:
    raise TypeError("Argument must be int or list of int.")

#
#
# DataTracker class.

class DataTracker:
  """Tracks some data for Breath Of Fire III.

  Tracks current party, party levels, Skill Ink and Zenny attributes, 
  and tracks weapon quantities for the weapons you can find before D'Lonzo.

  """

  #
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
  def __make_weapon_requirements():
    duplicates = [Weapon.DAGGER, Weapon.BALLOCK_KNIFE, Weapon.BENT_SWORD, Weapon.POINTED_STICK]
    return dict(map(lambda w: (w, 2 if w in duplicates else 1), list(Weapon)))
  WEAPON_REQUIREMENTS = __make_weapon_requirements()

  #
  #
  # Constructor

  def __init__(self):
    """Construct a DataTracker instance."""
    # TODO make fields private.
    self.entries = [DataTracker.Entry()]
    self.current_entry = self.entries[0]
    self.totals = []
    # Add starting character.
    self.gain_character(Character.RYU)

  #
  #
  # Interface methods

  #
  # Incrementing methods

  # Character methods

  def gain_character(self, character):
    """Add character to party.

    Args:
      character (Character): The character being gained by the party.

    Raises:
      TypeError: If character is not a Character.
      AssertionError: If character is already in the party.

    """
    self.__validate_character_for_add(character)
    self.current_entry.party.add(character)
    if character not in self.current_entry.party_levels:
      self.current_entry.party_levels[character] = self.STARTING_LEVELS[character]

  def lose_character(self, character):
    """Lose character from party.

    Args:
      character (Character): The character leaving the party.

    Raises:
      TypeError: If character is not a Character.
      KeyError: If character is not in the party.

    """
    self.__validate_character_for_modify(character)
    self.current_entry.party.remove(character)


  def level_up(self, character, levels=1):
    """Level up character.

    Args:
      character (Character): The character levelling up.
      levels (:obj:`int`, optional): The amount of levels gained. Defaults to 1.

    Raises:
      TypeError: If character is not a Character. 
      KeyError: If character is not in the party.   
      ValueError: If levels is nonpositive.  

    """
    self.__validate_character_for_modify(character)
    self.__validate_positive_input(levels, "Levels gained")
    pl = self.current_entry.party_levels
    add_key_value_to_dict(pl, character, levels)

  # Skill Ink methods

  def pick_up_skill_ink(self):
    """Add picked up Skill Ink to inventory."""
    sk = self.current_entry.skill_ink
    add_key_value_to_dict(sk, SkillInk.PICK_UP, 1)

  def buy_skill_ink(self, amt=1):
    """Add purchased Skill Ink to inventory.

    Args:
      amt (int): Amount of Skill Inks purchased. Defaults to 1.

    Raises:
      ValueError: If amt is nonpositive.

    """
    self.__validate_positive_input(amt, "Skill Ink amount")
    sk = self.current_entry.skill_ink
    add_key_value_to_dict(sk, SkillInk.BUY, amt)

  def use_skill_ink(self):
    """Take used Skill Ink out of inventory."""
    sk = self.current_entry.skill_ink
    add_key_value_to_dict(sk, SkillInk.USE, 1)

  # Zenny methods

  def pick_up_zenny(self, amt):
    """Add picked up Zenny to total.

    Args:
      amt (int): Amount of Zenny gained.

    Raises:
      ValueError: If amt is nonpositive.

    """
    self.__validate_positive_input(amt, "Picked up Zenny amount")
    self.current_entry.zenny[Zenny.PICK_UP].append(amt)

  def boss_drop_zenny(self, amt):
    """Add Zenny from Boss to total.

    Args:
      amt (int): Amount of Zenny gained.

    Raises:
      ValueError: If amt is nonpositive.

    """
    self.__validate_positive_input(amt, "Zenny dropped by Boss")
    self.current_entry.zenny[Zenny.BOSS_DROP].append(amt)

  def sell(self, amt):
    """Add Zenny from Sale to total.

    Args:
      amt (int): Amount of Zenny gained.

    Raises:
      ValueError: If amt is nonpositive.

    """
    self.__validate_positive_input(amt, "Zenny from sale")
    self.current_entry.zenny[Zenny.SALES].append(amt)

  def buy(self, amt):
    """Take Zenny from purchase off of total.

    Args:
      amt (int): Amount of Zenny lost.

    Raises:
      ValueError: If amt is nonpositive.

    """
    self.__validate_positive_input(amt, "Zenny spent")
    self.current_entry.zenny[Zenny.BUY].append(amt)

  def set_current_zenny(self, amt):
    """Set current Zenny total.

    Args:
      amt (int): The value to set as current.

    Raises:
      ValueError: If amt is nonnegative.

    """
    self.__validate_nonnegative_input(amt, "Current Zenny amount")
    self.current_entry.zenny[Zenny.CURRENT] = amt

  # Weapon methods

  def pick_up_weapon(self, weapon):
    """Add picked up weapon to inventory.

    Args:
      weapon (Weapon): The weapon picked up.

    Raises:
      TypeError: If weapon is not Weapon type.

    """
    self.__validate_weapon_for_add(weapon)
    add_key_value_to_dict(self.current_entry.weapons, weapon, 1) 

  def buy_weapon(self, weapon, cost):
    """Add purchased weapon to inventory.

    Args:
      weapon (Weapon): The weapon purchased.
      cost (int): The amount of money spent.

    Raises:
      TypeError: If weapon is not Weapon type.
      ValueError: If cost is nonpositive.

    """
    self.__validate_weapon_for_add(weapon)
    self.__validate_positive_input(cost, "Cost")
    self.pick_up_weapon(weapon)
    self.buy(cost)

  #
  # Getting methods

  def number_of_splits(self):
    """Return the number of splits so far."""
    return len(self.totals)

  def __get_previous_totals(self):
    """Return the entry containing the totals from the previous split."""
    if not self.totals:
      return DataTracker.Entry()
    else:
      return self.totals[self.number_of_splits() - 1]

  def get_name(self, split):
    """Return the name of a split.

    Args:
      split (int): Selects the split.

    Returns:
      The name of the specified split.

    Raises:
      IndexError: If split is negative or at least number_of_splits().

    """
    self.__validate_split_number(split)
    return self.totals[split].name

  def get_party(self, split=None):
    """Return the party.

    Args:
      split (:obj:`int`, optional): Selects the split. Defaults to None.
          If not specified, returns current party.

    Returns:
      The current party, or from a given split if specified.

    Raises:
      IndexError: If split is negative or at least number_of_splits().

    """
    if not split == None:
      self.__validate_split_number(split)
      return set(self.totals[split].party)
    return set(self.current_entry.party)

  def get_party_levels(self, split=None):
    """Return the party levels.

    Args:
      split (:obj:`int`, optional): Selects the split. Defaults to None.
          If not specified, returns current party levels.

    Returns:
      The current party levels, or from a given split if specified.

    Raises:
      IndexError: If split is negative or at least number_of_splits().

    """
    if not split == None:
      self.__validate_split_number(split)
      return dict(self.totals[split].party_levels)
    return add_dicts(
        self.__get_previous_totals().party_levels, 
        self.current_entry.party_levels)

  def get_weapons(self, split=None):
    """Return the weapons in inventory.

    Args:
      split (:obj:`int`, optional): Selects the split. Defaults to None.
          If not specified, returns current weapon quantities.

    Returns:
      The current weapon amounts, or from a given split if specified.

    Raises:
      IndexError: If split is negative or at least number_of_splits().

    """
    if not split == None:
      self.__validate_split_number(split)
      return dict(self.totals[split].weapons)
    return add_dicts(
        self.__get_previous_totals().weapons, 
        self.current_entry.weapons)

  def have_all_weapons(self):
    """Returns True if weapon requirements are met, false otherwise."""
    weapons = self.get_weapons()
    reqs = self.WEAPON_REQUIREMENTS
    finished = True
    for w in list(Weapon):
      finished = finished and reqs[w] <= weapons[w]
    return finished

  def get_gain(self, attribute, split):
    """Return the increase in an attribute during a given split.

    Args:
      attribute ("name" or Character or SkillInk or Zenny or Weapon): The
          attribute to retrieve data for.
      split (int): Selects the split to retrive data for.

    Returns:
      The amount gained for a given attribute during the specified split.

    Raises:
      IndexError: If split is negative or at least number_of_splits().
      KeyError: If attribute is not SkillInk or Zenny type.

    """ 
    self.__validate_attribute_type(attribute)
    self.__validate_split_number(split)
    return self.entries[split].get(attribute)

  def get_total(self, attribute, split=None):
    """Return the total of an attribute.

    Args:
      attribute ("name" or Character or SkillInk or Zenny or Weapon): The
          attribute to retrieve data for.
      split (:obj:`int`, optional): Selects the split. Defaults to -1.
          If not specified, returns current total.

    Returns:
      The total for a given attribute, or from a given split if specified.

    Raises:
      IndexError: If split is negative or at greater than number_of_splits().
      KeyError: If attribute is not SkillInk or Zenny type.

    """
    self.__validate_attribute_type(attribute)
    if (split == None) or (split == len(self.entries) - 1):
      gain = self.get_current(attribute)
      prev_total = self.__get_previous_totals().get(attribute)
      return absolute_value(gain) + absolute_value(prev_total)
    self.__validate_split_number(split)
    return self.totals[split].get(attribute)

  def get_current(self, attribute):
    """Return current value of an attribute.

    Args:
      attribute ("name" or Character or SkillInk or Zenny or Weapon): The
          attribute to retrieve data for.

    Returns:
      The current amount for a given attribute.

    Raises:
      KeyError: If attribute is not SkillInk or Zenny type.

    """
    self.__validate_attribute_type(attribute)
    return self.current_entry.get(attribute)

  #
  #
  # Split

  def split(self, name):
    """Split the DataTracker.

    Args:
      name (str): The name of the split.

    """
    # Finalize current entry
    self.current_entry.name = str(name)
    self.current_entry.finalize()
    # Compute totals
    previous_totals = self.__get_previous_totals()
    totals_entry = DataTracker.Entry.new_totals_entry(self.current_entry, previous_totals)
    self.totals.append(totals_entry)
    # Make new entry
    self.current_entry = DataTracker.Entry.new_current_entry(totals_entry)
    self.entries.append(self.current_entry)

  #
  #
  # Input validation

  def __validate_character_for_add(self, character):
    self.__validate_character_type(character)
    if character in self.current_entry.party:
      raise KeyError("Character already in party.")

  def __validate_character_for_modify(self, character):
    self.__validate_character_type(character)
    if character not in self.current_entry.party:
      raise KeyError("Character not in party.")

  def __validate_character_type(self, character):
    if not isinstance(character, Character):
      raise TypeError("Input must be Character type.")

  def __validate_positive_input(self, x, argname):
    if x < 1:
      raise ValueError(argname + " must be positive.")

  def __validate_nonnegative_input(self, x, argname):
    if x < 0:
      raise ValueError(argname + " must be nonnegative.")

  def __validate_weapon_for_add(self, weapon):
    if not isinstance(weapon, Weapon):
      raise TypeError("Input must be Weapon type.")

  def __validate_split_number(self, split):
    if split < 0 or split >= self.number_of_splits():
      raise IndexError("Split index must be nonnegative and less than the number of splits.")

  def __validate_attribute_type(self, attribute):
    if not isinstance(attribute, Zenny) and not isinstance(attribute, SkillInk):
      raise KeyError("Attribute must be Zenny or SkillInk type.")

  #
  #
  # Inner class DataTracker.Entry

  class Entry:
    """Stores relevant data for a split."""

    #
    #
    # Constructors

    def __init__(self):
      """Construct DataTracker.Entry instance."""
      self.finalized = False
      self.name = None
      self.party = set()
      self.party_levels = dict()
      self.skill_ink = dict(map(lambda a : (a, 0), list(SkillInk)))
      self.zenny = dict(map(lambda a : (a, []), list(Zenny)))
      self.zenny[Zenny.CURRENT] = 0
      self.zenny[Zenny.ENEMY_DROP] = 0
      self.weapons = dict(map(lambda a : (a, 0), list(Weapon)))

    def new_totals_entry(current_entry, previous_totals):
      """Compute the new totals from the current entry and the previous totals."""
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
      # set zenny
      gain_totals = dict()
      for k in current_entry.zenny:
        gain_totals[k] = current_entry.zenny[k] if k in [Zenny.CURRENT, Zenny.ENEMY_DROP]\
                                        else sum(current_entry.zenny[k])
      e.zenny = gain_totals
      # set weapons
      e.weapons = add_dicts(current_entry.weapons, previous_totals.weapons)
      # Finalize
      e.finalize()
      return e

    def new_current_entry(totals_entry):
      """Construct a new current entry from previous totals."""
      e = DataTracker.Entry()
      e.party = set(totals_entry.party)
      return e

    #
    #
    # Finalization

    def finalize(self):
      """Compute derived fields and finalize."""
      self.skill_ink[SkillInk.CURRENT] = self.__current_skill_ink()
      self.zenny[Zenny.ENEMY_DROP] = self.__enemy_drop()
      self.finalized = True

    #
    #
    # Getting methods

    def get(self, attribute):
      """Return the value of an attribute."""
      if isinstance(attribute, SkillInk):
        if attribute == SkillInk.CURRENT:
          return self.__current_skill_ink()
        return self.skill_ink.get(attribute, 0)
      if isinstance(attribute, Zenny):
        if attribute == Zenny.ENEMY_DROP:
          return self.__enemy_drop()
        return copy(self.zenny[attribute])

    #
    #
    # Derived fields

    def __current_skill_ink(self):
      sk = self.skill_ink
      if self.finalized:
        return sk[SkillInk.CURRENT]
      return sk[SkillInk.PICK_UP] + sk[SkillInk.BUY] - sk[SkillInk.USE]

    def __zenny_subtotal(self):
      '''Current Zenny and enemy urops can be computed in terms of one another
      by using this subtotal.
      '''
      z = self.zenny
      return absolute_value(z[Zenny.PICK_UP]) + absolute_value(z[Zenny.BOSS_DROP]) \
          + absolute_value(z[Zenny.SALES]) - absolute_value(z[Zenny.BUY])

    def __enemy_drop(self):
      z = self.zenny
      if self.finalized:
        return z[Zenny.ENEMY_DROP]
      return z[Zenny.CURRENT] - self.__zenny_subtotal()
