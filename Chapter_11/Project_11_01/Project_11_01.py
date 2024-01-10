"""
Debugging Coin Toss
The following program is meant to be a simple coin toss guessing game. The
player gets two guesses (it’s an easy game). However, the program has several
bugs in it. Run through the program a few times to find the bugs that keep
the program from working correctly.
import random
guess = ''
while guess not in ('heads', 'tails'):
 print('Guess the coin toss! Enter heads or tails:')
 guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
 print('You got it!')
else:
 print('Nope! Guess again!')
 guesss = input()
 if toss == guess:
 print('You got it!')
 else:
 print('Nope. You are really bad at this game.')


@author Sharaf Qeshta
"""
import random

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1)  # 0 is tails, 1 is heads

if toss == guess:  # you cannot compare a string to an integer "1 != heads and 0 != tails"
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()  # guess misspelled in here so what ever the input is it will execute the else block
    if toss == guess:  # you cannot compare a string to an integer
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
