# Breath of Fire III Notes

This is a project to help me take notes when doing runs for Breath Of Fire III.

The first part of the project is a small script for setting up new notes files. 
Running the script `scripts/new_run.py` with python3 will create a new folder 
parallel to the `scripts` folder, with the prefix "run" and whose suffix is the 
next positive integer which has not been used yet. It will also copy all of the
contents of the `scripts/template` folder into the new folder, and add a header
to the `notes.txt` file which is specific to the new suffix. If there was a
previous run with notes, the script will look through its notes file for lines
starting with "`*NEXT TIME`" and create a TODO list out of them in the new notes
file.  

The constructor of the `RunFolderMaker` object also allows the user to specify
their own prefix and template path. In the future I want these to be command
line arguments.

The second part of the project is the `DataTracker` class in 
`scripts/objects/datatracker.py`. This object tracks several game statistics: 
the current members of the party, the party's levels, weapon amounts for the 
[D'Lonzo checklist](https://bof.fandom.com/wiki/D%27Lonzo), and several attributes
related to Skill Ink and Zenny. This information is organized into time segments, 
or "splits", and there are public interface methods for accessing the data from 
a given split. For a given run, the user will use a `data.py` file to input 
commands to their `DataTracker`'s interface.

The third piece is the `DataPrinter` object, which produces a readable output string
from the information in a `DataTracker`. It has a `print()` method that outputs
the string, and the line width is an optional parameter that defaults to 60.

## TODO

### `new_run`

- Update the script to set up a `data.py` file which imports `DataTracker` and
`DataPrinter`. The user will write commands in this file using the `DataTracker`
public interface, and it should write the output from a `DataPrinter` object to a
file in the same folder.

- Make prefix and template path into command line arguments. Make sure the user 
can't break anything.

- Make a demonstration folder.

### `DataTracker`

- Write a `Value` class to replace `absolute_value` helper function and some 
awkward type checking and printing difficulties.

### `DataPrinter`

- Polish output string.

- Documentation.

### At some point, down the road, eventually, etc., etc....

- Make a GUI for the `DataTracker` object.

- Serialize `DataTracker` information.
