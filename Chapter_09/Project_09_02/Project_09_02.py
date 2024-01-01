"""
Mad Libs
Create a Mad Libs program that reads in text files and lets the user add
their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
appears in the text file. For example, a text file may look like this:
The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.
The program would find these occurrences and prompt the user to
replace them.
Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck
The following text file would then be created:
The silly panda walked to the chandelier and then screamed. A nearby pickup
truck was unaffected by these events.
The results should be printed to the screen and saved to a new text file.


@author Sharaf Qeshta
"""

import re

file = open('text.txt', 'r')
content = file.read()
mad_lib_words = list(content.split())
file.close()

adj_regex = re.compile(r'ADJECTIVE')
noun_regex = re.compile(r'NOUN')
adv_regex = re.compile(r'ADVERB')
verb_regex = re.compile(r'VERB')

result_file = open('result.txt', 'w')
result_string = ""
for word in mad_lib_words:
    if adj_regex.match(word):
        word = adj_regex.sub(input("Give an adjective: "), word)
    elif noun_regex.match(word):
        word = noun_regex.sub(input("Give a noun: "), word)
    elif verb_regex.match(word):
        word = verb_regex.sub(input("Give a verb: "), word)
    elif adv_regex.match(word):
        word = adv_regex.sub(input("Give a adverb: "), word)
    result_string += word + " "
    result_file.write(word + " ")

print(result_string)
result_file.close()
