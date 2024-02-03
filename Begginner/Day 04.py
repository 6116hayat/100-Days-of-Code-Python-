## Randomisation
import random

# priting random numbers
'''
random_int = random.randint(1,10)
print(random_int)
'''

# Module
'''
Module are like the classes in Java, where the different code can be stored for various code
'''
# printing random float numbers between 0 and 5
'''
random_float = random.random() * 5
print(random_float)
'''
# Coin Toss Exercise
'''
1 = Heads , 0 = Tails
'''
'''
print('Welcome to the Coin Toss Program:')
user_input =  input('Do you want the computer to toss a coin for you: Y or N \n')

coin_toss = random.randint(0,1)
# print(coin_toss)
if user_input == 'Y':
    if coin_toss == 0:
        print('Your coin toss results is Tails')
    elif coin_toss == 1:
        print('Your Coin Toss results is Heads ')
elif user_input == 'N':
    print('Sorry no coin was tossed for you ')
'''

## Lists
'''
list is a type of data structure, where we store data using list

code syntax:
list = [item1, item2]
'''
# creating an example of list
'''
fruits = ['Apple', 'Mango', 'Peach']

print(fruits[0]) # printing with index of list
fruits.extend(['Pear','Watermelon'])
print(fruits)
'''
# Exercise for paying bill as russian roulette
'''
Aman, Umar, Sujeet, Sivam
'''
'''
# My Logic
names =  ['Aman', 'Umar', 'Sujeet', 'Sivam']
num = random.randint(0, 3)

print(num)
print(f'The person who will pay is {names[num]}')
'''

## Rock, Paper And Scissors Game
'''
# Rock Paper Scissors ASCII Art

# Rock
print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
'''

print("Welcome to the ROCK-PAPER-SCISSORS Game")
print('0 = ROCK, 1 = PAPER, 2 = SCISSORS')

# saving ASCII art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# printing game images
game_images = [rock, paper, scissors]

user_choice = int(input('Make your choice \n'))

# fixing the bug
if user_choice < 2:
    print('User Chose')
    print(game_images[user_choice])

'''
if user_choice == 0:
    print("You chose Rock")
    print(rock)
elif user_choice == 1:
    print("You Chose Paper")
    print(paper)
elif user_choice == 2:
    print("You Chose Scissors")
    print(scissors)
'''

computer_choice = random.randint(0,2)
if user_choice < 2:
    print('Computer Chose')
    print(game_images[computer_choice])

'''
if computer_choice == 0:
    print("Computer chose Rock")
    print(rock)
elif computer_choice == 1:
    print("Computer Chose Paper")
    print(paper)
elif computer_choice == 2:
    print("Computer Chose Scissors")
    print(scissors)
'''

# if else logic
# user winning
if (user_choice == 0) and (computer_choice == 2):
    print('You won!! ')
if (user_choice == 1) and (computer_choice == 0):
    print('You won !!')
if (user_choice == 2) and (computer_choice == 1):
    print('You won !!')

# computer winning
if (computer_choice == 0) and (user_choice == 2):
    print('Computer Won!!')
if (computer_choice == 1) and (user_choice == 0):
    print('Computer Won!!')
if (computer_choice == 2) and (user_choice == 1):
    print('Computer Won!!')

# Draw
if (user_choice == 0) and (computer_choice == 0):
    print('Draw')
if (user_choice == 1) and (computer_choice == 1):
    print('Draw')
if (user_choice == 2) and (computer_choice == 2):
    print('Draw')

# fixing the bug
if user_choice > 2:
    print('Hey Smart ass!!, Cant you read, Choose number between 0-2')
    print('Now Re-run the program and choose correct numbers')
    print('If not, then shut the program!!')