from cs115 import *

def span(L):
    small = reduce(min,L)
    print("hi there")
    large = reduce(max,L)
    return large - small

L0 = [3, -1, 5]
L1 = range(27)
def gauss(N):
    return reduce(add, range(N+1))

def add(N,M):
    return N+M

def positive(n):
    if n > 0:
        return True
    else:
        return False

def increment(n):
    def add_to(k):
        return k + n
    return add_to

def inc_all(num, n):
    return map(increment(n),nums)

def test_inc_all():
    print(inc_all([], 2) == [])
    print(inc_all([1, 3, 5], 2) == [3, 5, 7])
    print(inc_all([-2, -1, 0, 1, 2], 10) == [-2, -1, 0, 1, 2])
    

def sqrs(xs):
    def sqr(n): return n*n
    return map(sqr, xs)

def f(n):
    return f(n)

def tower(n):
    if n == 0:
        return 1
    else:
        return 2 ** tower(n-1)

