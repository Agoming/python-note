# encoding:utf-8
# http://www.runoob.com/python3/python3-multithreading.html # 关于Queue和lifoqueue
import  threading
import  time

# python2 调用
# from Queue import Queue # 要从Queue包里面引入

# python3 调用
import queue  # 直接引入

# queue是一个特殊的仓库(list)
# queue一个特殊的特性：运行存储里面的变量先进先出，内部自动排序
# 案例： 使用queue编写一个生产者生成东西到仓库，消费者到仓库把东西消费掉的一个场景
class Producer(threading.Thread):# 利用线程继承写法编写多线程
    def run(self): # 重写run函数
        global queue
        count = 0 # 记录生成的东西
        while True:
            if queue.qsize() < 1000: # qsize = 返回queue内容长度，判断queue仓库是否有一千的商品 如果有则不再生产
                for i in range(100):
                    count = count + 1 # 因为第一次生成出来的是0  所以加一 好记录
                    msg = "生产产品" + str(count) + "号" # 将产品序号转化为str 再加入其他字符
                    queue.put(msg) # put=放置商品 将已经转化为str的产品放置到queue仓库
                    print(msg)
            time.sleep(0.5) # 当生成者生产完毕时，停顿0.5秒


class Consumer(threading.Thread):
    def run(self):
        global  queue
        while True:
            if queue.qsize() > 100: # 当商品多余100个时候，消费者才进去获取
                for i in range(3):
                    msg = self.name + "消费了" + queue.get() # get=获取商品
                    print(msg)
            time.sleep(1) # 消费完就停顿一秒

if __name__ == "__main__":
    queue = queue.Queue() # queue.Queue(Maxsize) # Maxsize=可存放最大尺寸

    for i in range(500):
        queue.put("初始产品"+str(i)+"号")

    for i in range(2):
        p = Producer()
        p.start() # 继承写法，实例化对象可直接调用

    for i in range(5):
        c = Consumer()
        c.start()

    # 一直循环生产和消费的动作
