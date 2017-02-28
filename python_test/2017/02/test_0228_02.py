# coding:utf-8
import time
import threading


def consumer(cond):
    t = threading.current_thread()
    with cond:
        cond.wait()  # 线程挂起 创建锁一个名字为waiter的锁 并且设置锁为locked 这个锁用于线程间通信
        print("{} consumer".format(t.name))


def producer(cond):
    t = threading.current_thread()
    with cond:
        print("{} producer".format(t.name))
        cond.notifyAll()  # 释放锁 唤醒消费者


condition = threading.Condition()
c1 = threading.Thread(name="c1", target=consumer, args=(condition,))
c2 = threading.Thread(name="c2", target=consumer, args=(condition,))
p = threading.Thread(name='p', target=producer, args=(condition,))


c1.start()
time.sleep(1)
c2.start()
time.sleep(1)
p.start()

