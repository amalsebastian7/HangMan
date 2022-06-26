'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
from dataclasses import replace
import random

class Hangman:

    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.num_lives = 3
        self.word = list(random.choice(self.word_list))
        self.list_letter=[]
        self.word_guessed =['_']*len(self.word)
        self.num_letters=len(set(self.word))

        print(f"The mystery word has {len(self.word)} characters")
        print(f"{self.word_guessed}")
        pass

    def check_letter(self, letter) -> None:

        while self.num_lives >0:
            if letter in list(self.word):
                self.num_letters-=1
                index= [i for i,L in enumerate (self.word) if L == letter]
                self.word_guessed[index]=letter
                print(f"The word is :{self.word_guessed}")
            else:
                self.num_lives -=1
                print(f"The letter guessed is wrong")
            break
        pass

    def ask_letter(self):
         while True:
            letter =input("Enter a letter: ").lower()
            if len(letter) != 1:
                    print(f"Enter just a character,Please: ")
                    continue
            elif letter in self.list_letter:
                    print(f"{letter}  already tried")
                    continue
            self.list_letter.append(letter)
            self.check_letter(letter)
            break
    pass


def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    game.ask_letter()

if __name__ == '__main__':
    word_list = [ "Execution","Tea","Supposedly", "there" ,"are" ,"over" ,"one","million", "words" ,"in", "the" ,"English" ,"Language"   ]
    play_game(word_list)
# %%
