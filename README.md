# Breath of Fire III Notes

This is a project to help me take notes when doing runs for Breath Of Fire III.

At the moment it contains a small script for setting up new notes files. Running the script `scripts/new_run.py` with python3 will create a new folder parallel to the `scripts` folder, with the prefix "run" and whose suffix is the next positive integer which has not been used as a suffix. It will also copy all of the contents of the `scripts/template` folder into the new folder, and add a header to the `notes.txt` file which is specific to the new suffix. If there was a previous run with notes, the script will look through its notes file for lines starting with "`*NEXT TIME`" and create a TODO list out of them in the new notes folder.  

The constructor of the `RunFolderMaker` object also allows the user to specify their own prefix and template path. In the future I want these to be command line arguments.