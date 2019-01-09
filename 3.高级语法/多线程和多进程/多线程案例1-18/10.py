# 多线程的类化(工业化)写法
# coding:utf-8
import threading
from time import sleep,ctime

class ThreadFunc:
    def __init__(self,name):
        self.name = name

    def loop(self,name,st):
        print("start loop:",name,"at",ctime())
        sleep(st)
        print("start loop:",name,"at",ctime())

def main():
    print("starting at",ctime())
    t = ThreadFunc("loop") # 此参数传给self
    # 也可以ThreadFunc("loop").loop
    t1 = threading.Thread(target=t.loop,args=("LOOP1",4)) # 传入参数一个name一个是st

    # 西方工业化写法
    t2 = threading.Thread(target=ThreadFunc('loop').loop,args=("LOOP2",2))
    # 其实就是同过类引入其需要被子线程执行的函数而已

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("all done at ",ctime())

if __name__ == "__main__":
    main()
