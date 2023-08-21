from cs115 import *


def exp(n,k):
    if k == 0:
        return 1
    else:
        return n * exp(n, k-1)

def expfast(n,k):
    if k == 0:
        return 1
    elif k % 2 ==0:
        t = expfast(n, k//2)
        return t*t
    return n * expfast(n,k-1)

def testExp():
    assert exp(3,5) == 3**5
    assert exp(2,0) == 2**0
    assert expfast(3,5) == 3**5
    assert expfast(2,0) == 2**0

def exptail(n, k):
    def ext(accumulator, n, k):
        if k == 0:
            return accumulator
        else:
            return ext(n * accumulator, n, k-1)
        return ext(1, n, k)
