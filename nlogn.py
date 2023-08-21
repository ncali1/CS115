import math

EPSILON = 1e-9


def nlogn(c):
    lower = 0.0
    upper = c
    while True:
        middle = lower + (upper - lower) / 2
        val = middle * math.log(middle, 2)
        if abs(c - val) <= EPSILON:
            return int(middle)
        if val > c:
            upper = middle
        else:
            lower = middle



def cube(num):
    return num * num * num

number = float(input( " Please Enter number: "))

cub = cube(number)
print("The cube of a number {0} = {1}".format(number, cub))
