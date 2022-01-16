# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 12:25:56 2021

@author: Shruti Goel
"""
#Choose random word from the input list
import random

#Package to import .py file from from directory
import sys

#Add path of python file 

sys.path.insert(1, 'E:\Shruti\Study\MBA\Sem-2\Analytics\Python\Assignments\Assignment Programs\ShrutiHangmanGame')

#import word list
from words import word_list

#Import Module to play hangman game
from PlayGame import play

#Get word from list randomly
def get_word():
    word = random.choice(word_list)
    return word.upper()

#Start the execution 
def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()