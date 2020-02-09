import newrun
from newrun import RunFolderMaker

from pathlib import Path

import unittest

class TestRunFolderMakerConstructor(unittest.TestCase):
  def setUp(self):
    self.scripts_folder = Path(__file__).absolute().parents[1]
    self.test_folder = self.scripts_folder / 'objects/test'

  #
  # Testing constructor failures
  #

  # Invalid base_path
  @unittest.expectedFailure
  def test_base_path_not_valid(self):
    try:
      RunFolderMaker(7)
    except Exception as e:
      print(e)
      raise
  @unittest.expectedFailure
  def test_base_path_not_found(self):
    try:
      RunFolderMaker(self.test_folder / 'foo')
    except Exception as e:
      print(e)
      raise
  @unittest.expectedFailure
  def test_base_path_not_a_dir(self):
    try:
      RunFolderMaker(self.test_folder / 'dummy.txt')
    except Exception as e:
      print(e)
      raise

  # Invalid template_path
  @unittest.expectedFailure
  def test_template_path_not_valid(self):
    try:
      RunFolderMaker(self.test_folder, template_path=7)
    except Exception as e:
      print(e)
      raise
  @unittest.expectedFailure
  def test_template_path_not_found(self):
    try:
      RunFolderMaker(self.test_folder, template_path=self.test_folder / 'foo')
    except Exception as e:
      print(e)
      raise
  @unittest.expectedFailure
  def test_template_path_not_a_dir(self):
    try:
      RunFolderMaker(self.test_folder, template_path=self.test_folder / 'dummy.txt')
    except Exception as e:
      print(e)
      raise

  # Valid input
  def test_valid_params(self):
    assert(RunFolderMaker(self.test_folder, template_path=self.scripts_folder / 'template'))


if __name__ == "__main__":
  unittest.main()



