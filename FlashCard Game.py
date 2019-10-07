
"""
This flashcard program allows the user to ask for a glossary entry.
In response,if user select show flash card
the program randomly picks an entry from all glossary
entries. It shows the entry. After the user presses return, the
program shows the definition of that particular entry.
If user select show_definition the program randomly picks a 
definition fro the glossary. It shows the definition and if user 
presses return, the program displays the key of the random definition
displayed.
The user can repeatedly ask for an entry , or the definition also
has the option to quit the program instead of seeing
another entry or definition.
"""

from random import *

def show_flashcard():
    """ Show the user a random key and ask them
        to define it. Show the definition
        when the user presses return.    
    """
    random_key = choice(list(glossary))
    print('Define: ', random_key)
    input('Press return to see the definition')
    print(glossary[random_key])
    
def show_definition():
    """Show the user a random definiton. Show the key
    which is associated with the random definition
    printed above"""
    random_key = choice(glossary.values())
    print(random_key)
    input('Press return to see the word')
    key = glossary.keys()[glossary.values().index(random_key)]
    print key


# Set up the glossary

glossary = {'word1':'definition1',
            'word2':'definition2',
            'word3':'definition3'}

# The interactive loop

exit = False
while not exit:
    user_input = sinput('Enter s to show a flashcard,Enter d to see a definition and q to quit: ')
    if user_input == 'q':
        exit = True
    elif user_input == 's':
        show_flashcard()
    elif user_input == 'd':
        show_definition()
    else:
        print('You need to enter either q or s.')
                    