#
# life.py - Game of Life lab
#
# Name: Nicholas Cali
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#

import random
import sys
import random

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row



def createBoard(width, height):
    '''returns a 2nd array with "height" rows and "width" cols'''
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A


def diagonalize(width, height):
    ' creates as empty board and then modifies it so that it has a diagonal strip of "on cells.'''
    A = createBoard( width, height)
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A



def printBoard(A):
    ''' this function prints the 2d list of lists
        A without spaces (using sys. stdout.write)
    '''
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')


def innerCells(w, h):
    ''' returns 2nd array of all live cells- with the value of 1- except for a one-cell-wide border of empty cells
    '''
    A = createBoard(w, h)
    for row in range(1, h-1):
        for col in range(1, w-1):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 1     
    return A
            
            
    
def randomCells(w, h):
    ''' returns an array of randomly-assigned 1's and 0's execept that the outer edge of the array is still completely empty as in case of innerCells
    '''
    A = createBoard(w,h)
    for row in range(1, h-1):
        for col in range(1, w-1):
            if row == col:
                A[row][col] = random.choice([0,1])
            else:
                A[row][col] = random.choice([0,1])
    return A


def copy(A):
    '''copies the old board'''
    B = createBoard(len(A), len(A[0]))
    for row in range(len(A)):
        for col in range(len(A[0])):
            B[row][col] = A[row][col]
    return B
                
     
def innerReverse(A):
    '''changes one generation of cells to a new one'''
    B = copy(A)
    for row in range(1, len(A)-1):
        for col in range(1, len(A[0])-1):
            if B[row][col] == 0:
                B[row][col] = 1
            elif B[row][col] == 1:
                B[row][col] = 0
    return B

def countNeighbors(row, col, A):
    '''returns the number of live neighbors for a cell in the board A at
       a particular row and col
    '''
    n = 0
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if A[r][c] == 1:
                n = n + 1
    if A[row][col]==1:
        n= n - 1
    return n

def next_life_generation(A):
    ''' makes a copy of A and then advanced one generation of Conway's game
        of life within the "inner cells" of that copy. The outer edge always
        stays 0
    '''
    B = copy(A)
    for r in range(1,len(A)-1):
        for c in range(1, len(A[0])-1):
            n = countNeighbors(r, c, A)
            #print(n)
            if n>3 or n<2:
                B[r][c] = 0
            elif n == 3:
                B[r][c] = 1
            else:
                B[r][c] = A[r][c]
    return B
    



        
