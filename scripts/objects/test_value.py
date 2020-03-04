from unittest import TestCase

from value import *


class TestStaticMethods(TestCase):

  def setUp(self):
    self.d = {
      'a': BasicValue(),
      'b': BasicValue(5),
      'c': ListValue([5]),
    }

  def test_add_key_int_to_dict(self):
    add_key_int_to_dict(self.d, 'a', 2)
    assert(self.d['a'].value() == 2)
    assert(self.d['a'].raw() == 2)
    add_key_int_to_dict(self.d, 'c', 2)
    assert(self.d['c'].value() == 7)
    assert(self.d['c'].raw() == [5,2])
    with self.assertRaises(KeyError):
      add_key_int_to_dict(self.d, 'buh', 2)

  def test_add_key_value_to_dict(self):
    # add to basic value
    add_key_value_to_dict(self.d, 'a', BasicValue(2))
    assert(self.d['a'].value() == 2)
    assert(self.d['a'].raw() == 2)
    add_key_value_to_dict(self.d, 'a', ListValue([2]))
    assert(self.d['a'].value() == 4)
    assert(self.d['a'].raw() == 4)
    # add to list value
    add_key_value_to_dict(self.d, 'c', BasicValue(2))
    assert(self.d['c'].value() == 7)
    assert(self.d['c'].raw() == [5, 2])
    add_key_value_to_dict(self.d, 'c', ListValue([2]))
    assert(self.d['c'].value() == 9)
    assert(self.d['c'].raw() == [5, 2, 2])
    # missing key basic
    add_key_value_to_dict(self.d, 'missing_basic', BasicValue(2))
    assert(self.d['missing_basic'].value() == 2)
    # missing key list
    add_key_value_to_dict(self.d, 'missing_list', ListValue([2, 7]))
    assert(self.d['missing_list'].value() == 9)
    assert(self.d['missing_list'].raw() == [2, 7])

  def test_copy_dict(self):
    d2 = copy_dict(self.d)
    assert(not d2 is self.d)
    assert(d2 == self.d)
    add_key_int_to_dict(d2, 'a', 10)
    assert(d2 != self.d)

  def test_int_dict(self):
    d2 = int_dict(self.d)
    assert(not d2 is self.d)
    assert(d2['a'] == 0)
    assert(d2['b'] == 5)
    assert(d2['c'] == 5)

  def test_raw_dict(self):
    d2 = raw_dict(self.d)
    assert(not d2 is self.d)
    assert(d2['a'] == 0)
    assert(d2['b'] == 5)
    assert(d2['c'] == [5])

  def test_string_dict(self):
    d2 = string_dict(self.d)
    assert(not d2 is self.d)
    assert(d2['a'] == '0')
    assert(d2['b'] == '5')
    assert(d2['c'] == '5')
    self.d['c'].add(2)
    assert(d2['c'] == '5')
    d2 = string_dict(self.d)
    assert(d2['c'] == '5+2=7')

  def test_add_dicts(self):
    d2 = {
      'a': ListValue([1,2,3]),
      'c': ListValue([5,2]),
      'e': ListValue([2,3]),
    }
    d3 = add_dicts(self.d, d2)
    expected_sum = {
      'a': BasicValue(6),
      'b': BasicValue(5),
      'c': ListValue([5, 7]),
      'e': ListValue([2,3]),
    }
    assert(d3 == expected_sum)
    d4 = add_dicts(d2, self.d)
    expected_sum = {
      'a': ListValue([1,2,3,0]),
      'b': BasicValue(5),
      'c': ListValue([5, 2, 5]),
      'e': ListValue([2,3]),
    }
    assert(d4 == expected_sum)



class TestBasicValue(TestCase):

  def test(self):
    v = BasicValue()
    assert(v.value() == 0)
    assert(v.value() == v.raw())
    assert(v.print() == '0')
    v.add(5)
    assert(v.value() == 5)
    assert(v.value() == v.raw())
    assert(v.print() == '5')
    v.add(-10)
    assert(v.value() == -5)
    assert(v.value() == v.raw())
    assert(v.print() == '-5')
    assert(v == BasicValue(-5))
    assert(v == v.clone())

  def test_exceptions(self):
    with self.assertRaises(ValueError):
      BasicValue(initial_value='buh')
    with self.assertRaises(ValueError):
      BasicValue().add("buh")


class TestListValue(TestCase):

  def test(self):
    v = ListValue()
    assert(v.value() == 0)
    assert(v.raw() == [])
    assert(v.print() == '0')
    v.add(5)
    assert(v.value() == 5)
    assert(v.raw() == [5])
    assert(v.print() == '5')
    v.add(-10)
    assert(v.value() == -5)
    assert(v.raw() == [5, -10])
    assert(v.print() == '5-10=-5')
    assert(v == ListValue([5, -10]))
    assert(v == v.clone())

  def test_exceptions(self):
    # non-iterable initial value
    with self.assertRaises(TypeError):
      ListValue(initial_value=True)
    # initial value is iterable but has entries that don't convert to int
    with self.assertRaises(ValueError):
      ListValue(initial_value=['buh', 'foo'])
    with self.assertRaises(ValueError):
      ListValue().add("buh")
