# coding:utf-8
from Queue import Queue
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
                words = self._q.get(True, 1000)
                if words:
                    return words
                else:
                    return 0
            except Exception:
                print enumerate
                self._q.task_done()

    def set_words(self, num):
        self._q.put(num)

    def run(self):
        i = 0
        while 1:
            time.sleep(4)
            self.set_words(i)
            i += 1
