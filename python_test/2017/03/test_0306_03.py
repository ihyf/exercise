# coding:utf-8
import time
from multiprocessing import Pool


def profile(func):
    def warpper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("use time:{}".format(end - start))
    return warpper


def fib(n):
    if n <= 2:
        return 1
    return fib(n-1)+fib(n-2)


@profile
def no_processing():
    fib(35)
    fib(35)


@profile
def has_processing():
    p = Pool(2)
    p.map(fib, [35]*2)


no_processing()
has_processing()
