from datatracker import *

class DataPrinter():
  '''Prints a DataTracker's data.

  Takes a structure containing strings representing data from a DataTracker
  (specificaly, the output of DataTracker.get_strings()) and produces a readable
  string output.

  '''
   
  def __init__(self, name, strings, line_width=60):
    '''A helper object for printing a DataTracker.

    Args:
      name (str): The name of the DataTracker instance.
      strings (custom structure): The output of DataTracker.get_strings().
      line_width (int, optional): The width of any line.

    '''
    self.name = name
    self.strings = strings
    self.line_width = line_width

  def print(self):
    '''Returns a string representing an entire DataTracker.'''
    s = self._make_header()
    for i in range(0, len(self.strings)):
      s += self.print_entry(i)
    return s

  def _make_header(self):
    title = "Data for " + self.name
    padding = ' '
    line_width = len(title) + 2 * len(padding) + len('||||||||')
    header = (line_width - 2) * '='             + '||\n' + \
            '||'    + (line_width - 6) * '='    + '||||\n' + \
            '||||'  + padding + title + padding + '||||\n' + \
            '||||'  + (line_width - 6) * '='    + '||\n' + \
            '||'    + (line_width - 2) * '='    + '\n' + \
            '\n'
    return header

  def print_entry(self, i):
    '''Returns a string representing a single entry.'''
    if i < 0 or i >= len(self.strings):
      raise IndexError("Split index must be nonnegative and less than the number of splits.")
    s = DataPrinter._make_entry_header(self.strings[i]['name'])
    s += self._print_characters(i) + '\n'
    s += self._print_zenny(i) + '\n'
    s += self._print_skill_ink(i) + '\n'
    s += self._print_weapon(i)
    return s + '\n\n'

  def _make_entry_header(s):
    s = s + '\n' + '-' * len(s)
    return s + '\n'

  #
  #
  # Character and Weapon printing.

  def _print_characters(self, i):
    s = ''
    w = 0
    strings = self.strings[i]['party_levels']
    for c in list(Character):
      if c in strings['total']:
        suf = c.name + ': ' + strings['total'][c]
        s, w = self._add_to_lined_string(s, w, suf)
    return s + '\n'

  def _print_weapon(self, i):
    s = 'Weapon:\n'
    w = 0
    strings_dict = self.strings[i]
    amts = strings_dict['weapons']['total']
    reqs = strings_dict['weapon_requirements']
    printed = False
    for c in list(Weapon):
      if int(amts[c]) >= int(reqs[c]):
        continue
      suf = c.name + ': ' + amts[c] + '/' + reqs[c]
      s, w = self._add_to_lined_string(s, w, suf)
      printed = True
    if not printed:
      s += 'Completed!'
    return s + '\n'

  def _add_to_lined_string(self, s, used, suf):
    suf_with_space =  ' ' * 5  + suf
    w = used + len(suf_with_space)
    if used == 0:
      s += suf
      w = len(suf)
    elif w <= self.line_width:
      s += suf_with_space
    else:
      s += '\n' + suf
      w = len(suf)
    return s, w

  #
  #
  # Zenny and SkillInk printing

  def _print_zenny(self, i):
    return self._print_enum(i, Zenny)

  def _print_skill_ink(self, i):
    return self._print_enum(i, SkillInk)

  def _print_enum(self, i, enum):
    if enum == Zenny:
      s, key = 'Zenny:\n', 'zenny'
    elif enum == SkillInk:
      s, key = 'Skill Ink:\n', 'skill_ink'
    else:
      raise ValueError("enum must be Zenny or SkillInk")
    strings = self.strings[i][key]
    val1s, val2s, max_val2_length = self._pre_process(strings, enum)
    for att in list(enum):
      s += self._print_line(att.name, val1s[att], val2s[att], max_val2_length)
    return s

  def _pre_process(self, strings, enum):
    max_val2_length = 0
    val1s, val2s = dict(), dict()
    for att in list(enum):
      v1, v2 = '', ''
      if att == enum.CURRENT:
        v1 = strings['total'][att]
        v2 = strings['gain'][att]
        if int(v2) >= 0: v2 = '+' + v2
        v2 = ' (' + v2 + ')'
      else:
        v1 = strings['gain'][att]
        v2 = strings['total'][att]
        v2 = ' (/' + v2 + ')'
      val1s[att], val2s[att] = v1, v2
      if len(v2) > max_val2_length: max_val2_length = len(v2)
    return val1s, val2s, max_val2_length

  def _print_line(self, name, val1, val2, max_val2_length):
    title = name + ':'
    val2 = (max_val2_length - len(val2)) * ' ' + val2
    dots = (self.line_width - len(name) - len(val1) - len(val2)) * '.'
    return name + dots + val1 + val2 + '\n'
