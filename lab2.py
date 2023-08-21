# I pledge my honor that I have abided by the Stevens Honor System.

from cs115 import *


def dot(L, K):
    if L==[] or K==[]:
        return 0
    return L[0] * K[0] + dot(L[1:], K[1:])
        
def explode(S):
    if S=="":
        return []
    return [S[0]] + explode(S[1:])

def ind(e, L):
    if L == [] or L == "":
        return 0
    if e == L[0]:
        return 0
    else:
        return 1 + ind(e, L[1:])

def removeAll(e, L):
    if L == []:
        return []
    if e == L[0]: 
        return removeAll(e, L[1:])
    return [L[0]] + removeAll(e, L[1:])

def myFilter(f, L):
    if L == []:
        return []
    if f(L[0]) == True:
        return [L[0]] + myFilter(f,L[1:])
    return myFilter(f,L[1:])
        
def even(X):
    if X % 2 == 0 :
        return True
    else:
        return False

def deepReverse(L):
    if L == []:
        return []
    if isinstance(L[0], list):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    else:
       return deepReverse(L[1:]) + [L[0]]

def odd(x):
    if x%2 == 1
        












