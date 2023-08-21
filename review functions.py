def collatz(n):
    print(n, end=' ')
    if n == 1:
        return
    if n % 2 == 0:
        collatz(n//2)
    else:
        collatz(3 * n + 1)

def splitter(x):
    if x > 0:
        print(x, end= ' ')
        splitter(x // 2)
        splitter(x // 2)

def mystery(x, y):
    if y == 0:
        return 1
    if y == 1:
        return x
    if y % 2 == 0:
        return 1 * mystery(x * x, y // 2)

    return x * mystery(x * x, y // 2)

def col_rev(lst):
    if lst == []:
        return []
    if isinstance(lst[0], list):
        return col_rev(lst[1:]) + col_rev(lst[0])
    return col_rev(lst[1:]) + [lst[0]]

def keep_small_and_square(values, thresold):
    return map(lambda x: x * x, filter(lambda x: x * x < thresold, values))

def collapse(lst):
    if lst ==[]:
        return []
    if isinstance(lst[0], list):
        return collapse(lst[0]) + collapse(lst[1:])
    return [[lst[0]] + collapse(lst[1:])
def mystery(n, L):
    if L == []:
        return None
    if n == L[0]:
        return 0
    return 1 + myst(L[1:])

