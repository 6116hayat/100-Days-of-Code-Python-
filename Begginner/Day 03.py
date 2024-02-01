## If else statements
'''
print('WELCOME TO THE ROLLER COASTER ')
height = int(input('What is your Height in cm ? \n '))

# if-else Flow
if height > 120:
    print('You Can Ride the Roller Coaster!!!')
elif 0 < height < 120:
    print('Grow Your Height Bud !!!')
else:
    print('Dont play with me lad, by putting -ve height')
'''

## Exercise: If the number is Odd or Even
'''
number = int(input('Enter your number \n'))
modulo = number % 2
if modulo == 0:
    print('The number is EVEN')
else:
    print('The Number is ODD')
'''

## Nested if else statements
'''
# Program for park entry And can ride a roller coaster or not:
print('WELCOME TO THE AMUSEMENT PARK')
age = int(input('Enter your Age: \n'))
height = int(input('Enter your height \n'))

if age > 18:
    print('Your ticket price is 800 Rupees')
    if height > 120:
        print('You Can Ride the Roller Coaster!!!')
    elif 0 < height < 120:
        print('Sorry Sir You Cannot ride the roller coaster  !!!')
elif 12 < age < 18:
    print('Your ticket price is 550')
elif 0 < age < 12:
    print('Your ticket price is 400')
else:
    print('Dont Fool me with putting a negative number')
'''

## Nested BMI 2.0
'''
Under 18.5 = under weight
Over 18.5 and below 25 = normal weight
Over 25 and below 30 = over weight
over 30 but below 35 = obese
Above 35 clinically obese
'''

'''
weight = float(input('Enter the weight in Kg: \n'))
height = float(input('Enter the height in Metres: \n'))
BMI = round(float(weight / (height * height)))

if BMI < 18.5:
    print('You are Under weight')
elif 18.5 < BMI < 25:
    print('You are normal weight')
elif 25 < BMI < 30:
    print('You are over weight')
elif 30 < BMI < 35:
    print('You are obese')
elif 35 < BMI:
    print('You are Clinically Obese')
'''

## Leap Year Exercise
'''
year = int(input('Enter your desired Year \n'))

if year % 4 == 0:
    print(f'{year} is a leap year, And it has 366 days')
else:
    print(f'{year} is not a leap year, And it has 365 days')
'''

## Multiple if statement

'''
syntax
if condition 1:
    do A
if condition 1:
    do B
if condition 1:
    do C
'''

'''
# Writing a program to charge price for the photo clicked on the roller coaster
print('WELCOME TO THE AMUSEMENT PARK')
height = int(input('Enter your height \n'))

bill = 0

if height >= 120:
    print('You can ride the roller-coaster ')
    age = int(input('Enter your age \n'))
    if age < 12:
        print('Child tickets are  ₹450')
        bill = 450
    elif age <= 18:
        print('Youth tickets is  ₹550')
        bill = 550
    else:
        print('Adult tickets is  ₹800')
        bill = 800

    wantPhotos = input('Do you want Photos?? Y or N \n')
    if wantPhotos == 'Y':
        bill += 100
        print(f'You have charged extra for Photos, Your total bill is  ₹{bill}')
    if wantPhotos == 'N':
        print(f'You are not paying extra it is only ₹{bill} ')

else:
    print('You cannot ride the roller Coaster ')
    age = int(input('Enter your age \n'))
    if age < 12:
        print('Child tickets are  ₹450')
        bill = 450
    elif age <= 18:
        print('Youth tickets is  ₹550')
        bill = 550
    else:
        print('Adult tickets is  ₹800')
        bill = 800
'''

## Pizza Order Program
'''
print('Welcome to the Hayat-Pizza-Palace')
size = input('What size of pizza you want?? S, M or L \n ')
add_pepproni = input('Do you want pepproni?? Y or N \n')
extra_cheese = input('Do you want extra cheese? Y or N \n')

bill = 0

if size== 'S':
    # print('For small size of pizza, you will be charged ₹99')
    bill = 99
elif size == 'M':
    # print('For medium size pizza, you  will be charged ₹249')
    bill = 249
elif size == 'L':
    # print('For medium size pizza, you  will be charged ₹449')
    bill = 449

## for pepproni
if add_pepproni == 'Y':
    bill += 50
    # print(f'You are charged Extra ₹50 for pepproni, Your final bill is {bill}')
#else:
    # print('You wont be charged Extra...')

## for cheese
if extra_cheese == 'Y':
    bill += 50
    # print(f'You are charged Extra ₹50 for cheese, Your final bill is {bill}')
#else:
    #print('You wont be charged Extra...')

print(f'Your total bill is {bill}')
'''

## Logical Operators
'''
Types of logical operators
and 
or 
else 
'''

#Love Calculator Exercise
'''
lower() : this functions convert all the letter to lower
count() : this functions counts the letters in a string

Love Score 
# less than 10 or greater than 90
'your score is x, you go together like coke and mentos'
# between 40 and 50
'Your score is y, you are alright together'
# else
'Your score is z'
'''

'''
print('Welcome to the love calculator exercise')
yourName = input('Enter your name: \n')
theirName = input('Enter their name: \n')

combined = yourName + theirName
lowerCase = combined.lower()

# for true
t = lowerCase.count('t')
r = lowerCase.count('r')
u = lowerCase.count('u')
e = lowerCase.count('e')

true = t + r + u + e

l = lowerCase.count('l')
o = lowerCase.count('o')
v = lowerCase.count('v')
e = lowerCase.count('e')

love = l + o + v + e

love_score = int(str(true)) +int(str(love))

print(love_score)



if (love_score < 10) or (love_score >90):
    print(f'Your love is {love_score}, You are together Like Coke and Mentos')
elif (love_score >= 40) and (love_score <= 50):
    print(f'Your score is {love_score},You are alright together')
else:
    print(f'Your score is {love_score}')
'''

