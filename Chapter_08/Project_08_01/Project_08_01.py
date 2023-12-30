"""
Sandwich Maker
Write a program that asks users for their sandwich preferences. The program
 should use PyInputPlus to ensure that they enter valid input, such as:
•	 Using inputMenu() for a bread type: wheat, white, or sourdough.
•	 Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
•	 Using inputYesNo() to ask if they want cheese.
•	 If so, using inputMenu() to ask for a cheese type: cheddar, Swiss,
or mozzarella.
•	 Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
•	 Using inputInt() to ask how many sandwiches they want. Make sure this
number is 1 or more.
Come up with prices for each of these options, and have your program
display a total cost after the user enters their selection.

@author Sharaf Qestha
"""

import pyinputplus as pyin

BREAD_PRICES = [1.25, 1, 1.5]
PROTEIN_PRICES = [3, 2.45, 2.12, 1.5]
CHEESE_PRICES = [1.5, 1.4, 1.3]
TOP_PRICES = [0.25, 0.30, 0.45, 0.52]


def get_input():
    bread_type = pyin.inputMenu(["wheat", "white", "sourdough"])
    protein_type = pyin.inputMenu(["chicken", "turkey", "ham", "tofu"])
    cheese_type = pyin.inputMenu(["cheddar", "Swiss", "mozzarella"])
    top = pyin.inputMenu(["mayo", "mustard", "lettuce", "tomato"])
    count = pyin.inputInt(prompt="How many sandwiches you want?", min=1)

    total_cost = 0
    if bread_type == "wheat":
        total_cost += BREAD_PRICES[0]
    elif bread_type == "white":
        total_cost += BREAD_PRICES[1]
    else:
        total_cost += BREAD_PRICES[2]

    if protein_type == "chicken":
        total_cost += PROTEIN_PRICES[0]
    elif protein_type == "turkey":
        total_cost += PROTEIN_PRICES[1]
    elif protein_type == "ham":
        total_cost += PROTEIN_PRICES[2]
    else:
        total_cost += PROTEIN_PRICES[3]

    if cheese_type == "cheddar":
        total_cost += CHEESE_PRICES[0]
    elif cheese_type == "Swiss":
        total_cost += CHEESE_PRICES[1]
    else:
        total_cost += CHEESE_PRICES[2]

    if top == "mayo":
        total_cost += TOP_PRICES[0]
    elif top == "mustard":
        total_cost += TOP_PRICES[1]
    elif top == "lettuce":
        total_cost += TOP_PRICES[2]
    else:
        total_cost += TOP_PRICES[3]

    total_cost = total_cost * count
    print(f"Total Price is ${total_cost}")


get_input()
