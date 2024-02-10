"""
Brute-Force PDF Password Breaker
Say you have an encrypted PDF that you have forgotten the password to,
but you remember it was a single English word. Trying to guess your forgotten
 password is quite a boring task. Instead you can write a program that
will decrypt the PDF by trying every possible English word until it finds one
that works. This is called a brute-force password attack. Download the text file
dictionary.txt from https://nostarch.com/automatestuff2/. This dictionary file contains
 over 44,000 English words with one word per line.
Using the file-reading skills you learned in Chapter 9, create a list of
word strings by reading this file. Then loop over each word in this list, passing
it to the decrypt() method. If this method returns the integer 0, the password
 was wrong and your program should continue to the next password.
If decrypt() returns 1, then your program should break out of the loop and
print the hacked password. You should try both the uppercase and lowercase
 form of each word. (On my laptop, going through all 88,000 uppercase
and lowercase words from the dictionary file takes a couple of minutes. This
is why you shouldn’t use a simple English word for your passwords.)


@author Sharaf Qeshta
"""

import PyPDF2

text_file_name = "dictionary.txt"
pdf_file_name = "brute_force.pdf"

text_file = open(text_file_name)
pdf_file = open(pdf_file_name, 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
found = False

for line in text_file:
    stripped_line = line.strip()
    try:
        """
        as it stated in the documentations 
            NOT_DECRYPTED = 0
            USER_PASSWORD = 1
            OWNER_PASSWORD = 2
        """
        if pdf_reader.decrypt(stripped_line.upper()) >= 1:
            print(f"The password is {stripped_line.upper()}")
            found = True
            break
        if pdf_reader.decrypt(stripped_line.lower()) >= 1:
            print(f"The password is {stripped_line.lower()}")
            found = True
            break
    except Exception as error:
        print(error)

if not found:
    print("The password is not exist in dictionary.txt")

text_file.close()
pdf_file.close()
