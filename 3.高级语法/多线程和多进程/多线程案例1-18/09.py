# encoding:utf8

# 使用继承threading.Thread的方法来执行多线程
import threading
import time


class MyThread(threading.Thread):
    def __init__(self,in1):
        super(MyThread,self).__init__() # 先重写父类里的init函数
        self.in1 = in1

    def run(self):
        # 将需要线程执行的内容放置到重写run函数里面，run函数才是代表真正执行的功能
        print("start loop1", time.ctime())
        print("我是参数", self.in1)
        time.sleep(4)
        print("end loop1", time.ctime())


class MyThread2(threading.Thread):
    def __init__(self,in1,in2):
        super(MyThread2,self).__init__() # 先重写父类里的init函数
        self.in1 = in1
        self.in2 = in2

    def run(self):
        # 将需要线程执行的内容放置到重写run函数里面，run函数才是代表真正执行的功能
        print("start loop2", time.ctime())
        print("参数",self.in2,self.in1)
        time.sleep(2)
        print("end loop2", time.ctime())


# 通过重写threading.thread的方法构建的线程函数 就不需要再次调用threading.thread才能被使用 而是可以直接使用类实例start

T1 = MyThread("第一")
T2 = MyThread2("第二","第一")
T1.start()
T2.start()
T1.join()
T2.join()