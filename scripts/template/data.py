import sys
sys.path.insert(1, '../scripts/objects/')
from datatracker import *

dt = DataTracker()

# Segement 0: Awakening
dt.split("Awakening")


### START OF USER COMMANDS ###

#
# ... Your commands go here ...
#

### END OF USER COMMANDS ###


# write DataTracker output to file.

from dataprinter import DataPrinter
from pathlib import Path

# get path to current run folder
path_to_run_folder = Path(__file__).absolute().parent
# make data filename
file = Path(path_to_run_folder / (run_name + "_data.txt"))
# create file
Path.touch(file)
# create output and write to file
dp = DataPrinter(run_name, dt.get_strings())
file.write_text(dp.print())
