#I pledge my honor that I have abided by the Stevens Honor System.

from cs115 import *

def change(amount, coins):
    if amount==0:
        return 0
    elif coins==[]:
        return float("inf")
    if amount <0:
        return float("inf")
    use = change(amount-coins[0], coins) + 1
    lose = change(amount, coins[1:])
    return min(use, lose)
     
    
