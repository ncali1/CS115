from cs115 import *
import random

##def play():
##    print('Welcome!')
##    secret = random.ranint(1, 100)
##    num_guesses = 0
##    user_guess = 0
##    while True:
##        user_guess = int(input('Enter your name:'))
##        num_guesses += 1
##        if user_guess == secret:
##            print('You got it in', num_guesses, 'guess(es)!')
##        elif user_guess > secret:
##            print('Too High')
##        else:
##            print('Too Low')
##        print('Thanks for playing!')
##play()


def factorial(n):
    result = 1
    for n in range(1, n+1):
        result = result * n
    return res


def fib(n):
    x = 0
    y = 1
    z = 0
    for n in range(1, n+1):
        z = x + y
        x = y
        y = z
        return x



def printBoard(board):
    board = printBoard[0]+ printBoard[0][1] + printBoard[0][2]
    print('board')
        
