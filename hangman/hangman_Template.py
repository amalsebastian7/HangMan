import random

#create class 
class Hangman:
#defining all initializations

    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.num_lives = 3
        self.word = list(random.choice(self.word_list).lower())
        self.list_letter=[]
        self.word_guessed =['_']*len(self.word)
        self.num_letters=len(set(self.word))

        print(f"The mystery word has:  {len(self.word)} characters")
        print(f"{self.word_guessed}")
        pass

    def check_letter(self, letter) -> None:
        if letter in list(self.word):
            self.num_letters -= 1
            for i, L in enumerate(self.word):
                if L == letter:
                    self.word_guessed[i] = L
            print(f"Yes {letter} is in the word")
            print(f"Your word so far : {self.word_guessed}")
        else:
            self.num_lives -=1
            print(f"The letter guessed is wrong,you have :  {self.num_lives} lives left")
            print(f"Your word so far : {self.word_guessed}")
        pass

    def ask_letter(self):
        while True:
            letter =input("Enter a letter: ").lower()
            if len(letter) != 1:
                    print(f"Enter just a character,Please: ")
                    continue
            elif letter in self.list_letter:
                    print(f"{letter}  already tried")
                    self.list_letter.append(letter) 
                    continue 
            else:
                self.check_letter(letter)
            break
        return letter 
    pass


def play_game(word_list):
    game = Hangman(word_list, num_lives=5) 
    while game.num_lives > 0:
        game.ask_letter() 
        if game.num_lives == 0:
            print(f"The word is : {game.word}")
            print(f"You lost")
            break
        elif game.num_letters == 0: 
            print("Congratulations, you won!") 
            break 
if __name__ == '__main__':
    word_list = [ "Execution","Tea","Supposedly", "there" ,"are" ,"over" ,"one","million", "words" ,"in", "the" ,"English" ,"Language"]
    play_game(word_list)

word = 'apple'
num_letters=len(set(word))
print(num_letters)



























'''
Previous code:

from dataclasses import replace
import random

class Hangman:

    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.num_lives = 3
        self.word = list(random.choice(self.word_list).lower())
        self.list_letter=[]
        self.word_guessed =['_']*len(self.word)
        self.num_letters=len(set(self.word))

        print(f"The mystery word has:  {len(self.word)} characters")
        print(f"{self.word_guessed}")
        pass

    def check_letter(self, letter) -> None:

        while self.num_lives >0:
            if letter in list(self.word):
                self.num_letters-=1
                for i, L in enumerate(self.word):
                    if L == letter:
                        self.word_guessed[i] = L
                print(f"The word is : {self.word_guessed}")
                self.ask_letter()
            else:
                self.num_lives -=1
                print(f"The letter guessed is wrong,you have :  {self.num_lives} lives left")
                if self.num_lives == 0:
                    print(f"The word is : {self.word}")
                    print(f"You lost")
                    break
                self.ask_letter()
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
            if self.num_lives != 0:
                self.check_letter(letter)
            else:
                print(f"The word is : {self.word}")
                print(f"You lost")
                break
            break
    pass


def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    game.ask_letter()
    if game.word_guessed.count('_') == 0:
        print("Congratulations, you won!")

if __name__ == '__main__':
    word_list = [ "Execution","Tea","Supposedly", "there" ,"are" ,"over" ,"one","million", "words" ,"in", "the" ,"English" ,"Language"   ]
    play_game(word_list)

    '''
# %%
