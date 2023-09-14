"""
Comma Code
Say you have a list value like this:
spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and
inserted before the last item. For example, passing the previous spam list to
the function would return 'apples, bananas, tofu, and cats'.
 But your function should be able to work with any list value passed to it. Be sure to test
the case where an empty list [] is passed to your function.


@author Sharaf Qeshta
"""


def main(array):
    returned = ""
    for i in range(len(array)):
        if i == len(array) - 1:
            returned += "and " + array[i]
        else:
            returned += array[i] + ", "
    return returned


spam = ['apples', 'bananas', 'tofu', 'cats']
print(main(spam))
