# encoding:utf-8
# 解决多线程同时调用同一变量时候产生的共享变量问题
# 使用lock让其变量变得可控制

import threading
sum = 0
loopSum = 10000000

lock = threading.Lock()  # 把锁赋给变量  记得括号，是调用其方法 赋值给变量

def myadd():
    global  sum,loopSum # 还是要把这两变量变成全局变量  才能让循环的值被带出去
    for i in range(1,loopSum):
        lock.acquire() # 上锁
        sum += 1       # 调用需要被上锁的变量
        lock.release() # 解锁 或者说释放锁，让变量可以被其他线程访问

def myMinu():
    global sum,loopSum
    for i  in range(1,loopSum):
        lock.acquire() # 哪怕是另一个线程调用也需要对变量进行上锁
        sum -= 1       # 对变量调用
        lock.release() # 解锁

if __name__ == '__main__':
    print("Starting {0}".format(sum))

    t1 = threading.Thread(target=myadd,args=())
    t2 = threading.Thread(target=myMinu,args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done{0}".format(sum)) # 在每个线程在调用sum变量 每一次调用都进行上锁和解锁操作的情况下，最后结果正确了