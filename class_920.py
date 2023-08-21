from cs115 import *


def powerset(s):
    if s=="":
        return [""]
    else:
        map(lambda x: s[0] + s[1:])

def LCS(s1, s2):
    if s1=="" or s2=="":
        return 0
    elif s1[0]==s2[0]:
        return 1 + LCS(s1[1:], s2[1:])
    else:
        left = LCS(s1[1:],s2)
        right = LCS(s1, s2[1:])
        return max(LCS(s1, s2[1:]), LCS(s1[1:], s2))

def testLCS():
    assert LCS("spam","spa!") == 3
    assert LCS("spam","xsam") == 3
    print("good")
        
