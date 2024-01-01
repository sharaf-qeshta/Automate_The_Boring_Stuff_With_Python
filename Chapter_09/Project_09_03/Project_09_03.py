"""
Regex Search
Write a program that opens all .txt files in a folder and searches for any
line that matches a user-supplied regular expression. The results should
be printed to the screen.

@author Sharaf Qeshta
"""

import re
import os

user_regex = input("Enter a regex to search for: ")

print("The following lines matched your regex:")

pattern = re.compile(r"%s" % user_regex)
for file_name in os.listdir("./"):
    if re.compile(r"\.txt$").search(file_name) is not None:
        file = open(file_name, "r")
        for line in file:
            if pattern.search(line) is not None:
                print(line.strip())
        file.close()
