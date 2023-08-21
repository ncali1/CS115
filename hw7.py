'''
Created on 10/21/2019
@author:   Nicholas Cali
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Hw 7
'''
import math

# Each row has (x,y,carry-in) : (sum,carry-out)
FullAdder =\
{ ('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }


def numToBaseB(N, B):
    '''returns a string representing the number N in base B'''
    def numToBaseBhelper(N, B, k):
        '''comuptes the intial value of n and converst to the string'''
        if k == 0:
            return "0"
        if N==0:
            return ""
        else:
            return numToBaseBhelper(N//B, B, k) + str(N%B)
    return numToBaseBhelper(N, B, N)

def baseBToNum(S, B):
    '''converts a base to number'''
    if S == "":
        return 0
    else:
        return baseBToNum(S[0:-1], B) * B + int(S[-1])

def baseToBase(B1, B2, SinB1):
    '''returns a string representing the same number in Base B2'''
    return numToBaseB(baseBToNum(SinB1, B1), B2)



def add(S1, S2):
    '''adds two binary strings and returns one string'''
    return numToBaseB(baseBToNum(S1, 2) + baseBToNum(S2, 2),2)


def addB(S1, S2):
    ''' adds up one column of the binary strings'''
    val = len(S1)-len(S2)
    if val > 0:
        S2 = "0" * val + S2
    if val < 0:
        S1 = "0" * abs(val) + S1
    def addBHelper(S1, S2, carry):
        ''' adds remaining strings with adder''' 
        if S1 == '':
            if carry == '0':
                return ''
            return '1'
        return addBHelper(S1[:-1], S2[:-1], FullAdder[(S1[-1], S2[-1], carry)][1]) + FullAdder[(S1[-1], S2[-1], carry)][0]
    return addBHelper(S1, S2, '0')
    
    
    
