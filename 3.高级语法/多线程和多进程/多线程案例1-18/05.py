# encoding:utf-8
# 使用threading里面的join来让线程一起提交

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
    print("start at",time.ctime())
    t1 = threading.Thread(target=loop1,args=("第一",))
    t1.start()
    t2 = threading.Thread(target=loop2,args=("第二","第一"))
    t2.start()

    # 注意 你的那个线程先启动就要让哪个线程先提交不管他停顿多长时间
    t1.join()
    t2.join() #join的作用在于主线程任务结束之后，进入阻塞状态，一直等待其他的子线程执行结果结束之后，主线程再终止
    print("all dont at",time.ctime())

if __name__ == "__main__":
    main()
    # while True:
    #     time.sleep(10)