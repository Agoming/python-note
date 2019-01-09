# encoding:utf-8
# 案例13的死锁问题：解决方案1：控制锁的时间
import  threading
import time

lock_1 = threading.Lock()
lock_2 = threading.Lock()

def func_1():
    print("func_1 starting.....",time.ctime())
    lock_1.acquire(timeout=4) # 申请锁1 等待时间4秒
    print("func_1 申请了 lock_1...",time.ctime())
    time.sleep(2)
    print("func_1 等待 lock_2......",time.ctime())

    rst = lock_2.acquire(timeout=2) # 申请锁2 等待时间2秒

    if rst: # 假如得到了锁1情况下
        print("func_1 已经得到锁lock_2")
        lock_2.release()
        print("func_1 释放了锁lock_2")
    else: # 当申请超时执行
        print("func_1 没申请到锁loc_2")
    print("func_1 申请了lock_2 .....",time.ctime())

    lock_1.release()
    print("func_1 释放了lock_1",time.ctime())
    print("func_1 done...") # func_1结束

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
    print("主程序启动......",time.ctime())
    t1 = threading.Thread(target=func_1,args=())
    t2 = threading.Thread(target=func_2,args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    # 在func_1没申请到锁lock_2时等待了2秒之后便不再等待，而是发出 无法申请的信号，并且释放了lock_1，让func_2申请到了lock_1并且让程序进行下去，并未出现卡死情况