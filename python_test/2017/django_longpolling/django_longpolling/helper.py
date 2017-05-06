# coding:utf-8
from Queue import Queue, Empty
from threading import Thread

import time


def singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]
    return _singleton


class Reader(Thread):
    def __init__(self):
        super(Reader, self).__init__()
        self._q = Queue()
        self.start()

    def get_words(self):
        while 1:
            try:
                words = self._q.get(True, 5)
                if words:
                    return words
            except Empty:
                return ''

    def set_words(self, num):
        self._q.put(num)

    def run(self):
        i = 0
        while 1:
            time.sleep(1)
            self.set_words(i)
            i += 1
