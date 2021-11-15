# Created by:       Brad Arrowood
# Created on:       2021.11.15
# Last updated:     2021.11.15
# Script name:      emptyDir.py
# Description:      script to check if a directory is empty and delete folder if it is.
#                   might set up for it to later check folder size and if under specific amount to also delete.

import os

root='C:/Users/username/test/'
emptyDirs = 'empty_directories.txt'

def isEmpty(path):
    if os.path.exists(path) and not os.path.isfile(path):
  
        # checking if the directory is empty or not
        # if no sub-folders or files then folder is added to a file to log it before the folder is deleted
        if not os.listdir(path):
            f.write(path)
            f.write('\n')
            os.rmdir(path)
        else:
            print(path + " - Directory not empty")
    else:
        print("The path is either for a file or not valid")

# this section gets the list of folders within the root directory
dirlist = [ item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item)) ]

with open(emptyDirs, "a") as f:
    for dir in dirlist:
        path = root + dir
        isEmpty(path)
