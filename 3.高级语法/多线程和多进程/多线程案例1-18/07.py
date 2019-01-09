# encoding:utf-8
# 守护线程和不是守护线程的对比

import  time
import threading
# def fun():
#     print("Start fun")
#     time.sleep(2)
#     print("end fun")
#
# import  time
# import threading
# def fun2():
#     print("Start fun2")
#     time.sleep(4)
#     print("end fun2")
#
# def main():
#     t1 = threading.Thread(target=fun,args=())
#     t2 = threading.Thread(target=fun2,args=())
#     # 设置fun2为守护线程，一旦设置为守护线程，则代表该线程不重要
#     # 设置守护线程要在线程start之前设置
#     t2.setDaemon(True)# 或者t2.daemon = True
#     t1.start()# t1正常运行
#     t2.start()# t2启动
#
#
# if __name__ == '__main__':
#     main() # end fun2这句话并未打印，因为在该线程还未执行完毕时候，主线程已经退出执行
#

# 例子2
# 关于join和守护线程
# join的工作是线程同步，而守护线程则是让主线程不用在乎守护的线程的执行是否完毕，那么如果两者同时出现会如何
def fun():
    print("Start fun")
    time.sleep(2)
    print("end fun")


import time
import threading


def fun2():
    print("Start fun2")
    time.sleep(4)
    print("end fun2")


def main():
    t1 = threading.Thread(target=fun, args=())
    t2 = threading.Thread(target=fun2, args=())
    t2.setDaemon(True)  # 或者t2.daemon = True
    t1.start()  # t1正常运行
    t2.start()  # t2启动

    t1.join() # 设置线程强行同步，就会让守护线程机制失效
    # t2.join()
    t2.join(timeout=2) # join参数 timeout = 让主函数等待子函数多少秒时间,我们这里测试，让join线程同步还延迟4秒并且是守护线程的情况下让主线程等待2秒
    # 结果来说还没等线程同步就被该主函数抹杀掉了 ，timeout>join>deamon 执行等级

if __name__ == '__main__':
    main()  # end fun2这句话并未打印，因为在该线程还未执行完毕时候，主线程已经退出执行
