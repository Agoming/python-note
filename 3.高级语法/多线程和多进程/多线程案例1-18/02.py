# 使用_thread来计算两个函数的运行时间

import time
import _thread as thread

def loop1():
    print("Start loop 1 at:",time.ctime())
    time.sleep(4)
    print("end loop 1 at:",time.ctime())

def loop2():
    print("Start loop 2 at :",time.ctime())
    time.sleep(2)
    print("end loop2 at :",time.ctime())
    # 跟 01 案例一样都是两个相同的函数不同地停顿

def main():
    print("Starting at:",time.ctime())
    # 启动多线程执行的概念 = 利用多线程去调用某函数，也就是一个线程负责一个函数
    # 启动多线程语法为 _thread.start_new_thread(函数,(args,))
    # 参数注意，前者是需要运行的函数名(不带括号，并不是运行函数),后者为函数的参数，作为元祖使用，为空则使用空元祖
    # 注意:如果函数只有一个参数，则需要在参数后面加一个逗号
    thread.start_new_thread(loop1,()) # 哪怕没有参数也要有括号
    thread.start_new_thread(loop2,())
    print("all done at:",time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)# 让主函数无限循环不结束，不然的话主函数执行完了 子函数还没执行完就一起结束就永远看不到子函数的end
        # 两个函数同时运行所用时间 4秒，使用多线程能大大增加程序的运行性能