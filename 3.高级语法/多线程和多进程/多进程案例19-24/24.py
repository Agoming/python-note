# encoding:utf-8
import multiprocessing
import time

# 改进哨兵存在的问题：
# 问题1：当某个消费者取走命为"None"的哨兵之后，后来的消费者就无法再获取哨兵信息
# 解决方案: 有多少个消费者就设置多少个哨兵

def consumer(input_q): # 设置消费者逻辑
    print("Into consumer:",time.ctime())
    while True:
        item = input_q.get()
        if item is None:
            print("接受到哨兵",item)
            break
        print("pull",item,"out of q")

def producer(seqiemce,q):
    print("Into producer", time.ctime())
    for item in seqiemce:
        q.put(item)
        print("put",item)
    print("Out of procuder",time.ctime())

if __name__ == "__main__":
    q = multiprocessing.Queue()
    # 生成两个消费者
    p1 = multiprocessing.Process(target = consumer , args=(q,))
    p1.start()
    p2 = multiprocessing.Process(target = consumer , args=(q,))
    p2.start()

    seqi = [1,2,3,4]
    producer(seqi , q)

    # 加入同样数量的哨兵
    q.put("None")
    q.put("None")
    p1.join()
    p2.join()

