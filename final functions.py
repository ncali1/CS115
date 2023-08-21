'''
Final test Functions
'''


def squareSums(n):
    L = []
    s = 0
    for i in range(1, n+1):
        s += i*i
        L.append(s)
    return L



def squareSumsTrace(n):
    L = []
    s = 0
    print("s  i  L \n -----------------")
    for i in range(1,n+1):
          print(s,i,L)
          s += i*i
          L.append(s)
    print(s, i, L, "\n")
    return L
