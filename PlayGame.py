# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 12:51:36 2021

@author: Shruti Goel
"""

#import module of hangman stages output
from HangmanStages import display_hangman


def play(word):
    word_length = "_" * len(word)
    guessed = False
    letter_guessed = []
    word_guessed = []
    tries = 6
    print("Let's play Hangman!")
    print("You have to guess the word in 6 tries")
    print(display_hangman(tries))
    print("Word Length:", len(word_length))
    print(word_length)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in letter_guessed:
                print("You already guessed the letter", guess)
                print("You have left", tries, "tries")
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                print("You have left", tries, "tries")
                letter_guessed.append(guess)
            else:
                print("\nGood job,", guess, "is in the word!")
                print("You have", tries, "tries to made.")
                print("Go ahead for next alphabet!!")
                letter_guessed.append(guess)
                word_as_list = list(word_length)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_length = "".join(word_as_list)
                if "_" not in word_length:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in word_guessed:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                word_guessed.append(guess)
            else:
                guessed = True
                word_length = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_length)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries.")
        print("The word was " + word + ".")
        print("Better Luck next time!")
