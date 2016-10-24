=====
NewPy
=====

*A simple utility to create files and folders based on templates*

With this program you can define template files, for instance a Python script 
with some documentation or functions already defined, or a directory for a 
LaTeX document. See the example directory for an example of a Python script.

Usage
=====

Usage is quite simple, type::

    ./new.py

on the command line to get an overview of the current templates, and their 
names. Templates should be stored in the home directory, in the directory 
`${HOME}/.newpy_templates`. If you have for instance a Python script with the 
name `python.py` as template name, you will get::

    ./new.py
    Available targets:
    Name	  	File / Dir
    ----	  	----------
    python	->	python.py

With the target name `python`, you can use the following command to copy the 
template to the current directory::

    ./new.py python

This will create a new file in the current directory named `python.py`.  
Finally, there is the option of naming the file in the current directory 
differently::

    ./new.py python myscript.py

This will create the file `myscript.py`, as a copy of the `python.py` 
template.

Installation
============

Simply download the script, create a template or two, and start using it! For 
added usability, you can create an alias in your `~/.bashrc` file, for 
instance:

    alias new="/path/to/new.py"

Then you can simply type `new <target>` in your terminal.

Afterwords
==========

Author: G.J.J. van den Burg

Date: 2016-10-24

License: GPLv3
