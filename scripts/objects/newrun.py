from pathlib import Path
from shutil import copyfile
import os

#
# Helper functions for lists.
#

def last_element(lst):
  '''
  Returns the last element of a list, or None if it is empty.
  '''
  if not lst:
    return None
  return lst[-1]

def get_largest_int(obj_list):
  '''
  Tries to convert the elements of obj_list to ints, and retuns the largest.
  Returns None if obj_list doesn't contain anything int-able.
  '''
  max_int = None
  for x in obj_list:
    try:
      int_x = int(x)
    except ValueError:
      continue 

    if (not max_int) or (int_x and int_x > max_int):
      max_int = int_x
  return max_int


#
# Helper class for setting up a new run folder.
#

class RunFolderMaker:
  '''
  Constructor assumes base_path and template_path are pathlib objects.
  In particular it assumes they have exists() and is_dir() methods which
  both return true.
  The constructor also assumes prefix is a string
  '''
  def __init__(self, base_path, prefix="run", template_path=None):
    # TODO: make sure input doesn't have any special characters
    #       maybe this is handled already by checking exists()?

    # initialize and validate self.base_path
    self.base_path = None
    try:
      self.base_path = Path(base_path)
    except TypeError:
      raise ValueError("base_path must be convertible to pathlib.Path")
    if not self.base_path.exists():
      raise ValueError("base_path does not exist")
    if not self.base_path.is_dir():
      raise ValueError("base_path must be a directory")

    # initialize self.prefix (str(o) will never throw an exception)
    self.prefix = str(prefix)  

    # initialize and validate self.template_path and self.default_template
    self.template_path = None
    self.default_template = True
    if template_path:
      self.default_template = False
      try:
        self.template_path = Path(template_path)
      except TypeError:
        raise ValueError("template_path must be convertible to pathlib.Path")
    else:
      self.template_path = base_path / "scripts/template"
    if not self.template_path.exists():
      raise ValueError("template_path does not exist")
    if not self.template_path.is_dir():
      raise ValueError("template_path must be a directory")

 
  def setup_folder(self, copy_suffix=None):
    '''
    Creates a new folder (with template) in self.base_path with prefix self.prefix.
    If no template was specified in the constructor, uses the default template setup.
    If any folders exist with integer suffixes the new suffix will be one 
    larger than the maximum existing suffix, and 1 otherwise.
    The optional parameter copy_suffix is the suffix of the folder the client 
    wishes to copy from. It is only used for the default template.
    '''
    # Find the largest integer suffix, or 0.
    max_suffix = get_largest_int(self.__folder_suffixes()) or 0

    # Create new name and new folder.
    new_run_name = self.prefix + str(max_suffix + 1)
    new_folder = self.base_path / new_run_name
    print("Making new folder " + new_run_name + "...")
    new_folder.mkdir()
    print("Created folder " + new_run_name + ".")

    # Copy template files.
    print("Copying template files to new folder...")
    self.__copy_template(new_folder, new_run_name, copy_suffix or max_suffix)
    print("Template files copied. Setup of folder " + new_run_name + " is complete.")

    # Finish.
    print("Have fun!")

  def __folder_suffixes(self):
    '''
    Finds all folders begining with self.prefix, and returns their suffixes.
    '''
    return [last_element(x.parts)[len(self.prefix):] \
            for x in self.base_path.glob(self.prefix + '*') if x.is_dir()]

  def __copy_template(self, new_folder, new_run_name, copy_suffix):
    '''
    Copies all the files from the template folder, but prepends new_run_name.
    Does not recursive copy, in case the template folder is huge.
    '''
    for f in [x for x in self.template_path.iterdir()]:
      new_file_name = new_run_name + "_" + last_element(f.parts)
      copyfile(f, new_folder / new_file_name)
    # The default template has extra setup.
    if self.default_template:
      self.__setup_notes_file(new_folder, new_run_name, copy_suffix)


  def __setup_notes_file(self, new_folder, new_run_name, copy_suffix):
    '''
    Makes a header out of the new run's suffix, and copies TODO list from
    the run with suffix copy_suffix, if one exists.
    '''
    # Make header.
    run_suffix = new_run_name[len(self.prefix):]
    content = self.__make_header(run_suffix)
    # Make TODO list.
    if copy_suffix > 0:
      old_run = self.prefix + str(copy_suffix)
      old_notes = self.base_path / old_run / (old_run + '_notes.txt')
      if old_notes.exists():
        content = content + self.__make_todo(old_notes)
    # Write content to new file.
    new_notes =  new_folder / (new_run_name + '_notes.txt')
    new_notes.write_text(content)

  def __make_header(self, run_suffix):
    title = "Notes " + run_suffix
    padding = ' '
    line_width = len(title) + 2 * len(padding) + len('||||||||')
    header = (line_width - 2) * '=' + '||\n'    + \
            '||'    + (line_width - 6) * '='    + '||||\n' + \
            '||||'  + padding + title + padding + '||||\n' + \
            '||||'  + (line_width - 6) * '='    + '||\n' + \
            '||'    + (line_width - 2) * '='    + '\n' + \
            '\n'
    return header

  def __make_todo(self, old_notes):
    tag = '*NEXT'
    new_tag = '*THIS'
    todo = ''
    with old_notes.open() as f:
      line = f.readline()
      while line:
        if line.startswith(tag):
          todo = todo + new_tag + line[len(tag):]
        line = f.readline()

    return todo

