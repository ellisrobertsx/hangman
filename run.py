import random

# List of possible words
comedy_list = ['step brothers', 'the hangover', 'grown ups', 'dodgeball', 'internship', 'ted', 'scary movie', 'american pie', 'due date', 'the other guys']
action_list = ['james bond', 'john wick', 'the matrix', 'rambo', 'the gray man', 'deep water horizon', 'the maze runner', 'batman', 'catch me if you can', 'heat']
horror_list = ['saw', 'the purge', 'halloween', 'a nightmare on elm street', 'the conjuring', 'psycho', 'scream', 'paranormal activity', 'alien', 'the silence of the lambs']


#Max number of guesses allowed 
max_guesses = 6

# Hangman Stages 
hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]


""" Function allows user to select between 3 different game modes"""
def select_game_mode():
    while True:
        mode = input("Select a game mode: Press 'A' for action, 'B' for horror, or 'C' for comedy: ").upper()
        if mode == 'A':
            return action_list
        elif mode == 'B':
            return horror_list
        elif mode == 'C':
            return comedy_list
        else:
            print("Invalid choice. Please press 'A' for action, 'B' for horror, or 'C' for comedy.")

# Selects a random word from the appropriate list
def choose_word(word_list):
    return random.choice(word_list)


