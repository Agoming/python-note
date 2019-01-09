# encoding:utf-8
import  multiprocessing
import time

# 使用JoinableQueue库编写生产者和消费者模式

def consumer(input_q): # 消费者
    print("Into consumer",time.ctime())
    while True:
        item = input_q.get() # 将消费者从queue库取走的商品放置到变量item
        print("get",item,"out of q") # 将变量打印出来
        input_q.task_done()# 在每次消费者在queue库取走东西后，处理好相关问题，调用此方法用于提醒join是否停止阻塞，让线程向前执行或者退出，说明白点就是告知消费者queue库里面还有没有商品，没有就退出，有就继续
    print("out of consumer",time,ctime()) # 这句话不会执行，原因：q.join收集到四个task_done信号后，主线程启动，还未等待print完成,进程就结束了

def producer(sequence,output_p):  # 生产者
    print("Info procuder:",time.ctime())
    for item in sequence:
        output_p.put(item) # 生成物品 放置到JoinableQueue库里面
        print("put",item,"of q")
    print("Out of procuder:",time.ctime())


if __name__ == "__main__":
    q = multiprocessing.JoinableQueue()
    cos_p = multiprocessing.Process(target = consumer,args = (q ,))
    cos_p.daemon = True # 启动守护线程，在主线程结束之后，该线程马上终止
    cos_p.start()

    sequence = [1,2,3,4] # 生成4个产品
    producer(sequence,q) # 将库放置到producer函数
    q.join() # 提交