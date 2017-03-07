# coding:utf-8
import time
import threading
from random import random
from multiprocessing import Queue


def double(n):
    return n*2


class Worker(threading.Thread):
    def __init__(self, queue):
        super(Worker, self).__init__()
        self._q = queue
        self.daemon = True
        self.start()

    def run(self):
        while 1:
            f, args, kwargs = self._q.get()
            try:
                print("use {}".format(self.name))
                print(f, args, **kwargs)
            except Exception as e:
                print(e)
                self._q.task_done()


class ThreadPool(object):
    def __init__(self, num_t=5):
        self._q = Queue(5)
        for _ in range(num_t):
            Worker(self._q)

    def add_task(self, f, args, **kwargs):
        self._q.put((f, args, kwargs))

    def wait_complete(self):
        self._q.join()


t = ThreadPool()
for i in range(8):
    t.add_task(double, i)
t.wait_complete()


