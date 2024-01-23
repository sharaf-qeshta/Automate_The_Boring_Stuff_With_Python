"""
Blank Row Inserter
Create a program blankRowInserter.py that takes two integers and a filename
string as command line arguments. Let’s call the first integer N and the second
integer M. Starting at row N, the program should insert M blank rows
into the spreadsheet. For example, when the program is run like this:
python blankRowInserter.py 3 2 myProduce.xlsx
. . . the “before” and “after” spreadsheets should look like Figure 13-12.
Figure 13-12: Before (left) and after (right) the two blank rows are inserted at row 3
You can write this program by reading in the contents of the spreadsheet.
 Then, when writing out the new spreadsheet, use a for loop to copy
the first N lines. For the remaining lines, add M to the row number in the
output spreadsheet.

@author Sharaf Qeshta
"""


import openpyxl
import sys

file_name = sys.argv[1]
row_number = int(sys.argv[2])
rows_count = int(sys.argv[3])

wb = openpyxl.load_workbook(file_name)
sheet = wb.active
sheet.insert_rows(row_number, rows_count)
wb.save(file_name)
