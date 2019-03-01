# encoding:utf-8
# 将list生成式从大括号改成小括号写，就生成了简单的generator生成器

L = [i * i for i in range(10)] # 普通list生成器
print(L)

g = (i * i for i in range(10)) # generator生成器
print(g) # generator返回的是对象，而不是数列
