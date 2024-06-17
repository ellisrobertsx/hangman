import random

""" List of possible words"""
comedy_list = ['Step Brothers', 'The Hangover', 'Grown Ups', 'Dodgeball', 'Internship', 'Ted', 'Scary Movie', 'American Pie', 'Due Date', 'The Other Guys']
action_list = ['James Bond', 'John Wick', 'The Matrix', 'Rambo', 'The Gray Man', 'Deep Water Horizon', 'The Maze Runner', 'Batman', 'Catch me if you can', 'Heat']
horror_list = ['Saw', 'The Purge', 'Halloween', 'A nightmare on Elm street', 'The Conjuring', 'Psycho', 'Scream', 'Paranormal Activity', 'Alien', 'The Silence of the Lambs']

def select_game_mode():
    while True:
        mode = input("Select a game mode: 'comedy', 'action', or 'horror': ").lower()
        if mode == 