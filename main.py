import os
import pathlib
import getpass

# Current user
username = getpass. getuser()

# Top folders 
desktop = os.path.expanduser("~\Desktop")
documents = os.path.expanduser("~\Documents")

# Testing functions
print(desktop)
print(documents)

for root, subdirs, files in os.walk(desktop):
    for d in subdirs:
        print(d)

        