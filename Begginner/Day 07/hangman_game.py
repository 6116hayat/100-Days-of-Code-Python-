# HANGMAN GAME
import random


'''
# My-Logic
word_lst = ['balloon', 'rocket', 'clown', 'sniper']


chosen_wrd =  random.choice(word_lst)
print(chosen_wrd)

# TODO 1
display =[]
for blnk in range(len(chosen_wrd)):
    display.append("_")
print(display)


gues = input("Guess the letter ").lower()

# TODO 2
for leter in chosen_wrd:
    if leter == gues:
        
    else:
        print("Choose other leter....")

print(display)
'''


# Course Logic

#priting the logo
from Hangman_art import logo
print(logo)

end_of_game = False

from Hangman_Words import word_list
chosen_word = random.choice(word_list)

# Cheat - Code
print(f'The choosen word {chosen_word}')

# tracking lives of player
lives = 0

# Creating Blanks
display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)

# creating a while loop
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    from turtle import clear
    clear()

    if guess in display:
        print(f'You have already guessed the word, I wont give extra points {guess}')

# Hardest Part.....
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Writing at new indentation, helps us to loop through the code at one more time
    if guess not in chosen_word:
        print(f'You have guessed {guess}, that is not in the word, you lose life')
        lives += 1
        if lives == 6:
            end_of_game = True
            print("You lose.")

    print(display)

    if '_' not in display:
        end_of_game = True
        print("You win.")

    from Hangman_art import HANGMANPICS
    print(HANGMANPICS[lives])