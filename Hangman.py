import random
import string
from words import words
# word = words[ri(0, len(words) + 1)]


def valid_check():
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():

    word = valid_check()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    print(word_letters)
    print(word)
    while True:
        user_letter = input('Enter a letter.. ').upper()
        if len(word_letters) == 0:
            print('You guessed it')
            exit()
        elif user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print('Already used')
        else:
            print('Invalid Character')


hangman()
