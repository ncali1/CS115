'''
Created on  September 17, 2019
@author:     Nicholas Cali
Pledge:   I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']
scorelist = []

# Implement your functions here.

def scoreList(Rack):
    '''Returns all the words that can be made from the the global variable, Dictionary from the list Rack.'''

    if Rack==[]:
        return []
    return map(lambda word: [word, wordScore(word, scrabbleScores)], listOfWords(Dictionary, Rack))

def isPossible(word, Rack):
    '''Returns True assuming the word is a string and Rack is a list of letters and returns False if it's not.'''
    if word =="":
        return True
    if word[0] in Rack:
        return isPossible(word[1:], Remove(word[0], Rack))
    return False

def listOfWords(Dict, Rack):
    '''Return all words in dictionary that can be made via the letters in Rack.'''
    return filter(lambda word: isPossible(word, Rack), Dict)

def letterScore(letter, scoreList):
    '''Assuming letter is a letter and scorelist is a list and that other letters have a scrabble score, returns the score of the letter within the scorelist.'''
    if scoreList==[]:
        return 0
    if letter==scoreList[0][0]:
        return scoreList[0][1]
    return letterScore(letter, scoreList[1:])

def wordScore(S, scoreList):
    '''Assuming s is a string and scorelist is a list containing each letter and its score, returns the sum of the letter and the score of the word.''' 
    if S=='':
        return 0
    return letterScore(S[0], scoreList)+wordScore(S[1:], scoreList)

def bestWord(Rack):
    '''Returns the word with the highest score in Rack with its score.'''
    scorelist=scoreList(Rack)
    if scorelist == []:
        return ["",0]
    return reduce(lambda x,y: x if x[1] > y[1] else y, scorelist)

def Remove(letter, Rack):
    ''' Assuming the letter is a string and Rack is a list of letters, returns Rack without the first letter.'''
    if letter =='':
        return []
    if Rack[0]== letter:
        return Rack[1:]
    return [Rack[0]]+ Remove(letter, Rack[1:])



        

