## must be called from notes folder for the paths to work out.

from pathlib import Path
from objects.newrun import RunFolderMaker


#
# Main method.
#
def main():

  path_to_script = Path(__file__).absolute()
  # print(path_to_script)
  path_to_runs_folder = path_to_script.parents[1]
  # print(path_to_runs_folder)
  base_path = path_to_runs_folder

  # #
  # # Testing constructor
  # #
 
  # # invalid base_path input
  # try:
  #   RunFolderMaker(7)
  # except Exception as e:
  #   print("Error: " + str(e))
  # try:
  #   RunFolderMaker(base_path / 'foo')
  # except Exception as e:
  #   print("Error: " + str(e))
  # try:
  #   RunFolderMaker(base_path / 'run_dummy.txt')
  # except Exception as e:
  #   print("Error: " + str(e))

  # # invalid template_path input
  # try:
  #   RunFolderMaker(base_path, template_path=7)
  # except Exception as e:
  #   print("Error: " + str(e))
  # try:
  #   RunFolderMaker(base_path, template_path=base_path / 'foo')
  # except Exception as e:
  #   print("Error: " + str(e))
  # try:
  #   RunFolderMaker(base_path, template_path=base_path / 'run_dummy.txt')
  # except Exception as e:
  #   print("Error: " + str(e))


  #
  # Script
  #

  # Create RunFolderMaker object, and setup folder.
  rfm = RunFolderMaker(base_path)
  rfm.setup_folder()

if __name__ == '__main__':
  main()






