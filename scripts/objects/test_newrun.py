import newrun
from newrun import *

from pathlib import Path
from shutil import rmtree
import unittest

SCRIPTS_FOLDER = Path(__file__).absolute().parents[1]
TEST_FOLDER = SCRIPTS_FOLDER / 'objects/test'

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

  #
  # Testing constructor failures
  #

  # Helper function for bad input.
  def bad_input(self, base_path, template_path=None):
    try:
      if template_path:
        RunFolderMaker(base_path, template_path=template_path)
      else:
        RunFolderMaker(base_path)
    except Exception as e:
      print(e)
      raise

  # testing bad base_path
  @unittest.expectedFailure
  def test_base_path_not_valid(self):
    self.bad_input(7)

  @unittest.expectedFailure
  def test_base_path_not_found(self):
    self.bad_input(TEST_FOLDER / 'foo')

  @unittest.expectedFailure
  def test_base_path_not_a_dir(self):
    self.bad_input(TEST_FOLDER / 'dummy.txt')

  # testing bad template_path
  @unittest.expectedFailure
  def test_template_path_not_valid(self):
    self.bad_input(TEST_FOLDER, template_path=7)

  @unittest.expectedFailure
  def test_template_path_not_found(self):
    self.bad_input(TEST_FOLDER, template_path=TEST_FOLDER / 'foo')

  @unittest.expectedFailure
  def test_template_path_not_a_dir(self):
    self.bad_input(TEST_FOLDER, template_path=TEST_FOLDER / 'dummy.txt')

  #
  # Testing constructor success
  #

  def test_valid_params(self):
    assert(RunFolderMaker(TEST_FOLDER))
    assert(RunFolderMaker(TEST_FOLDER, template_path=TEST_FOLDER / 'scripts'))


class TestFolderMaker(unittest.TestCase):

  # Make sure test folder is clean before and after running folder creation tests.
  def setUp(self):
    TestFolderMaker.delete_test_folders()

  def tearDown(self):
    TestFolderMaker.delete_test_folders()

  def get_test_run_folders():
    return TEST_FOLDER.glob('test*')

  def delete_test_folders():
    test_folders = TestFolderMaker.get_test_run_folders()
    # print("Test folders: ")
    for f in test_folders:
      # print(f)
      try:
       rmtree(f)
      except OSError:
        raise


  def test_setup_folder(self):
    rfm = RunFolderMaker(TEST_FOLDER, prefix='test')
    rfm.setup_folder()
    run_name = 'test1'
    new_folder = TEST_FOLDER / run_name
    assert(new_folder.exists())
    path_prefix = str(new_folder / run_name)
    testa_path = Path(path_prefix + '_testa.txt')
    assert(testa_path.exists())
    with testa_path.open() as f:
      assert(f.readline() == 'testa')
    testb_path = Path(path_prefix + '_testb.txt')
    assert(testb_path.exists())
    with testb_path.open() as f:
      assert(f.readline() == 'testb')
    test_notes_path = Path(path_prefix + '_notes.txt')
    assert(test_notes_path.exists())
    with test_notes_path.open() as f:
      line = f.readline()
      assert(line == '===============||\n')

    # make second run
    with test_notes_path.open('a') as f:
      f.write('*NEXT TIME do this')
    rfm.setup_folder()
    test_notes_path_2 = TEST_FOLDER / 'test2/test2_notes.txt'
    with test_notes_path_2.open() as f:
      line = f.readline()
      while line and not line.startswith('*THIS'):
        line = f.readline()
      assert(line == '*THIS TIME do this')


if __name__ == "__main__":
  unittest.main()



