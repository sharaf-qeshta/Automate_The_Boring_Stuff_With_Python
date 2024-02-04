"""
PDF Paranoia
Using the os.walk() function from Chapter 10, write a script that will go
through every PDF in a folder (and its subfolders) and encrypt the PDFs
using a password provided on the command line. Save each encrypted PDF
with an _encrypted.pdf suffix added to the original filename. Before deleting
the original file, have the program attempt to read and decrypt the file to
ensure that it was encrypted correctly.
Then, write a program that finds all encrypted PDFs in a folder (and its
subfolders) and creates a decrypted copy of the PDF using a provided password.
 If the password is incorrect, the program should print a message to
the user and continue to the next PDF.

@author Sharaf Qeshta
"""

import os
import PyPDF2

PASSWORD = "Sharaf_Keshta"

def encrypt():
    for folder_name, sub_folders, filenames in os.walk('C:\\pdfs'):
        for filename in filenames:
            if filename.endswith(".pdf"):
                # create a new pdf file
                pdf_file = open(f'C:\\pdfs\\{filename}', 'rb')
                pdf_reader = PyPDF2.PdfReader(pdf_file)  # PdfFileReader is deprecated
                pdf_writer = PyPDF2.PdfWriter()  # PdfFileWriter is deprecated
                for page_number in range(len(pdf_reader.pages)):
                    pdf_writer.add_page(pdf_reader.pages[page_number])

                # start encrypting the file
                pdf_writer.encrypt(PASSWORD)
                result_pdf = open(f'C:\\pdfs\\{filename}_encrypted.pdf', 'wb')
                pdf_writer.write(result_pdf)
                result_pdf.close()

def decrypt():
    for folder_name, sub_folders, filenames in os.walk('C:\\pdfs'):
        for filename in filenames:
            if filename.endswith(".pdf"):
                pdf_file = open(f'C:\\pdfs\\{filename}', 'rb')
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                if pdf_reader.is_encrypted:
                    pdf_reader.decrypt(PASSWORD)
                    pdf_file.close()
                    new_file_name = f'C:\\pdfs\\{filename.replace("_encrypted.pdf", "")}'
                    os.rename(f'C:\\pdfs\\{filename}', new_file_name, src_dir_fd=None, dst_dir_fd=None)

                    result_pdf = open(new_file_name, 'wb')
                    pdf_writer = PyPDF2.PdfWriter()
                    pdf_writer.write(result_pdf)
                    result_pdf.close()

decrypt()