# encoding:utf-8
# 当同一个变量被多线程同时调用的案例

import threading
sum = 0 # 需要被多线程同时调用的变量
loopSum = 10000000 # 需要循环的次数

def myAdd():
    global sum,loopSum
    for i in range(1,loopSum):
        sum += 1

def myMinu():
    global  sum,loopSum # 让sum和loopSum变成全局变量
    for i in range(1,loopSum):
        sum -= 1

if __name__ == '__main__':
    print("Starting ...{0}".format(sum))
    m1 = threading.Thread(target=myAdd,args=())
    m2 = threading.Thread(target=myMinu,args=())

    m1.start()
    m2.start()

    m1.join()
    m2.join()

    print("Done...{0}".format(sum)) # 结果是错误的，因为sum被两个子线程瞎几把访问