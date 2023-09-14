"""
Input Validation
Add try and except statements to the previous project to detect whether the
user types in a noninteger string. Normally, the int() function will raise a
ValueError error if it is passed a noninteger string, as in int('puppy'). In the
except clause, print a message to the user saying they must enter an integer.

@author Sharaf Qeshta
"""


def collatz(number):
    if number % 2 == 0:
        returned_value = number // 2
        print(returned_value)
        return returned_value
    if number % 2 == 1:
        returned_value = 3 * number + 1
        print(returned_value)
        return returned_value


def main():
    try:
        number = int(input("Enter number:"))
    except ValueError:
        print("you must enter an integer value")
        return

    collatz_value = collatz(number)
    while collatz_value != 1:
        collatz_value = collatz(collatz_value)


main()
