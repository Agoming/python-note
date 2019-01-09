# encoding:utf-8
# 可重入锁，当同一个线程在未释放同一把锁的情况下，可再次申请的操作

import threading
import time

class MyThread(threading.Thread):# 继承多线程写法
    def run(self):
        global num
        time.sleep(1)
        if mutex.acquire(1):# 申请超时超过一秒则不申请
            num = num+1
            msg = self.name +"set num to"+str(num)
            print(msg)
            mutex.acquire() # 在同一把锁还未释放的时候，再次申请同一把锁
            mutex.release()  # 不管释放的是否是同一把锁，你申请了多少次就要释放多少次
            mutex.release()


num = 0
mutex = threading.RLock()# Rlock = 可重入锁
def testTh():
    for i in range(5):
        t = MyThread()
        t.start()

if __name__ == '__main__':
    testTh()