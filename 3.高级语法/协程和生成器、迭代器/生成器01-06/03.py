# encoding:utf-8
# 使用generator来编写斐波那契数列
# 如果generator推算的算法比较复杂，用类似列表生成式的for循环无法实现时，可以使用函数来实现

# 普通写法
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b # 注意此句子的算法，用于计算斐波那契的叠加
        # a,b = b,a+b 相当于
        # t = (b,a+b) # 这是一个tuple
        # a = t(0)
        # b = t(1)
        n = n + 1
    return  'done' # 解决返回

print(fib(6))

# generator写法
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b # 其实就是改变了这里
        a,b = b,a+b
        n = n + 1
    return "done"
f = fib(6) # 当有yield就不是一个普通的函数，而是一个generator所以需要实例化对象
print(f)
