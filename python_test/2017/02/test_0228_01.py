# coding utf-8
from random import random
from threading import Thread, Semaphore, Lock
import time
sema = Semaphore(3)


def profile(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(end-start)
    return wrapper()


def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


def foo(tid):
    with sema:
        print("tid={} acquire ".format(tid))
        wt = random()*2
        time.sleep(wt)
        print("tid={} release".format(tid))
threads = []


def test_sema():
    # 信号量test
    for i in range(5):
        t = Thread(target=foo, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


value = 0
lock = Lock()


def get_lock():
    global value
    with lock:
        new = value+1
        time.sleep(0.001)
        value = new


def test_lock():
    for i in range(4):
        t = Thread(target=get_lock)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print(value)

test_lock()


