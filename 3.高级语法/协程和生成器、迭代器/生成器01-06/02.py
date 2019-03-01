# encoding:utf-8
# 使用普通打印和for循环迭代方法打印


# 使用next方法打印
L = (i * i for i in range(10))
print(next(L))
print(next(L))
print(next(L))
print(next(L))
print(next(L))
print(next(L))
print(next(L))
print(next(L))
print(next(L))
print(next(L))

# 因为generator是迭代器，也可以被for访问
H = (i * i for i in range(10))
for i in H:
    print(i) # 在被next访问过的L数列 无法再次获取 只能重写一个L数列

