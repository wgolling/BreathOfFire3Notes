from datatracker import *

class DataPrinter():
   
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
    s = self.__make_header()
    for i in range(0, len(self.strings)):
      s += self.print_entry(i)
    return s

  def __make_header(self):
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
    s = DataPrinter.__make_entry_header(self.strings[i]['name'])
    s += self.__print_characters(i) + '\n'
    s += self.__print_zenny(i) + '\n'
    s += self.__print_skill_ink(i) + '\n'
    s += self.__print_weapon(i)
    return s + '\n\n'

  def __make_entry_header(s):
    s = s + '\n' + '-' * len(s)
    return s + '\n'

  #
  #
  # Character and Weapon printing.

  def __print_characters(self, i):
    s = ''
    w = 0
    strings = self.strings[i]['party_levels']
    for c in list(Character):
      if c in strings['total']:
        suf = c.name + ': ' + strings['total'][c]
        s, w = self.__add_to_lined_string(s, w, suf)
    return s + '\n'

  def __print_weapon(self, i):
    s = 'Weapon:\n'
    w = 0
    strings_dict = self.strings[i]
    strings = strings_dict['weapons']['total']
    for c in list(Weapon):
      suf = c.name + ': ' + strings[c] + '/' + strings_dict['weapon_requirements'][c]
      s, w = self.__add_to_lined_string(s, w, suf)
    return s + '\n'

  def __add_to_lined_string(self, s, used, suf):
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

  def __print_line(self, att, gain, total):
    padding = self.line_width - len(att) - len(gain) - len(total) - 3
    return att + ':' + padding * '.' + gain + '(' + total + ')' + '\n'

  def __print_zenny(self, i):
    s = 'Zenny:\n'
    strings = self.strings[i]['zenny']
    for z in list(Zenny):
      s += self.__print_line(z.name, strings['gain'][z], strings['total'][z])
    return s

  def __print_skill_ink(self, i):
    s = 'Skill Ink:\n'
    strings = self.strings[i]['skill_ink']
    for att in list(SkillInk):
      s += self.__print_line(att.name, strings['gain'][att], strings['total'][att])
    return s
