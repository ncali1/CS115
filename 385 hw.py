def mystery(n):
    s = 0
    for i in range(1, n):
        s =  s + i * i
    return s


print( mystery(1))
