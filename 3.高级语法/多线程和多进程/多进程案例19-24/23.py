# encoding:utf-8
import multiprocessing
import time

# 哨兵问题，在JoinableQueue库里面，哨兵是用特殊方法(比如判断变量)制造而成
# 制作哨兵通知消费者，仓库没产品了

def consumer(input_q):
    print("Into cousumer:",time.ctime())
    while True:
        item = input_q.get()
        if item is None:
            print("收到哨兵",item)
            break # 退出判断
        print("get",item,"out of q")
    print("Out of consumer",time.ctime())

def producer(sequence,output_q):
    print("Info procuder:",time.ctime())
    for item in sequence :
        output_q.put(item)
        print("put",item,"into q")
    print("Out of procuder",time.ctime())

if __name__ == "__main__":
    q = multiprocessing.Queue()
    cons_q = multiprocessing.Process(target = consumer,args = (q,))
    cons_q.start()

    sequence = [1,2,3,4] # 生产四个产品
    producer(sequence,q)
    q.put(None) # 在仓库里面放置一个名为"None"的产品，当消费者检测到"None" 的产品时就会跳出消费循环，从而达到哨兵的效果
    cons_q.join()
