#Guess my number
#7/15/2018
#CTI-110 P5HW2 - Random Number Guessing Game
#Krystal Lewis
#


import random

num = random.randint( 1 , 100 )
flag = True
guess = "0"


print('Guess my number 1-100: ', end = ' ')

while flag == True:
    guess = input()
    if not guess.isdigit():
        print('Invalid! Enter only digits 1-100')
        break
    elif int(guess) < num:
        print('Too low, try again: ', end = ' ')
    elif int(guess) > num:
        print('Too high, try again: ', end = ' ')
    else:
        print('Correct... My number is ' + guess)
        flag = False


