# timeit
  # 准确测量小段代码的执行时间

import  time
import timeit

# 使用timem模块测量例子
# def p():
#     time.sleep(3.6)
# t1 = time.time()
# p()
# print(time.time() - t1)

# 使用timeit模块测量
# stmt 放置需要被测量的代码,可以传参数
# number = 执行次数
# num = []
# def a():
#     for i in range(1000):
#         num.append(i)
# t1 = timeit.timeit(stmt="[i for i in range(1000)]",number=100000)
# t2 = timeit.timeit(stmt=a,number=100000)
# print(t1)
# print(t2)

# timeit 执行一个函数，测试其执行时间
# def doit():
#     a = 0
#     for i in range(5):
#         a += i
#         print(a)
#
# t = timeit.timeit(stmt=doit,number=10)
# print(t)

# setup 是timeit里面的属性，主要用于带入测试函数的属性
# 在使用setup带入参数时，必须把函数赋值给一个变量，才能进行传参

# 注意下面函数是被传给了变量
s = """  
def b(num):
    for i in range(num):
        print(i)
"""

t = timeit.timeit("b(num)",setup=s+"num = 3",number=10)
print(t)

