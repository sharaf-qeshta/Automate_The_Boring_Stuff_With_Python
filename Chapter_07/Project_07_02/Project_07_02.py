"""
Strong Password Detection
Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that is at
least eight characters long, contains both uppercase and lowercase characters,
and has at least one digit. You may need to test the string against multiple
regex patterns to validate its strength.

@author Sharaf Qeshta
"""
import re


def test_password(password):
    if len(password) < 8:
        return False

    if re.compile(r"[A-Z]+").search(password) == None:
        return False

    if re.compile(r"[a-z]+").search(password) == None:
        return False

    return re.compile(r"\d+").search(password) != None


print(test_password("AbcSdeas45"))  # valid
print(test_password("abcsdeas45"))  # not valid
print(test_password("AbcSdeas"))  # not valid
print(test_password("Abcdeas"))  # not valid
print(test_password("SHARAFKESHTA12"))  # not valid
print(test_password("SharafKeshta12"))  # valid
