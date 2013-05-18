---+ Project description

This code is part of an academic project in which we try to make a computer
program that learns poetic form based on poems as training data. 

---+ Run

To run the code from this project, execute one of the following:

==
swipl -s debug.pl
swipl -s load.pl
==

---++ Environment

This script was tested using SWI-Prolog 6.3.15.

---++ Data

We intend to store data outside of the source code directory, because that
location may not be writeable by the user. A subdirectory in the user's
home is created (called '.EAPoem').

Currently there seems to be a problem with creating this directory on
Windows (absolute_file_name/3). See module LOGGING for this.

---+ Documentation

The documentation for this project can be accessed at http://localhost:2222,
once the file _|load.pl|_ is started.

---+ Console

The Web console for this project can be accessed at http://localhost:5000.
