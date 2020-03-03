def add_key_int_to_dict(d, k, v):
  '''Adds a (key, int) pair to a dict of Values.

  Assumes k is a key in d. Mutates d.

  Args:
    d (dict ?: Value): A dictionary whose values respond to .add(int) and .clone().
    k (?): An arbitrary key (must be hashable).
    v (int): The int to add to the value

  Raises:
    KeyError: If k is not in d.

  '''
  d[k].add(v)

def add_key_value_to_dict(d, k, v):
  '''Adds a (key, Value) pair to a dict of Values.

  Mutates d.

  Args:
    d (dict ?: Value): A dictionary whose values respond to .add(int) and .clone().
    k (?): An arbitrary key (must be hashable).
    v (Value): The Value object to add to the value in the d.

  '''
  if k in d:
    d[k].add(v.value())
  else:
    d[k] = v.clone()

def copy_dict(d):
  '''Copies a dict of cloneable Values.'''
  d2 = dict()
  for k in d:
    d2[k] = d[k].clone()
  return d2

def add_dicts(d1, d2):
  '''Adds two dicts of Values together.
  
  Makes a copy of the first dict, and adds the values from the second dict.

  '''
  new_dict = copy_dict(d1)
  for k in d2:
    add_key_value_to_dict(new_dict, k, d2[k])
  return new_dict



class BasicValue:
  '''A basic value class. The value is represented by an int.'''

  def __init__(self, initial_value=0):
    '''Constructs a BasicValue instance.

    Args:
      initial_value (list of int, optional): Initial value. Defaults to 0.

    Raises:
      ValueError: If initial_value is not convertible to int.

    '''
    self.__value = int(initial_value)

  def __eq__(self, other):
    if isinstance(other, BasicValue):
      return self.__value == other.__value
    return false

  def print(self):
    '''Prints value.

    Returns:
      The string version of the int value.

    '''
    return str(self.__value)

  def raw(self):
    '''Returns the raw value.

    Returns:
      The int value. This function is the same as BasicValue.value().

    '''
    return self.value()

  def value(self):
    '''Returns int value.

    Returns:
      The int value.  This function is the same as BasicValue.raw().

    '''
    return self.__value

  def add(self, x):
    '''Adds an int to the value.

    Args:
      x (int): The int being added.

    Raises:
      ValueError: If x is not convertible to int.

    '''
    self.__value += int(x)

  def clone(self):
    return BasicValue(initial_value=self.__value)


class ListValue:
  '''A value class where the value is a represented by a list of ints.'''

  def __init__(self, initial_value=[]):
    '''Constructs a ListValue instance.

    Args:
      initial_value (list of int, optional): Initial value. Defaults to empty list.

    '''
    self.__value = [int(x) for x in initial_value]

  def __eq__(self, other):
    if isinstance(other, ListValue):
      return self.__value == other.__value
    return false

  def print(self):
    '''Prints value.

    Returns:
      The string version of the list value. Returns '0' if the list is empty and
        the unique element if the list has length 1. Otherwise, returns a 
        summation expression over the elements of the list, followed by an equals
        sign and the sum of the list.

    '''
    if len(self.__value) == 0:
      return '0'
    if len(self.__value) == 1:
      return str(self.__value[0])
    ints = list(self.__value)
    s = str(ints.pop(0))
    for i in ints:
      (op, n) = ('+', str(i)) if i >= 0 else ('-', str(-i))
      s += op + n
    s += '=' + str(self.value())
    return s

  def value(self):
    '''Returns int value.

    Returns:
      The sum of the elements in the list.

    '''
    return sum(self.__value)

  def raw(self):
    '''Returns the raw value.

    Returns:
      A copy of the list value.

    '''
    return list(self.__value)
    
  def add(self, x):
    '''Adds an int to the value.

    Args:
      x (int): The int value to be added.

    Raises:
      ValueError: If x is not convertible to int.

    '''
    self.__value.append(int(x))

  def clone(self):
    return ListValue(initial_value=self.__value)
