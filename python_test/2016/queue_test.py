#coding:utf-8

# import Queue
#
# my_queue = Queue.Queue(maxsize=10)
# my_queue.put("the first")
# print my_queue.get()
# Queue.qsize() 返回队列的大小
# Queue.empty() 如果队列为空，返回True,反之False
# Queue.full() 如果队列满了，返回True,反之False
# Queue.full 与 maxsize 大小对应
# Queue.get([block[, timeout]])获取队列，timeout等待时间
# Queue.get_nowait() 相当Queue.get(False)
# 非阻塞 Queue.put(item) 写入队列，timeout等待时间
# Queue.put_nowait(item) 相当Queue.put(item, False)
# Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
# Queue.join() 实际上意味着等到队列为空，再执行别的操作

import Queue
import threading
import time
import random

q = Queue.Queue(0) #当有多个线程共享一个东西的时候就可以用它了
NUM_WORKERS = 3

class MyThread(threading.Thread):

    def __init__(self,input,worktype):
        self._jobq = input
        self._work_type = worktype
        threading.Thread.__init__(self)

    def run(self):
        while True:
            if self._jobq.qsize() > 0:
                self._process_job(self._jobq.get(),self._work_type)
            else:break

    def _process_job(self, job, worktype):
        doJob(job,worktype)

def doJob(job, worktype):
    time.sleep(random.random() * 3)
    print"doing",job," worktype ",worktype

if __name__ == '__main__':
    print "begin...."
    for i in range(NUM_WORKERS * 2):
        q.put(i) #放入到任务队列中去
    print "job qsize:",q.qsize()

    for x in range(NUM_WORKERS):
        MyThread(q,x).start()