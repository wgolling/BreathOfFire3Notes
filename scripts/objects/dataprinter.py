from datatracker import *

class DataPrinter():
   
  def __init__(self, data_tracker):
    self.dt = data_tracker
    self.line_width = 60

  def print_entry(self, i):
    if i < 0 or i >= self.dt.number_of_splits():
      raise IndexError("Split index must be nonnegative and less than the number of splits.")
    s = DataPrinter.__make_header(self.dt.get_name(i))
    s += self.__print_characters(i)
    s += self.__print_zenny(i)
    s += self.__print_skill_ink(i)
    s += self.__print_weapon(i)
    return s + "\n"

  def __make_header(s):
    s = s + '\n' + '-' * len(s)
    return s + '\n'

  def __print_characters(self, i):
    s = ''
    w = 0
    for c in list(Character):
      if c in self.dt.get_party(split=i):
        suf = c.name + ': ' + str(self.dt.get_party_levels(split=i)[c]) + ' ' * 5
        w += len(suf)
        if w > self.line_width:
          s += '\n'
          w = len(suf)
        s += suf
    return s + '\n'


  def __print_zenny(self, i):
    return ''

  def __print_skill_ink(self, i):
    return ''

  def __print_weapon(self, i):
    return ''


  def print(self):
    s = ''
    for i in range(0, self.dt.number_of_splits()):
      s += self.print_entry(i)
    return s
    