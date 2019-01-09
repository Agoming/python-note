# encoding:utf-8
import  multiprocessing # 引入线程包
from time import sleep,ctime # 把sleep和ctime包独立引入
# 使用Process来创建线程

def clock(interval):
    while True: # 设置死循环
        print("The time is %s" % ctime()) # 通过%s放置时间进字符串中
        sleep(interval) # 通过参数控制停顿时间

if __name__ == "__main__":
    p = multiprocessing.Process(target = clock , args=(5,)) # 使用Process将需要放置在线程的函数和其参数一同放置
    p.start()
    # while True:
    #     print("sleeping.....")
    #     sleep(1)