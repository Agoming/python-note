# encoding:utf-8
# 使用isinstance判断 迭代器和迭代对象的区别

# 从collections包里面引入Iterable可迭代对象包

from collections import Iterable

l = [1,2,3,4] # 创建一个可迭代对象
print(isinstance(l,Iterable)) # 直接将从collections包引入的可迭代对象包与我们创建的可迭代对象做对比

from collections import Iterator

print(isinstance((i for i in range(10)),Iterator)) # 与上面一致，使用列表创建法创建一个0到9的list 然后与迭代器包做对比