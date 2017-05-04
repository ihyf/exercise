# coding:utf-8


def double_num(num):
    return num*2


def add_num(n):
    sum = 0
    for i in range(n-1):
        result = double_num(i+1)
        sum += result
    return sum


print(add_num(30))