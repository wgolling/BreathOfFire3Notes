# Breath of Fire III Notes

This is a project to help me take notes when doing runs for Breath Of Fire III. 
I want to keep track of things like character levels, various attributes related
to the game's Zenny currency (Zenny that is picked up, gotten from boss drops,
spent, etc.), current Skill Ink amounts, and a checklist for the weapons that are
needed to unlock the master D'Lonzo as soon as the player reaches her. These
attributes are tracked over time in segments called "splits", and the project
contains objects and scripts for tracking and printing this data, as well as
setting up new run folders. For more information, see `manual.txt`.

Note: this project uses the pathlib library and so requires Python 3.4 or higher.

The first part of the project is a small script for setting up new notes files. 
Running the script `scripts/new_run.py` with python3 will create a new folder 
parallel to the `scripts` folder, with the prefix "run" and whose suffix is the 
next positive integer which has not been used yet. It will also copy all of the
contents of the `scripts/template` folder into the new folder. In the `notes.txt`
file, it will add a header which is specific to the new suffix, and if there was a
previous run with notes the script will look through its notes file for lines
starting with "`*NEXT TIME`" and create a TODO list out of them in the new notes
file. The script also creates a `data.py` file and sets it up to recieve commands
from the user.

The constructor of the `RunFolderMaker` object also allows the user to specify
their own prefix and template path. In the future I want these to be command
line arguments.

The second part of the project is the `DataTracker` class in 
`scripts/objects/datatracker.py`. This object tracks several game statistics: 
the current members of the party, the party's levels, weapon amounts for the 
[D'Lonzo checklist](https://bof.fandom.com/wiki/D%27Lonzo), and several attributes
related to Skill Ink and Zenny. This information is organized into time segments, 
or "splits", and there are public interface methods for accessing the data from 
a given split. Some attributes are tracked using a simple int value, but others
are tracked with a list of ints (such as Zenny pick-ups). In order to avoid 
annoying type-checking there are BasicValue and ListValue classes with the same
interface, and the complicated logic is taken care of by choosing the appropriate
type. 

For a given run, the user writes commands in the `<run_name>_data.py`
file to input commands to their `DataTracker`'s interface. The data file consists
of a single defition for a function called `track_data`, which takes a
`DataTracker` instance and applies a sequence of commands as written by the user.

The third part is the `DataPrinter` object, which produces a readable output string
from the information in a `DataTracker`. It has a `print()` method that outputs
the string, and the line width is an optional parameter that defaults to 60.

The final part is the `print_data` script. It take a single command line 
argument which is the name of the run, and imports `track_data` from the run's
`<run_name>_data.py` file. It constructs a fresh `DataTracker` object and passes
it to `track_data`, and then passes the string data to a `DataPrinter` object and 
writes the output to `<run_name>/<run_name>_data.txt`.

## TODO

### `new_run`

- Make prefix and template path into command line arguments. Make sure the user 
can't break anything.

### `DataTracker`

- Cleanup/refactor.

### `DataPrinter`

- Polish output string/debug.

- Documentation.

### At some point, down the road, eventually, etc., etc....

- Make a CLI or GUI for the `DataTracker` object.

- Serialize `DataTracker` information.
