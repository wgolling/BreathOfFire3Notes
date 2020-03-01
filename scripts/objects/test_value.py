from unittest import TestCase

from value import *

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

  def test_exceptions(self):
    # non-iterable initial value
    with self.assertRaises(TypeError):
      ListValue(initial_value=True)
    # initial value is iterable but has entries that don't convert to int
    with self.assertRaises(ValueError):
      ListValue(initial_value=['buh', 'foo'])
    with self.assertRaises(ValueError):
      ListValue().add("buh")
