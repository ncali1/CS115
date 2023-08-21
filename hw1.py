from cs115 import *
import math

#I pledge my honor that I have abided by the Stevens Honor System

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1) 

def add(x,y):
    return x+y

def mean(L):
    return sum(L) / len(L)

def div(k):
    return 42 % k == 0

def divides(n):
    def div(k):
        return n % k == 0
    return div

# I didn't do the prime function. I don't even know where to start.    
    
