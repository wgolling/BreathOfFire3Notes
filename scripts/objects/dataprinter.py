class DataPrinter():
   
  def __init__(self, data_tracker):
    self.dt = data_tracker

  def print_entry(self, i):
    if i < 0 or i >= self.dt.number_of_splits():
      raise IndexError("Split index must be nonnegative and less than the number of splits.")
    return "Entry " + str(i) + "\n"


  def print(self):
    s = ''
    for i in range(0, self.dt.number_of_splits()):
      s += self.print_entry(i)
    return s