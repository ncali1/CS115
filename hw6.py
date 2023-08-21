'''
Created on 10/10/2019
@author:   Nicholas Cali
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n % 2 != 0 


def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    return numToBinary(int(n/2)) + str(n%2)

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s== '':
        return 0
    return binaryToNum(s[:-1]) * 2 + int(s[-1])
    
def compress(s):
    '''return a string as a binary number'''
    def compress_helper(s, b):
        '''helps keep track of 0s and 1s that are being compressed'''
        if s == "":
            return ""
        if s[0] != str(b):
            return '0' * 5 + compress_helper(s, 1-b)
        else:
            return numToBinPadded(min(count(s) , MAX_RUN_LENGTH)) + compress_helper(s[min(MAX_RUN_LENGTH, count(s)):] , 1-b)
    return compress_helper(s, 0)

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    return ("0" * 5 +  numToBinary(binaryToNum(s) + 1))[-5:]

def countBin(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n == 0:
        return s 
    return countBin(increment(s), n-1)

def numToBinPadded(n):
    ''' returns a binary string of 5 digits'''
    return countBin("00000", n)
       
def uncompress(s):
    '''inverts the compressed string'''
    def uncompress_helper(s, state):
        '''helps the process of uncompressing by having it equal two states'''
        if s== "":
            return ""
        else:
            if state == 0:
                return binaryToNum(s[:5]) * "0" + uncompress_helper(s[5:], 1 - state)
            if state == 1:
                return binaryToNum(s[:5]) * "1" + uncompress_helper(s[5:], 1 - state)
    return uncompress_helper(s,0)

    
def compression(s):
    ''' returns the compression ratio'''
    return len(compress(s))/ len(s)

def count(s):
    '''returns how many numbers are in a row of the beginning of string'''
    if len(s) == 1:
        return 1
    if s[0] == s[1]:
        return 1 + count(s[1:])
    return 1



#The largest number of bits that my compress algorithm is 31.

#The tests that I conducted were that as follows and the ratios are small.
    '''def test01(self):
        sequence = '0' * 64
        compress = hw6.compress(sequence)
        self.assertEqual(compress, '1111100000111110000000010')
        uncompress = hw6.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw6.compression(sequence), 0.390625, 4)

    def test02(self):
        sequence = '01' * 32
        compress = hw6.compress(sequence)
        self.assertEqual(compress, '00001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001')
        uncompress = hw6.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw6.compression(sequence), 5.0, 4)

    def test03(self):
        sequence = '10' * 32
        compress = hw6.compress(sequence)
        self.assertEqual(compress, '0000000001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001')
        uncompress = hw6.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw6.compression(sequence), 5.078125, 4)

    def test04(self):
        sequence = '0' * hw6.MAX_RUN_LENGTH + '1' * hw6.MAX_RUN_LENGTH + '0' * (64 - 2 * hw6.MAX_RUN_LENGTH)
        compress = hw6.compress(sequence)
        self.assertEqual(compress, '111111111100010')
        uncompress = hw6.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw6.compression(sequence), 0.234375, 4)

    def test05(self):
        sequence = '0' * (hw6.MAX_RUN_LENGTH + 1) + '1' * (hw6.MAX_RUN_LENGTH + 1) + '0' * (64 - 2 * hw6.MAX_RUN_LENGTH - 2)
        compress = hw6.compress(sequence)
        self.assertEqual(compress, '111110000000001111110000000001')
        uncompress = hw6.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw6.compression(sequence), 0.46875, 4)

    def test06(self):
        sequence = '1' * hw6.MAX_RUN_LENGTH + '0' * hw6.MAX_RUN_LENGTH + '1' * (64 - 2 * hw6.MAX_RUN_LENGTH)
        compress = hw6.compress(sequence)
        self.assertEqual(compress, '00000111111111100010')
        uncompress = hw6.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw6.compression(sequence), 0.3125, 4)'''



#Professor Lai's algorithm cannot exist because data will get lost or will take too long
