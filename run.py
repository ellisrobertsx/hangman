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


def hangman(word_list):
    word = choose_word(word_list)
    word_letters = set(word)
    guessed_letters = set()
    incorrect_guesses = 0
    
    print("Welcome to Hangman!")
    print("/ " * len(word))  # Initial display with '/' instead of '_'
    
    while incorrect_guesses < max_guesses and word_letters:
        print(hangman_stages[incorrect_guesses])
        print(f"\nYou have {max_guesses - incorrect_guesses} guesses left.")
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        
        word_display = [letter if letter in guessed_letters else "_" for letter in word]  
        print("Current word:", " ".join(word_display))
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabetic character.")
        elif guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
        elif guess in word_letters:
            print(f"Good guess! '{guess}' is in the word.")
            guessed_letters.add(guess)
            word_letters.remove(guess)
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            guessed_letters.add(guess)
            incorrect_guesses += 1
    
    if word_letters:
        print(hangman_stages[incorrect_guesses])
        print(f"\nYou lost! The word was '{word}'.")
    else:
        print(f"\nCongratulations! You guessed the word '{word}'!")

def main():
    while True:
        word_list = select_game_mode()  # Get the word list based on the selected mode
        hangman(word_list)
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != 'yes':
            break

# Run the game
main()