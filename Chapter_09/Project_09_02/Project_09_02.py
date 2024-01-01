"""

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
