from cs115 import *

def sieve(L):
    if L==[]:
        return []
    else:
        return [L[0]] + sieve(filter(lambda X:X % L[0] !=0, L[1:]))
    

def subset(target, L):
    if target==0:
        return True
    elif L==[]:
        return False
    elif L[0]> target:
        return subset(target, L[1:])
    else: #L[0] <= target
        use = subset(target-L[0], L[1:])
        lose = subset(target, L[1:])
        return use or lose
    
