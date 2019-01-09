# encoding:utf-8
# 使用继承创建线程，通过类实例化对象启动线程

import multiprocessing
import time

class ClockProcess(multiprocessing.Process): # 一般写某继承父类的函数，最好函数名称都带上其父类名称
    def __init__(self,sl):
        super().__init__() # 与多线程一样都要重写父类函数
        self.sl = sl

    def run(self):
        while True:
            print("The time is %s" % time.ctime())
            time.sleep(self.sl)

if __name__ == "__main__":
    p = ClockProcess(3)
    p.start() # 通过实例化对象可以直接使用
    # while True:
    #     print("sleep....")
    #     time.sleep(1)