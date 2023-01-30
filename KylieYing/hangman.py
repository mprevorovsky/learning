# import nouns CSV from https://www.wordexample.com/list/most-common-nouns-english
# pick a random word

# diplay word or dashes
# diplay letters already tried
# make sure no letter is tried twice
# ending (win/lose)
# implement lives


import csv
import random
import string
import os


def get_words(csv_file_name):
    with open(csv_file_name) as csvfile:
        words = list(csv.reader(csvfile))
        words.pop(0)
    return words


def get_random_word(words):
    random_index = random.randint(0, len(words) + 1)
    random_word = words[random_index][0]
    return random_word


def dashes_to_letters(puzzle_word, word_guess, letter_guess):
    global lives
    word_guess = list(word_guess)
    c = 0
    is_correct = False
    for letter in puzzle_word:
        if letter == letter_guess:
            is_correct = True
            word_guess[c] = letter_guess
        c += 1
    if not is_correct:
        lives -= 1
    return ''.join(word_guess)


def evaluate_guess(puzzle_word, word_guess):
    letter_guess = str(input('Guess a letter: ')).lower()
    if letter_guess not in ALPHABET:
        message = f'"{letter_guess}" is not a valid letter!'
    elif letter_guess in letters_tried:
        message = f'You have already tried the letter "{letter_guess}"!'
    else:
        letters_tried.append(letter_guess)
        word_guess = dashes_to_letters(puzzle_word, word_guess, letter_guess)
        message = ''
    return word_guess, message



ALPHABET = list(string.ascii_lowercase)
CSV_FILE_NAME = 'most-common-nouns-english.csv'
letters_tried = []
lives = 6
message = ''

words = get_words(CSV_FILE_NAME)
puzzle_word = get_random_word(words)
word_guess = len(puzzle_word) * '-'

os.system('clear')
while '-' in word_guess and lives > 0:
    os.system('clear')
    print(message)
    print(word_guess)
    print(letters_tried)
    print(f'You have {lives} lives.')
    word_guess, message = evaluate_guess(puzzle_word, word_guess)
if lives > 0:
    print(f'\nCongratulations, you guessed the word "{word_guess}"!')
else:
    print(f'You lost all your lives. The correct solution was {puzzle_word}.')

