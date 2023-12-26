"""
Regex Version of the strip() Method
Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to
strip, then whitespace characters will be removed from the beginning and
end of the string. Otherwise, the characters specified in the second argument
 to the function will be removed from the string.

@author Sharaf Qeshta
"""
import re


def strip(string, characters=''):
    if len(characters) == 0:
        regex = re.compile(r"^[ \t\n]+")
        returned_value = regex.sub("", string)
        regex2 = re.compile(r"[ \t\n]+$")
        return regex2.sub("", returned_value)

    regex = re.compile(fr"[{characters}]")
    return regex.sub("", string)

print(strip("Hello", "ole"))
print(strip("              Hello sharaf     dasjkldjasld    "))
print(strip("Sharaf Keshta.", "Sa."))
