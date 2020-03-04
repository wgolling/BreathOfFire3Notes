# Breath of Fire III Notes

This is a project to help me take notes when doing runs for Breath Of Fire III.

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
related to Skill Ink and Zenny. Since some attributes are kept track of with ints 
and others with lists of ints, the annoying type-checking is taken care of with
`BasicValue` and `ListValue` classes which have the same interface. This information is organized into time segments, or "splits", and there are public interface methods
for accessing the data from a given split. For a given run, the user writes
commands in the `data.py` file to input commands to their `DataTracker`'s interface.

The third piece is the `DataPrinter` object, which produces a readable output string
from the information in a `DataTracker`. It has a `print()` method that outputs
the string, and the line width is an optional parameter that defaults to 60.

## TODO

### `new_run`

- Make prefix and template path into command line arguments. Make sure the user 
can't break anything.

- Make a demonstration folder.

### `DataTracker`

- Clean up/refactor etc.

### `DataPrinter`

- Polish output string.

- Documentation.

### At some point, down the road, eventually, etc., etc....

- Make a GUI for the `DataTracker` object.

- Serialize `DataTracker` information.
