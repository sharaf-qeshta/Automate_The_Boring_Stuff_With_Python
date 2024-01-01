"""
Extending the Multi-Clipboard
Extend the multi-clipboard program in this chapter so that it has a delete
<keyword> command line argument that will delete a keyword from the shelf.
Then add a delete command line argument that will delete all keywords.


@author Sharaf Qeshta
"""

import shelve
import pyperclip
import sys

mcb_shelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
    # To delete items in a shelve, pass the keyword as an argument to del mcb_shelf[keyword]
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcb_shelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    # To delete all arguments, run a loop through the list of keys
    elif sys.argv[1].lower() == 'deleteall':
        for keyword in list(mcb_shelf.keys()):
            del mcb_shelf[keyword]
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
mcb_shelf.close()
