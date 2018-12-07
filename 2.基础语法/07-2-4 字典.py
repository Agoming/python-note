# 四大内置数据结构
      # list 列表
      # set  集合
      # dict 字典
      # tuple 元祖

# 本章大纲
      # dict字典


# 字典的特征:
         # 字典是一种组合数据，没有顺序的组合数据，数据以相对应的键值形式出现
         # 字典是序列类型，但是是无序序列，所有没有分片和索引
         # 字典中的数据每个都有键值对组成，即kv对
                     # key:必须是可哈希的值，比如int,string,float,tuple但是list,set,dict不行
                     # vakye:任何值

# 字典的创建
# 创建空字典1
d = {}
print(d)

# 创建空字典
d = dict()
print(d)

# 创建带值字典
          # 每一组数据用冒号":"隔开,每一对键值用冒号隔开
d = {"one":1,"two":2,"three":3}
print(d)

# 用dict创建带值字典1
d = dict({"one":1,"two":2,"three":3})
print(d)

# 用dict创建带值字典2
# 利用赋值操作
d = dict(one = 1,two = 2,three = 3)
print(d)

# 用dict创建带值字典3
d = dict([("one",1),("two",2),("three",3)])
print(d)

# 字典常用操作
# 访问数据
d = {"one":1,"two":2,"three":3}
print(d["one"])# 通过键值访问

# 改变某个键值的内容
d["one"]="asd"
print(d)

# 删除某个键值
del d["one"]
print(d)

# 成员检测 in ,not in
# 成员检测检测的是key内容即键值
d = {"one":1,"two":2,"three":3}
# 测试检验是value还是key
if 2 in d:
    print("value")
if "two" in d:
    print("key")
if ("two",2) in d:
    print("key+value")
# 结果显示检测只检测key值

# 遍历在python2和3中区别比较大，代码不通用，这里以3作为实例
# 按key来使用for循环
d = {"one":1,"two":2,"three":3}
for k in d:
    print(k,d[k])

# 第二种方法
for k in d.keys():
    print(k,d[k])

# 只访问字典的值
for v in d.values():
    print(v)

# 特殊用法
for k,v in d.items():
    print(k,"--",v)

# 字典生成
d = {"one":1,"two":2,"three":3}
# 常规字典生成案例
dd = {k:v for k,v in d.items()}
print(dd)
# 加限制条件的字典生成案例
ddd ={k:v for k,v in d.items() if v%2 == 0}
print(ddd)

# 字典相关函数
# 通用函数:len,max,min关于通用函数详细请看
d = {"one":1,"two":2,"three":3}
# len：返回长度
print(len(d))

# max：返回最大值
print(max(d))

# min：返回最小值
print(min(d))

# str :返回字典的字符串格式
print(str(d))
print(type(str(d)))# 查看类型

# clear:清空字典
d ={"one":1,"two":2,"three":3}
print(d.clear())# 清空之后并不会返回一个空的dict，而是直接None

# items：犯罪字典的键值对组成的元祖格式
d = {"one":1,"two":2,"three":3}
i = d.items()
print(i)
print(type(i))# 查看类型

# keys:返回字典的键值组成的一个结构
d = {"one":1,"two":2,"three":3}
k = d.keys()
print(k)
print(type(k))

# values:返回字典键值对应的值组成的一个结构
d = {"one":1,"two":2,"three":3}
v = d.values() 
print(v)
print(type(v))

# get:根据指定键值返回相对应的值，好处是可以设置默认值
d =
