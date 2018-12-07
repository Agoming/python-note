# 四大内置数据结构
      # list 列表
      # set  集合
      # dict 字典
      # tuple 元祖

# 本章大纲
      # 集合-set
            # 集合常用操作
            # 集合序列操作
            # 集合遍历操作
            # 集合内置函数操作
            # 集合常用函数
            # 冰冻集合

# 集合的特征
       # 一堆确定结果但无序又是唯一的数据凑在一起便是集合，集合中每一个数据都成是独立的元素
       # 集合内数据无序，即无法使用索引和分片
       # 集合内部数据元祖具有唯一性，所以可以用来排除重复数据
       # 集合内的数据只是能可哈希数据(hash)，比如str,in,float,tuple,冰冻集合等


# 集合常用操作

# 使用set定义集合
s = set()
print(type(s))
print(s)

# 使用大括号定义set
s = {1,2,3,4,5}
print(type(s))
print(s)
# 使用大括号定义空set，类型为dict字典
s = {}
print(type(s))
print(s)

# 如果直接使用小括号定义空set，则类型为tuple元祖
s = ()
print(type(s))
print(s)
# 所以空的set只能使用set()定义,但是带值的集合不能使用set()创建，所以 带值的集合 = {val,val,val}，不带值的结合 = set()

# 集合序列操作

# 成员检测
# in
s = {4,5,"1","2"}
if 1 in s:
    print("true")
else:
    print("false")

# not in
if 4 not in s:
    print("true")
else:
    print("false")

# 因为集合里的内容是无序的，所以无法进行序列相加,序列相乘等等

# 集合遍历操作
# 使用for进行遍历，观察定义的集合内容顺序和使用for遍历打印之后的顺序
s ={3,4,5,"1","2","3",3.4}
for i in s:
    print(type(i))# 尽管打印为无序，尽管成为了一个独立的元素，但是还是保留了定义时的类型
    print(i,end=" ")

# 附带元祖tuple的遍历
# 访问集合里面每个元祖的值
s1 = {(1,2,3),("1","2","3"),(3.4,3.5,3.6)}
for k,v,m in s1:
    print(k,"--",v,"--",m)

# 直接访问每个元祖
for k in s1:
    print(k)

# set和dict都是hash表实现，而list这是链表实现,这就是为什么list是有序，而set是无序，dict则可以通过键值索引

# 集合的内置函数

# 使用集合过滤重复元素
s = {2,2,2,3,1,2,4,5,5,6}
print(s)

# 普通集合内置函数
s1 = {i for i in range(1,10)}
print(s1)# 和list不同这里使用的是大括号

# 带条件的集合内置函数
s1 = {i for i in range(1,10) if i %2 == 0}
print(s1)

# 多重循环的集合内置函数
s1 = {1,2,3,4}
s2 = {"i","love","you"}

s3 = {m*n for m in s1 for n in s2}
print(s3)# 将里面的内容全部打印1到4次，并存入同一个集合当中

# 带条件的多重循环
s4 = {m*n for m in s1 for n in s2 if m == 2}
print(s4) # 将s2里面的内容全部打印2次，并存入同一个集合里

# 集合常用函数
# min,max,len使用方法和list tuple一致
s = {43,2,4,5,1,2,5,2}
print(len(s))
print(min(s))
print(max(s))

# set:转化一个集合
l = [1,2,3,4,5,6] # 创建一个list
print(type(l))
print(l)
# 进行转化
l = set(l)
print(type(l))
print(l)

# add:向集合尾部添加元素
s = {1,2,3,4}
s.add(334)
print(s)

# clear:原地清除一个集合，即不改变其地址
l = {1,2,3,4}
print(id(l))
print(l)
l.clear()
print(id(l))
print(l)


# copy浅拷贝，关于浅拷贝和深拷贝，list篇已经说明很清楚了，请
l = {1,2,3,4,5}
l2 = l.copy()
print(id(l))
print(id(l2))

# remove移出指定的值，直接改变原有值
s = {1,2,3,4,5}
s.remove(3)
print(s)

# discard:移出指定的值，跟remove差不多，但可以设置返回值
s = {1,2,3,4,5}
s.discard(3)
print(s)

# remove和discard的区别，前者如果需要删除的值不存在则会报错，而后者则会返回一个none
s = {1,2,3,4,5}
s.discard(6)
print(s)
# s.remove(6)
# print(s)

# pop 随机移除一个元素，因为集合打印排序无法预测，pop默认为随机移除元素
s = {1,2,3,4,5,6,7}
d = s.pop()
print(d)
print(s)

# 集合函数
# intersection：交集
# difference：差集
# union:并集
# issubset:检查一个集合是否为另一个子集
# issuperset:检查一个集合是否为另一个超集

s1 = {1,2,3,4,5}
s2 = {6,7,8,9,10}
s3 = {5,6,7,8,9,10}
s4 = {1,2,3,4,5}
# intersection交集
# 让b集合去遍历a集合并返回相同的值
# 案例如下
s_1 = s1.intersection(s2)
print(s_1)

# 如何交集的对象没有相同的值则会返回一个空的集合

# intersection交集案例2
s_2 = s1.intersection(s3)
print(s_2)


# difference:差集
# 让a集合去遍历b集合并返回不同的值
# 案例如下
s_1 = s1.difference(s4)
print(s_1)
# 使用差集遍历两个集合内的对象如果完全一致则会返回一个空的集合

# difference差集案例2
s_2 = s1.difference(s2)
print(s_2)

# union:并集
# 将遍历的两个集合内容一起放进同一个集合里面
s_1 = s1.union(s2)
print(s_1)

# issubest:检查一个集合是否为另一个子集，返回值为布尔值
s_1 = s1.issubset(s2)
print(s_1)
s_2 = s1.issubset(s4)
print(s_2)


# issuperset:检查一个集合是否为另一个超集,返回值为布尔值
s_1 = s2.issuperset(s3)
print(s_1)
s_2 = s1.issuperset(s4)
print(s_2)

# 集合"-"应用,无法进行"+"应用

s1 = {1,2,3,4,5}
s2 = {5,6,7,8,9,10}

# "-"用法：判断a集合和b集合中是否有相同的值，有则抵消，并将a集合剩余的内容返回
print(s1-s2)

# 伪代码，测试"+"是否能使用
# print(s1+s2)

# frozenset: 冰冻集合
         # 冰冻集合就是不可以进行任何修改的集合(可被赋值替换)
         # frozenset是一种特殊集合

# 定义冰冻集合
s = frozenset()
# 查看冰冻集合类型并打印冰冻集合
s = frozenset()
print(type(s))

# 定义附带值的冰冻集合
s = frozenset([0,1,2,3,4,5])
print(s)

# 使用range定义冰冻集合
s = frozenset(range(10))
print(s)

# 测试冰冻集合不可被移除值或者增加值，但是可以被赋值替换，也就是传址
s = frozenset(range(5))
print(s)# 修改前
s = frozenset("asd")
print(s)# 修改后