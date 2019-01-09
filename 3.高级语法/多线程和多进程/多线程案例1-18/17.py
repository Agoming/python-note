# threading.Timer(time,target) = 设置指定时间启动某子线程 time = 指定的时间 按秒算，target = 需要指定的函数
# encoding:utf-8
import threading
import time

def func():
    print(" I am running...",time.ctime())
    time.sleep(4)
    print(" I am done....",time.ctime())

if __name__ == "__main__":
    print("启动时间:",time.ctime())
    t = threading.Timer(6,func) # 停顿6秒 # 在停顿过程中，系统不会挂起主线程，而是继续顺着下来执行，直到停顿时间过去 需要执行该子线程时候，才会继续执行
    t.start()
    print("结束时间:",time.ctime())
