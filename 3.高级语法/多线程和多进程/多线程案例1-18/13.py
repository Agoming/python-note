# 关于同一个线程，在没释放被# 锁上的变量时，再次调用其变量，就会形成一次死锁的问题
# encoding:utf-8
import  threading
import time

lock_1 = threading.Lock()
lock_2 = threading.Lock()

def func_1():
    print("func_1 starting.....",time.ctime())
    lock_1.acquire(2)
    print("func_1 申请了 lock_1...",time.ctime())
    time.sleep(2)
    print("func_1 等待 lock_2......",time.ctime())
    lock_2.acquire()
    print("func_1 申请了lock_2 .....",time.ctime())

    lock_2.release()
    print("func_1 释放了 lock_2",time.ctime())

    lock_1.release()
    print("func_1 释放了lock_1",time.ctime())


def func_2():
    print("func_2 starting.....",time.ctime())
    lock_2.acquire()
    print("func_2 申请了 lock_2...",time.ctime())
    time.sleep(4)
    print("func_2 等待 lock_1......",time.ctime())
    lock_1.acquire()
    print("func_2 申请了lock_1 .....",time.ctime())

    lock_1.release()
    print("func_2 释放了 lock_1",time.ctime())

    lock_2.release()
    print("func_2 释放了lock_2",time.ctime())

if __name__ == "__main__":
    print("主程序启动......")
    t1 = threading.Thread(target=func_1,args=())
    t2 = threading.Thread(target=func_2,args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("主程序启动.......")
    # func_1无法申请lock_2，所以func_2无法再次申请lock_1 ，所以两个线程都卡死了