# encoding:utf-8
# 在02版本上加入参数

import time
import _thread as thread

def loop1(in1):
    print("start loop1",time.ctime())
    print("我是参数",in1)
    time.sleep(4)
    print("end loop2",time.ctime())

def loop2(in1,in2):
    print("start loop2",time.ctime())
    print("参数",in1,in2)
    time.sleep(2)
    print("end loop2",time.ctime())
def main():
    print("starting at:",time.ctime())
    thread.start_new_thread(loop1,("第一",))# 如果只有一个参数就需要在参数后面加入逗号
    thread.start_new_thread(loop2,("第一","第二"))# 两个以上或者没有都不需要加逗号
    print("all done at",time.ctime())

if __name__ == '__main__':
    main()
    # 一定要由while语句
    # 因为启动多线程后本程序就以主线程为目标线程执行，当主线程执行完毕，整个程序关闭，那么子线程也会关闭
    while True:
        time.sleep(10)
