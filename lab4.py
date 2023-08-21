from cs115 import *

#I pledge my honor that I have abided by the Stevens Honor System.


def knapsack(capacity, itemList):
    if itemList == []:
        return [0,[]]
    if capacity == 0:
        return [0,[]]
    item = itemList[0]
    weight = item[0]
    if weight > capacity:
        return knapsack(capacity, itemList[1:])
    result = knapsack(capacity - weight, itemList[1:])
    use = [item[1] + result[0], [itemList[0]] + result[1]]
    lose = knapsack(capacity, itemList[1:])
    if use[0] > lose[0]:
        return use
    return lose
