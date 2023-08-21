from cs115 import *

def member(x, L):
    if L==[]:
        return False
    elif L[0]== x:
        return True
    else:
        return member(x,L[1:])

def map(f, L):
    if L==[]:
        return []
    else:
        f(L[0])
    return [f(L[0])] + map(f,L[1:])

def odd(x):
    return x % 2==1

def prime(n):
    possibleDivisors = range(2,n)
    divisors = filter(lambda X: n % X == 0, possibleDivisiors)
    return len(divisors) == 0
