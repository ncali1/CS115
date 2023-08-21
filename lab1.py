I pledge my honor that I have abided by the Stevens Honor System

from cs115 import *
import math

def inverse(n):
    return 1/n


def e(n):
    return reduce(add, map(inverse, map(math.factorial, range (0,n+1)))) 

def add(x,y):
    return x+y    

def error(n):
    return abs(math.e-e(n))

