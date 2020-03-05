import sys 
from pathlib import Path
import importlib

root_folder = Path(__file__).absolute().parents[1]
sys.path.insert(1, str(root_folder) + '/scripts/objects')
from datatracker import DataTracker
from dataprinter import DataPrinter

def main(argv):
  # Print data takes a command line input form the user.
  if (not argv):
    print("Must specify the folder name of the run.")
    return
  run_name = argv[0]
  # It checks to see if a folder with that name in the parent folder of `scripts`.
  script_location = Path(__file__).absolute()
  path_to_runs_folder = script_location.parents[1]
  run_folder = path_to_runs_folder / run_name
  assert(run_folder.exists())
  assert(run_folder.is_dir())
  # If it exists, it checks for a <name>_data.py and tries to import it.
  module_name = run_name + '_data'
  file_name = module_name + '.py'
  data_file = run_folder / file_name
  init_file = run_folder / '__init__.py'
  assert(data_file.exists())
  assert(init_file.exists())
  sys.path.insert(1, str(root_folder) + '/' + run_name)
  mod = importlib.import_module(module_name)
  # If the import succeeds, it initializes a DataTracker and calls the imported
  # file's "track data" function on it.
  dt = DataTracker()
  mod.track_data(dt)
  # Then it constructs a DataPrinter with the updated DataTracker's strings, and
  # prints the output to notes/<name>/<name>_data.txt
  dp = DataPrinter(run_name, dt.get_strings())
  file = Path(run_folder / (module_name + '.txt'))
  file.write_text(dp.print())


if __name__ == "__main__":
  main(sys.argv[1:])