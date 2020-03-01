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


class ListValue:
  '''A value class where the value is a represented by a list of ints.'''

  def __init__(self, initial_value=[]):
    '''Constructs a ListValue instance.

    Args:
      initial_value (list of int, optional): Initial value. Defaults to empty list.

    '''
    self.__value = [int(x) for x in initial_value]

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
