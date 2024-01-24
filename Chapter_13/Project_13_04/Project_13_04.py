"""
Text Files to Spreadsheet
Write a program to read in the contents of several text files (you can make
the text files yourself) and insert those contents into a spreadsheet, with
one line of text per row. The lines of the first text file will be in the cells of
column A, the lines of the second text file will be in the cells of column B,
and so on.
Use the readlines() File object method to return a list of strings, one
string per line in the file. For the first file, output the first line to column 1,
row 1. The second line should be written to column 1, row 2, and so on. The
next file that is read with readlines() will be written to column 2, the next
file to column 3, and so on.


@author Sharaf Qeshta
"""

import openpyxl

text_files = ["text1.txt", "text2.txt", "text3.txt"]
wb = openpyxl.Workbook()
sheet = wb.active

current_column = 1
for text_file in text_files:
    file = open(text_file, "r")
    lines = file.readlines()
    file.close()
    for i in range(len(lines)):
        cell = sheet.cell(row=i + 1, column=current_column)
        cell.value = lines[i]
    current_column += 1

wb.save("project_13_04.xlsx")
