# semaphore() = 参数定义某资源最多允许几个线程使用
# encoding:utf-8
import threading
import time

semaphore = threading.Semaphore(3) # 允许三个线程访问

def func():
    if semaphore.acquire(): # 上锁
        for i in range(1): # 让每个线程出现三次数
            print(threading.currentThread().getName()+"  get semaphore")# 获取当前正在运行的线程
        time.sleep(15)
        semaphore.release()# 释放锁
        print(threading.currentThread().getName()+'  release semaphore') # 获取释放锁之后还在运行的线程

for i in range(8):# 循环启动8个子线程
    t1 = threading.Thread(target=func,args=())
    t1.start()

# 结果：在结束前semaphore锁释放前，每次循环调用子线程只有三个子线程同时被调用，在调用线程达到3个的时候，func就会释放锁并且停止15秒
      # 在释放锁之后，再次把锁锁上，再重复满足三个线程并且调用，再次释放锁和停顿15秒，直到循环调用次数满足