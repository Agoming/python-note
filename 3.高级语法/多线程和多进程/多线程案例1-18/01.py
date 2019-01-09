
# 不使用多线程来计算两个函数顺序调用运行时间

import time
def loop1():
    print("Start loop 1",time.ctime())# 获取开始时间
    time.sleep(4)
    print("End loop 1",time.ctime())# 延迟4秒后，获取结束时间

def loop2():
    print("Start loop 2",time.ctime())
    time.sleep(2) # 延迟2秒
    print("end loop 2",time.ctime())

def main(): # 重写主函数
    print("Starting at:",time.ctime())
    loop1()# 调用两个函数
    loop2()
    print("end at",time.ctime())


if __name__ == '__main__':
    main() # 使用主函数作为入口
    # 一共执行6秒