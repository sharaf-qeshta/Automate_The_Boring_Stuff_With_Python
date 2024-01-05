"""
Deleting Unneeded Files
It’s not uncommon for a few unneeded but humongous files or folders to
take up the bulk of the space on your hard drive. If you’re trying to free up
room on your computer, you’ll get the most bang for your buck by deleting
the most massive of the unwanted files. But first you have to find them.
Write a program that walks through a folder tree and searches for exceptionally
 large files or folders—say, ones that have a file size of more than
100MB. (Remember that to get a file’s size, you can use os.path.getsize() from
the os module.) Print these files with their absolute path to the screen.

@author Sharaf Qeshta
"""

import os
import re

pattern = re.compile("txt$")
for folder_name, sub_folders, filenames in os.walk('C:\\delicious'):
    for filename in filenames:
        size = os.path.getsize(f"{folder_name}\\{filename}") / 1048576.0
        if size > 100:
            print(f"File Name: {filename}, Size: {size}")