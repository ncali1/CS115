'''
Nicholas Cali
'''


# Exercise on binary search

# This version is made to fit the search interface
# used in insertionExercise.py.
# The best way to do insertion sort is to use the insertV2
# function, with binary search instead of linear search.

#######################################################
# Search a sorted list segment.
# The idea is to use two variables, j and hi,
# narrowing the search range with j on the low
# side and hi on the high side.
# with invariant L[0:j] <= x and x < L[hi:i] and j<=hi
# Each iteration should decrease hi - j .
#######################################################

def binsearch(L, i, x):
    '''Assuming L[0:i] is sorted and 0 <= i <= len(L),
       return j such that 0 <= j <= i and L[0:j] <= x < L[j:i].'''
    j = 0
    k = i
    while j != x:
        if L[0:i] <= k:
            return k
        elif x < L[k:i]:
            return x
        return hi - j
    return hi
   
        
    
    pass # to do


def testBinSearch():
    # in middle
    assert binsearch([0,2,4,6,3,0,5], 3, 3) == 2
    # near start
    assert binsearch([1,2,3,4,1], 3, 1) == 1
    # at start 
    assert binsearch([1,2,3,0], 3, 2) == 2
    # at end
    assert binsearch([1,3,5,5], 3, 6) == 3
    assert binsearch([1,3,5,5], 4, 6) == 4
    # at end, short list 
    assert binsearch([0], 1, 5) == 1
    assert binsearch([3,4], 2, 5) == 2
    # at start, short list
    assert binsearch([5], 1, 2) == 0
    assert binsearch([3,4], 2, 1) == 0

#############################################
# Here's how to find an element of a list,
# using binary search.
#############################################

def find(L,x):
    '''For sorted L, return i such that L[i] == x,
       or -1 if x does not occur in L.'''
    i = binsearch(L, len(L), x) 
    if i == 0 or L[i-1] != x:
        return -1
    else:
        return i-1

def testFind():
    # at start
    assert find([3,6,20], 3) == 0
    # at end
    assert find([2,6,20], 20) == 2
    # in middle, odd position
    assert find([2,6,20,25,30], 25) == 3
    # in middle, even position
    assert find([2,6,20,25,30], 20) == 2
    # in middle, odd position, even list
    assert find([2,6,20,25], 25) == 3
    # in middle, even position, even list
    assert find([2,6,20,25], 20) == 2
    
