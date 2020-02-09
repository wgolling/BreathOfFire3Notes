import newrun
from newrun import *

from pathlib import Path
import unittest


class TestHelperFunctions(unittest.TestCase):

  def test_last_element(self):
    test_list = None
    assert(last_element(test_list) == None)
    test_list = []
    assert(last_element(test_list) == None)
    test_list = [1, 2, 3, "foo"]
    assert(last_element(test_list) == 'foo')

  def test_get_largest_int(self):
    test_list = []
    assert(get_largest_int(test_list) == None)
    test_list = ['one', 'two', 'three']
    assert(get_largest_int(test_list) == None)
    test_list.append(7)
    assert(get_largest_int(test_list) == 7)
    test_list.append('8')
    assert(get_largest_int(test_list) == 8)

  @unittest.expectedFailure
  def test_get_largest_int_bad_input(self):
    test_list = None
    get_largest_int(test_list)


class TestRunFolderMakerConstructor(unittest.TestCase):

  def setUp(self):
    self.scripts_folder = Path(__file__).absolute().parents[1]
    self.test_folder = self.scripts_folder / 'objects/test'

  #
  # Testing constructor failures
  #

  # Invalid base_path
  def bad_input_with_defaults(self, base_path):
    try:
      RunFolderMaker(base_path)
    except Exception as e:
      print(e)
      raise

  @unittest.expectedFailure
  def test_base_path_not_valid(self):
    self.bad_input_with_defaults(7)

  @unittest.expectedFailure
  def test_base_path_not_found(self):
    self.bad_input_with_defaults(self.test_folder / 'foo')

  @unittest.expectedFailure
  def test_base_path_not_a_dir(self):
    self.bad_input_with_defaults(self.test_folder / 'dummy.txt')

  # Invalid template_path
  def bad_input_template_path(self, base_path, template_path):
    try:
      RunFolderMaker(base_path, template_path=template_path)
    except Exception as e:
      print(e)
      raise
      
  @unittest.expectedFailure
  def test_template_path_not_valid(self):
    self.bad_input_template_path(self.test_folder, 7)

  @unittest.expectedFailure
  def test_template_path_not_found(self):
    self.bad_input_template_path(self.test_folder, template_path=self.test_folder / 'foo')

  @unittest.expectedFailure
  def test_template_path_not_a_dir(self):
    self.bad_input_template_path(self.test_folder, template_path=self.test_folder / 'dummy.txt')

  #
  # Testing constructor success
  #
  def test_valid_params(self):
    assert(RunFolderMaker(self.test_folder, template_path=self.scripts_folder / 'template'))


if __name__ == "__main__":
  unittest.main()



