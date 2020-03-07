from pathlib import Path
from shutil import copyfile

#
# 
# Utility functions for lists.

def last_element(lst):
  '''Returns the last element of a list, or None if it is empty.'''
  if not lst:
    return None
  return lst[-1]

def get_largest_int(obj_list):
  '''Returns the largest integer value in a list, if there is one.

  Args:
    obj_list (list)

  Returns: The largest int value derived from elements in obj_list, or None
    if none of the elements in obj_list are convertible to int.

  Raises:
    ValueError: If obj_list is not convertible to int.

  '''
  try:
    new_list = list(obj_list)
  except Exception:
    raise ValueError('Input must be convertible to list.')
    
  max_int = None
  for x in new_list:
    try:
      int_x = int(x)
    except ValueError:
      continue 

    if (not max_int) or (int_x and int_x > max_int):
      max_int = int_x
  return max_int

#
# 
# Class for setting up a new run folder.

class RunFolderMaker:
  '''RunFolderMaker sets up a new new run folder.

  It can create a new run folder in the directory specified in its constructor,
  which will contain files copied from a template. The default template includes
  notes.txt, masters.txt, data.py, and __init__.py files, and will set up the
  notes.txt file with a TODO list based on the previous run's notes.txt.

  '''
  def __init__(self, base_path, prefix="run", template_path=None):
    '''Constructs a new RunFolderMaker instance.
    
    Args:
      base_path (str or pathlib.Path): The path to the folder where the new run
        folder will be created.
      prefix (str, optional): The desired prefix for the run name. Defaults to "run".
      template_path (str or pathlib.Path, optional): The path to custom template
        files, if specified. Defaults to <base_path>/scripts/template.

    Raises:
      TypeError: If base_path or template_path are not convertible to pathlib.Path.
      ValueError: If base_path or template_path does not exist.
      ValueError: If base_path or template_path is not a directory.

    '''
    # TODO: make sure input doesn't have any special characters
    #       maybe this is handled already by checking exists()?

    # Initialize and validate self.base_path.
    self.base_path = None
    try:
      self.base_path = Path(base_path)
    except TypeError:
      raise ValueError("base_path must be convertible to pathlib.Path")
    if not self.base_path.exists():
      raise ValueError("base_path does not exist")
    if not self.base_path.is_dir():
      raise ValueError("base_path must be a directory")

    # Initialize self.prefix (str(o) will never throw an exception).
    self.prefix = str(prefix)  

    # Initialize and validate self.template_path and self.default_template.
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
    Creates a new run folder according to a template. 

    Creats folder in self.base_path with prefix self.prefix, using self.template_path.
    If no template was specified in the constructor, uses the default template setup.
    If any folders exist with integer suffixes the new suffix will be one 
    larger than the maximum existing suffix, and 1 otherwise.
    The optional parameter copy_suffix is the suffix of the folder the client 
    wishes to copy from. It is only used for the default template.

    '''
    # Find the largest integer suffix, or 0.
    max_suffix = get_largest_int(self._folder_suffixes()) or 0

    # Create new name and new folder.
    new_run_name = self.prefix + str(max_suffix + 1)
    new_folder = self.base_path / new_run_name
    print("Making new folder " + new_run_name + "...")
    new_folder.mkdir()
    print("Created folder " + new_run_name + ".")

    # Copy template files.
    print("Copying template files to new folder...")
    self._copy_template(new_folder, new_run_name, copy_suffix or max_suffix)
    print("Template files copied. Setup of folder " + new_run_name + " is complete.")

    # Finish.
    print("Have fun!")

  def _folder_suffixes(self):
    '''Finds all folders begining with self.prefix, and returns their suffixes.'''
    return [last_element(x.parts)[len(self.prefix):] \
            for x in self.base_path.glob(self.prefix + '*') if x.is_dir()]

  def _copy_template(self, new_folder, new_run_name, copy_suffix):
    '''Copies all the files from the template folder, but prepends new_run_name.

    Does not recursive copy, in case the template folder is huge.

    '''
    for f in [x for x in self.template_path.iterdir()]:
      new_file_name = new_run_name + "_" + last_element(f.parts)
      copyfile(f, new_folder / new_file_name)
    # The default template has extra setup.
    if self.default_template:
      # Make an init file because the data_printer script will import it as a module.
      init_file = new_folder / '__init__.py'
      init_file.touch(exist_ok=True)
      self._setup_notes_file(new_folder, new_run_name, copy_suffix)
      self._setup_data_file(new_folder, new_run_name)

  def _setup_notes_file(self, new_folder, new_run_name, copy_suffix):
    '''Makes a header out of the new run's suffix, and copies TODO list from
    the run with suffix copy_suffix, if one exists.
    '''
    # Make header.
    run_suffix = new_run_name[len(self.prefix):]
    content = self._make_header(run_suffix)
    # Make TODO list.
    if copy_suffix > 0:
      old_run = self.prefix + str(copy_suffix)
      old_notes = self.base_path / old_run / (old_run + '_notes.txt')
      if old_notes.exists():
        content = content + self._make_todo(old_notes)
    # Write content to new file.
    new_notes =  new_folder / (new_run_name + '_notes.txt')
    new_notes.write_text(content)

  def _setup_data_file(self, new_folder, new_run_name):
    template_file = self.template_path / "data.py"
    assert(template_file.exists())
    template_content = template_file.read_text()
    new_file = new_folder / (new_run_name + '_data.py')
    new_file.write_text(template_content)

  def _make_header(self, run_suffix):
    title = "Notes " + run_suffix
    padding = ' '
    line_width = len(title) + 2 * len(padding) + len('||||||||')
    header = (line_width - 2) * '='             + '||\n' + \
            '||'    + (line_width - 6) * '='    + '||||\n' + \
            '||||'  + padding + title + padding + '||||\n' + \
            '||||'  + (line_width - 6) * '='    + '||\n' + \
            '||'    + (line_width - 2) * '='    + '\n' + \
            '\n'
    return header

  def _make_todo(self, old_notes):
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
