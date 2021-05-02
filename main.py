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


# Testing 
print(desktop)
print(documents)
print(outputFolder)

# Find all files from desktop and sends information to output folder 
for root, subdirs, files in os.walk(desktop):
    for folder in subdirs:
        for name in files:
            createFolder = outputFolder + "\\" + folder
            dest = outputFolder + "\\" + folder + "\\" + name
            if not os.path.exists(createFolder):
                os.makedirs(createFolder)
            copyfile(os.path.join(root, name), dest)

            # Testing 
            debug = dest.encode("utf-8")
            print(debug)