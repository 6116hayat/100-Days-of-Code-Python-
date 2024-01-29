# Data Types

'''
## when we do not know the type the data
char = input('Type your word \n')
print(type(char))
'''

'''
## Converting the datatype
item1 = float(input('Input the price for item 1 \n'))
print(item1)
item2 = int(input('Input the price for item 2 \n'))
print(item2)
total = item1 + item2
print('Your total is =' + str(total))
'''

## Adding the individual digits of the number

## AI Generated Code (This code prints the sum of individual digits, with any input)
'''
num = int(input('Enter your digit'))
print('Your digit was:' + str(num))

def getSum(num):
    sum = 0
    while num != 0:
        sum += num % 10
        num //= 10
    return sum

print('The digit was:' +str(num) + ' And the sum is:' + str(getSum(num)))
'''

## Course Code (This code prints only the sum of two digit number)
'''
number = input('Enter your desired number \n')
first_digit = (number[0])
second_digit = (number[1])
result = int(first_digit) + int(second_digit)
print(result)
'''

## Mathematical Operators
'''
P - parentheses ()
E - Exponents **
M - Multiplication *
D - Division / 
A - Addition + 
S - Subtraction -
'''

## BMI Calculator
'''
## BMI formula 
BMI = Weight (kg ) / Height * Height
'''
'''
weight = float(input('Enter the weight in Kg: \n'))
height =  float(input('Enter the height in Metres: \n'))
BMI = float (weight / (height * height))
print(BMI)
'''

## String manipulation
'''
score = 0
height = 1.8
isWinning = True

## f-string is a special case, where strings gets converted automatically
print(f'your score is {score}, your height is {height}, you are winning is {isWinning}')
'''

## Calculating numbers of days, weeks, months left until user is 90 years old
'''
currentAge = int(input('Enter your Current age: \n'))
yearsLeft = 90 - (currentAge)
# Months Left
monthLeft = 12 * (yearsLeft)
# Weeks Left
weekLeft = 4.3 * (monthLeft)
# Days Left
dayleft = 7 * (weekLeft)

print(f'Years Left: {yearsLeft}, Months Left: {monthLeft}, Weeks Left: {weekLeft}, Days Left: {dayleft}')
'''

## Tip Calculator
print('WELCOME TO THE TIP CALCULATOR:')
totalBill = float(input('Enter the Total Amount \n'))
percent = float(input('Enter the Percentage for tip: 10, 12 or 15 \n'))
people = int(input('Enter the number of people \n'))
sum = 0
split = 0
if percent == 10:
    sum = (totalBill * 0.10) + totalBill
    split = sum / people
    # print('Each person should pay:'+ str(split))
elif percent == 12:
    sum = (totalBill * 0.12) + totalBill
    split = sum / people
    # print('Each person should pay:'+ str(split))
elif percent == 15:
    sum = (totalBill * 0.15) + totalBill
    split = sum / people
    # print('Each person should pay:'+ str(split))
finalAmount = round(split, 2)
print(f'Each person should pay :{finalAmount}')


