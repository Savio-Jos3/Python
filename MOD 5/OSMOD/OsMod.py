import os

#OS module provides functions for interacting with the operating system
#os module is a built-in module in Python

print(os.name) # name of the current os module
print(os.getcwd()) # current working directory
print(os.listdir()) # list of files in the current directory
print(os.path.abspath('OsMod.py')) # absolute path of the file
print(os.getcwd()) # current working directory
os.mkdir('new_dir') # create a new directory 
os.rmdir('new_dir') # remove a directory
os.rename('OsMod.py', 'OsMod1.py') # rename a file
os.remove('file.txt') # remove a file
print(os.path.exists('OsMod1.py')) # check if a file exists
os.chdir('..') # change the current working directory

