import sys 
from pathlib import Path
from importlib import import_module

script_location = Path(__file__).absolute()
root_folder = script_location.parents[1]
objects_folder = root_folder / 'scripts/objects'
sys.path.insert(1, str(objects_folder))
from datatracker import DataTracker
from dataprinter import DataPrinter

def main(argv):

  # Take a command line argument from the user to use as the run name.
  if (not argv):
    print("Must specify the folder name of the run.")
    return
  run_name = argv[0]

  # Check to see if a folder with that name is in the parent folder of `scripts`.
  run_folder = root_folder / run_name
  assert(run_folder.exists())
  assert(run_folder.is_dir())

  # Check for a <name>_data.py and try to import it.
  module_name = run_name + '_data'
  file_name = module_name + '.py'
  data_file = run_folder / file_name
  init_file = run_folder / '__init__.py'
  assert(data_file.exists())
  assert(init_file.exists())
  sys.path.insert(1, str(root_folder) + '/' + run_name)                       # Add run folder to path variable so the data module can be imported.
  mod = import_module(module_name)

  # Initialize a DataTracker and call the imported module's track_data function on it.
  dt = DataTracker()
  mod.track_data(dt)

  # Construct a DataPrinter with the updated DataTracker's strings, and
  # print the output to <root_folder>/<run_name>/<run_name>_data.txt
  dp = DataPrinter(run_name, dt.get_strings())
  file = Path(run_folder / (module_name + '.txt'))
  file.write_text(dp.print())

if __name__ == "__main__":
  main(sys.argv[1:])
