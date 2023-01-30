import random
import os


def compare_choices(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a draw"
    if (player_choice + computer_choice) in WINNING_RESULTS:
        return "You won!"
    return "You lost..."


def play():
    computer_choice = random.choice(OPTIONS)
    player_choice_valid = False
    while not player_choice_valid:
        player_choice = input('Choose either [r]ock, [p]aper or [s]cissors: ').lower()
        if player_choice in OPTIONS:
            player_choice_valid = True

    result = compare_choices(player_choice, computer_choice)
    print(f'The computer chose {computer_choice}.')
    print(result)


more_games = 'y'
OPTIONS = ['r', 'p', 's']
WINNING_RESULTS = ['rs', 'pr', 'sp']

while more_games == 'y':
    os.system('clear')
    play()
    more_games = input('Want to play again? [y]es or [n]o: ').lower()
