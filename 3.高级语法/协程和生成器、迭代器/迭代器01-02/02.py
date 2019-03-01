# 使用iter函数对iterable和Iterator的关系进行判断运算
# encoding:utf-8

from collections import Iterator
print(isinstance(iter("abc"),Iterator)) # 使用iter把原本是迭代对象但不是迭代器的str转化成迭代器，从判断答案True可以看出，str类型转化成功