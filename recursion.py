from cs115 import *

# exercises Sept 11, 2019
# recursion on a list L, ingredients:
# L==[]  L[0]  L[1:]

L0 = [9,11,2019]
L1 = ["the", "arc", "of", "the", "moral", "universe", "is", \
      "long", "but", "it", "bends", "towards", "justice"]

def myLen(L):
    if L==[]: return 0
    else: return 1 + myLen(L[1:])
def test_myLen():
    print (myLen(L0) == 3)

def mySum(L):
    '''assume L is a list of numbers; return its sum'''
    return None
def test_mySum():
    print (mySum(L0) == 2039)

def maxLen(L):
    '''assume L is a nonempty list of strings; return len of longest'''
    if len(L) == 1:
        return len(L[0]) 
    else:
        return maxLen(L[0]),maxLen([1:])
        

def test_maxLen():
    print (maxLen(L1) == 8)

def rep(n, x):
    if n == 0:
        return []
    else:
        return [x] + rep(n-1, x)

def rev(L):
    if L == []:
        return []
    else: return rev(L[1:]) + [L[0]]

def hanoi(n):
    if n == 1:
        return 1
    return 2* hanoi(n-1) + 1 
