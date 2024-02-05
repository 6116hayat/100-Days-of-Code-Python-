## Loops
'''
it helps to iterate over a code, over and over
'''
# import random

## for loops
'''
code syntax
for items in list_of_items
    Do something to each item
'''

'''
fruits =['Apple', 'Peach','Pear']
for fruit in fruits:
    print(fruit)
    print(fruit + 'Pie')

    print(fruit)

print(fruits)
'''


# Average Height Exercise
'''
Average height data : 180 124 165 173 189 169 146
Avg Height 2nd Data : 156 178 165 171 187
'''

# Course Logic
'''
student_heights = (input(' Input a list of student heights \n')).split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)


## for loop logic
total_height = 0
count = 0

for height in student_heights:
    total_height += height
    count += 1
print(total_height)

print(f'Total: {total_height}')
print(f'Count: {count}')

avg_height = (total_height)/count
print(f'The Average height : {avg_height}')
'''

# Highest Scores
'''
highest scores data: 78 65 89 86 55 91 64 89
'''

'''
# this is the  default code, to help our code work
student_scores = (input(' Input a list of student scores \n')).split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# for loop logic
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
        
print(f'The highest scores in the class: {highest_score}')
'''

## Range function
'''
code syntax
for number in range (a,b)
    print(number)
'''
'''
# example
for number in range(0, 11,):
    print(number)
'''

# adding numbers from 1 to 100
'''
total = 0
for number in range(1, 101):
    total += number
print(total)
'''

# Exercise to solve the sum of all the even numbers from 1 to 100
'''
total = 0
for number in range(0, 101, 2):
    total += number
    print(number)
print(total)
'''

# Fizz Buzz Exercise
# program logic
'''
print number from 1 to 100
When the number is divisible by 3, then instead of printing the number it should print 'FIZZ'
When the number is divisible by 5, then instead of printing the number it should print 'BUZZ'
When the number is divisible by 3 and 5 both, then instead of printing the number it should print 'FIZZ-BUZZ'
'''

'''
for number in range(1, 101):
    if (number % 3 == 0) and (number % 5 == 0):
        # Checking if the number is divisible by 3 and 5
        print('FIZZ-BUZZ')
    elif number % 3 == 0:
        # checking if the number is divisible by 3
        print('FIZZ')
    elif (number % 5 == 0):
        # checking if the number is divisible by 5
        print('BUZZ')
    else:
        print(number)
'''

## Exercise: Password Generator

'''
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('WELCOME TO THE PASSWORD GENERATOR')
user_letters = int(input('How many letters for your password \n'))
user_numbers = int(input('How many numbers for your password \n'))
user_symbols = int(input('How many symbols for your password \n'))
'''

'''
Easy-Level
e.g. 4 letter, 2 symbol, 2 number = JduE&!91

Hard-Level
4 letter, 2 symbol, 2 number = g^2jk8&P
'''
print('Easy Level')
'''
password =''

for char in range(1, user_letters+1):
    password += random.choice(letters)

for char in range(1, user_letters+1):
    password += random.choice(numbers)

for char in range(1, user_letters+1):
    password += random.choice(symbols)

print(password)
'''

'''
print('Hard-Level')
password_list = []

for char in range(1, user_letters+1):
    password_list.append(random.choice(letters))

for char in range(1, user_letters+1):
    password_list += random.choice(numbers)

for char in range(1, user_letters+1):
    password_list += random.choice(symbols)

print(password_list)

random.shuffle(password_list)
print(f'The suffled password {password_list}')

password =''
for char in password_list:
    password += char
print(f'Your password is {password}')
'''