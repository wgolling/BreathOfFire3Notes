from datatracker import *

class DataPrinter():
   
  def __init__(self, data_tracker):
    self.dt = data_tracker
    self.line_width = 60

  def print(self):
    s = self.__make_header()
    for i in range(0, self.dt.number_of_splits()):
      s += self.print_entry(i)
    return s

  def __make_header(self):
    return ''

  def print_entry(self, i):
    if i < 0 or i >= self.dt.number_of_splits():
      raise IndexError("Split index must be nonnegative and less than the number of splits.")
    s = DataPrinter.__make_entry_header(self.dt.get_name(i))
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
    for c in list(Character):
      if c in self.dt.get_party(split=i):
        suf = c.name + ': ' + str(self.dt.get_party_levels(split=i)[c])
        s, w = self.__add_to_lined_string(s, w, suf)
    return s + '\n'

  def __print_weapon(self, i):
    s = 'Weapon:\n'
    w = 0
    weapons = self.dt.get_weapons(split=i)
    for c in list(Weapon):
      suf = c.name + ': ' + str(weapons[c]) + '/' + str(self.dt.WEAPON_REQUIREMENTS[c])
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

  def __print_list(l):
    try:
      int(l)
    except TypeError:
      pass
    else:
      return str(l)
    if len(l) == 0:
      return '0'
    if len(l) == 1:
      return str(l[0])
    return '+'.join(str(i) for i in l) + ' = ' + str(sum(l))

  def __print_line(self, att, gain, total):
    str_gain = DataPrinter.__print_list(gain)
    padding = self.line_width - len(att) - len(str_gain) - len(str(total)) - 3
    return att + ':' + padding * '.' + str_gain + '(' + str(total) + ')' + '\n'

  def __print_zenny(self, i):
    s = 'Zenny:\n'
    for z in list(Zenny):
      s += self.__print_line(z.name, self.dt.get_gain(z, i), self.dt.get_total(z, split=i))
    return s

  def __print_skill_ink(self, i):
    s = 'Skill Ink:\n'
    for att in list(SkillInk):
      s += self.__print_line(att.name, self.dt.get_gain(att, i), self.dt.get_total(att, split=i))
    return s
