# encoding:utf-8
import time
import threading
# threading常用函数的使用
def loop1():
    # ctime 得到当前时间
    print('Start loop 1 at :', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(6)
    print('End loop 1 at:', time.ctime())

def loop2():
    # ctime 得到当前时间
    print('Start loop 2 at :', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(1)
    print('End loop 2 at:', time.ctime())

def loop3():
    # ctime 得到当前时间
    print('Start loop 3 at :', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(5)
    print('End loop 3 at:', time.ctime())

def main():
    print("starting at",time.ctime())
    t1 = threading.Thread(target=loop1,args=())
    t1.setName("one")# 为线程设置名称
    t1.start()

    t2 = threading.Thread(target=loop2,args=())
    t2.setName("two")
    t2.start()

    t3 = threading.Thread(target=loop3,args=())
    t3.setName("three")
    t3.start()

    for thr in threading.enumerate():# enumerate获取当前运行的线程数量
        print("获取正在运行的线程名称:{0}".format(thr.getName()))# getName获取线程名称

    print("获取正在执行的子线程数量:{0}".format(threading.activeCount()))

    time.sleep(3) # 延迟三秒,此时线程2已经结束

    for thr in threading.enumerate():# 此时线程2已经结束了，所以应该是三个线程在执行(一个主线程，两个子线程)
        print("获取停顿三秒后的仍执行的线程名称:{0}".format(thr.getName()))

    print("获取仍在执行的子线程数量:{0}".format(threading.activeCount()))

    print(" end at:",time.ctime())


if __name__ == '__main__':
     main()