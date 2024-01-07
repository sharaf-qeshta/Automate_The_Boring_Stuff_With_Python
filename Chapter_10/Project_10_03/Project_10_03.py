"""
Filling in the Gaps
Write a program that finds all files with a given prefix, such as spam001.txt,
spam002.txt, and so on, in a single folder and locates any gaps in the numbering
 (such as if there is a spam001.txt and spam003.txt but no spam002.txt).
Have the program rename all the later files to close this gap.
As an added challenge, write another program that can insert gaps
into numbered files so that a new file can be added.

@author Sharaf Qeshta
"""

import os
import shutil

prefix = "spam"
numbers = []
extension = ""
numbering_length = 0
folder_name = "C:\\delicious"

for file in os.listdir(folder_name):
    if os.path.isdir(file):
        continue

    if file.startswith(prefix):
        new_file = file.replace(prefix, "")
        extension_and_number = new_file.split(".")
        numbers.append(int(extension_and_number[0]))
        numbering_length = len(extension_and_number[0])
        extension = extension_and_number[1]

for i in range(0, len(numbers)-1):
    if numbers[i+1] - numbers[i] > 1:
        # closing the gap
        gap = numbers[i+1] - numbers[i]
        new_number = numbers[i+1] - gap + 1
        new_number_length = len(str(new_number))
        old_number_length = len(str(numbers[i+1]))
        new_file_name = f"{folder_name}\\{prefix}{'0' * (numbering_length - new_number_length)}{new_number}.{extension}"
        old_file_name = f"{folder_name}\\{prefix}{'0' * (numbering_length - old_number_length)}{numbers[i+1]}.{extension}"
        shutil.move(old_file_name, new_file_name)
        numbers[i + 1] = new_number
