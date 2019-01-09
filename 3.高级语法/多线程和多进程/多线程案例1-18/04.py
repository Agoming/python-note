# encoding:utf-8
# 使用threading包来处理多线程

import time
import threading

def loop1(in1):
    print("start loop1",time.ctime())
    print("我是参数",in1)
    time.sleep(4)
    print("end loop1",time.ctime())

def loop2(in1,in2):
    print("start loop2",time.ctime())
    print("参数",in1,in2)
    time.sleep(2)
    print("end loop2",time.ctime())

def main():
    print("starting at:",time.ctime())
    t1 = threading.Thread(target=loop1,args=("第一",)) # 传入参数也和_thread差不多
    t1.start() # 需要start启动
    t2 = threading.Thread(target=loop2,args=("第一","第二"))
    t2.start() # 需要start启动
    print("all at",time.ctime())

if __name__ == "__main__":
    main()
    # while True:
    #     time.sleep(10)