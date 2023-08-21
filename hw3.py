'''
Created on 9/20/2019
@author:   Nicholas Cali
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Hw 3

'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#your code goes here
def giveChange(amount, coins):
    '''Returns the best list of coins with the amount of each to make the amout given.'''
    if amount == 0:
        return [0,[]]
    elif coins == []:
        return [float("inf"),[]]
    elif coins[0] > amount:
        return giveChange(amount, coins[1:])
    result = giveChange(amount - coins[0], coins)
    use = [1 + result[0],[coins[0]] + result[1]]
    lose = giveChange(amount, coins[1:])
    if (use[0] < lose[0]):
           return use
    return lose
 
# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def letterScore(letter, scoreList):
    '''Assuming letter is a letter and scorelist is a list, and other letters have a scrabble score, returns the score of the letter within the scorelist'''  
    if scoreList == []:
        return 0
    if letter == scoreList[0][0]:
        return scoreList[0][1]
    return letterScore(letter, scoreList[1:])

def wordScore(S, scorelist):
    '''Assuming s is a string and scorelist is a list containing each letter and its score, returns the sum of the letter and the score of the word.'''
    if S=='':
        return 0
    return letterScore(S[0], scoreList) + wordScore(S[1:], scoreList)


def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]'''
    def letterScore(letter, scoreList):
        '''Assuming letter is a letter and scorelist is a list, and other letters have a scrabble score, returns the score of the letter within the scorelist'''  
        if scoreList == []:
            return 0
        if letter == scoreList[0][0]:
            return scoreList[0][1]
        return letterScore(letter, scoreList[1:])

    def wordScore(S, scorelist):
        '''Assuming s is a string and scorelist is a list containing each letter and its score, returns the sum of the letter and the score of the word.'''
        if S=='':
            return 0
        return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

    if dct ==[]:
        return []
    return [[dct[0], wordScore(dct[0], scores)]] + wordsWithScore(dct[1:], scores)
    



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    if n == 0 or L == []:
        return []
    return [L[0]] + take(n - 1, L[1:])
    



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if n == 0:
        return L
    if L == []:
        return []
    else:
        return drop(n-1, L[1:])
