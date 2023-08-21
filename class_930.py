from cs115 import *


def LCS(S1, S2):
    print("LCS(", S1, ",", S2, ")" )
    if S1 =='' or S2 == '':
        return 0
    elif S1[0] == S2[0]:
        return 1 + LCS(S1[1:], S2[1:])
    else:
        return max(LCS(S1, S2[1:]), LCS(S1[1:], S2))

def fastLCSalt(S1,S2)
    memo = {}
    def fLCS(S1,S2):
        if (S1, S2) in memo:
            return memo [(S1, S2)]
        elif S1 == '' or S2 == '':
            memo [(S1, S2)] = 0
            return 0
        elif S1[0] == S2[0]:
            answer = 1 + fLCS(S2[1:], S2[1:])
            memo = [(S1, S2)] = answer
            return answer
        else:
            chopS1 = fLCS(S1[1:], S2)
            chopS2 = fLCS(S1, S2[1:])
            answer = max(chopS1, chopS2)
            memo[(S1, S2)] = answer
            return answer
        return fLCS(S1, S2)
