
from dataclasses import replace
import random

class Hangman:
   
    def __init__(self, word_list, num_lives):
        # TODO 2: Initialize the attributes as indicated in the docstring

        # TODO 2: Print two message upon initialization:
        # 1. "The mystery word has {len(self.word)} characters" (The number of letters is NOT the UNIQUE number of letters)
        # 2. {word_guessed}


    def check_letter(self, letter) -> None:

        # TODO 3: Check if the letter is in the word. TIP: You can use the lower() method to convert the letter to lowercase
        # TODO 3: If the letter is in the word, replace the '_' in the word_guessed list with the letter
        # TODO 3: If the letter is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
        # TODO 3: If the letter is not in the word, reduce the number of lives by 1
        # Be careful! A letter can contain the same letter more than once. TIP: Take a look at the index() method in the string class.
        
     pass


    def ask_letter(self):
        # TODO 1: Ask the user for a letter iteratively until the user enters a valid letter

        while True:
            letter=input("Enter a letter")
                if len(letter)!=1:
                    print(f"Enter just a character,Please")
                    continue
                elif letter in self.list_letter:
                    print(f"{letter} already tried")
                    continue
                self.list_letter.append(str.lower(letter))
                self.check_letter(letter)
                break

        # TODO 1: Assign the letter to a variable called `letter`
        # TODO 1: The letter has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character"
        # TODO 2. It has to be a letter that has not been tried yet. Use the list_letters attribute to check this. If it has been tried, print "{letter} was already tried".
        # TODO 3: If the letter is valid, call the check_letter method
        


def play_game(word_list):
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)
    game.ask_letter()
    # TODO 1: To test this task, you can call the ask_letter method
    # TODO 2: To test this task, upon initialization, two messages should be printed 
    # TODO 3: To test this task, you call the ask_letter method and check if the letter is in the word
    
    # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    # If the user guesses the word, print "Congratulations, you won!"
    # If the user runs out of lives, print "You ran out of lives. The word was {word}"

    pass


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
