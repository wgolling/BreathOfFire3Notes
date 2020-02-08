from pathlib import Path
from objects.newrun import RunFolderMaker

#
# Main method.
#
def main():

  # Get the path to the parent of the folder containing this script file.
  path_to_runs_folder = Path(__file__).absolute().parents[1]

  rfm = RunFolderMaker(path_to_runs_folder)
  rfm.setup_folder()

if __name__ == '__main__':
  main()






