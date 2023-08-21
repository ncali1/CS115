from cs115 import *

# I pledge my honor that I have abided by the Steven Honor System

def pascal_add(L):
    '''Adds up the numbers of the current row in pascal's triangle'''
    if L == []:
        return []
    if len(L) == 1:
        return [1]
    return [L[0] + L[1]] + pascal_add(L[1:])


def pascal_row(n):
    ''' Returns the list of the numbers of the called row in Pascal's triangle.'''
    if n == 0:
        return [1]
    if n == 1:
        return [1,1]
    return [1] + pascal_add(pascal_row(n-1))
def pascal_triangle(n):
    '''Displays the row # with its values up to the called row number.'''
    if n == 0:
        return [1]
    if n == 1:
        return [[1], [1, 1]]
    return pascal_triangle(n-1) + [pascal_row(n)]



def test_pascal_triangle():
    assert pascal_triangle(0) == [1]
    assert pascal_triangle(1) == [1, [1, 1]]
    assert pascal_triangle(3) == [1, [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    assert pascal_triangle(5) == [1, [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    


def test_pascal_row():
    assert pascal_row(1) == [1, 1]
    assert pascal_row(2) == [1, 2, 1]
    assert pascal_row(3) == [1, 3, 3, 1]
    assert pascal_row(4) == [1, 4, 6, 4, 1]
                            
    
