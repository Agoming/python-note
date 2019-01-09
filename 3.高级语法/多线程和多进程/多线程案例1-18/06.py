# encoding:utf-8
# 使用threading来模拟非守护线程
import  time
import threading
def fun():
    print("Start fun")
    time.sleep(2)
    print("end fun")


def main():
    t1 = threading.Thread(target=fun,args=())
    t1.start()

if __name__ == "__main__":
    print("如果是守护线程，在执行完我这句话就可以结束了")# 没结束并且等待fun子线程，则证明fun是非守护线程
    main()



