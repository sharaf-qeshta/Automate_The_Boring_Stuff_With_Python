"""
Selective Copy
Write a program that walks through a folder tree and searches for files with
a certain file extension (such as .pdf or .jpg). Copy these files from whatever
location they are in to a new folder.

@author Sharaf Qeshta
"""
import os
import re
import shutil

pattern = re.compile("txt$")
for folder_name, sub_folders, filenames in os.walk('C:\\delicious'):
    for filename in filenames:
        if pattern.search(filename) is not None:
            shutil.copy(f"{folder_name}\\{filename}", "C:\\folder")
