# coding:utf-8
from functools import reduce


def normaxlize(name):
    a = name[0].upper()
    b = name[1:].lower()
    return a+b

L = ['adam', 'LISA', 'bafT']
L = list(map(normaxlize, L))
print(L)


def fn(x, y):
    return x*10+y


def char2int(s):
    return {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
            '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}[s]


print(str(map(char2int, '13579')))
print(reduce(fn, map(char2int, '13579')))
