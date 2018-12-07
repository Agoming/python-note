# 四大内置数据结构
      # list 列表
      # set  集合
      # dict 字典
      # tuple 元祖

# 本章大纲
# list(列表)
#     一组由顺序的数据的组合
#     创建列表
#          有值列表
#          无值列表（空列表）
#          使用list创建列表
#          修改列表值
#     列表常用操作
#          访问列表
#               使用下标操作(索引)，大部分语言索引都是从0开始
#               列表位置从0开始
#               语法: list[val]
#          分片操作（截取操作）
#               从列表里截取任意一段
#               语法: list[开始:结束]
#          del(删除命令)
#          列表的连接
#               使用乘加来对列表操作
#               列表成员资格运算
#          列表的遍历使用
#               使用for和while来遍历，对比过程
#               双层列表循环
#          列表内涵：list content
#          关于列表的常用函数
#               len(list)获取列表长度
#               mxn(list)求列表最大值
#               min(list)求列表最小值
#               list(str)把字符串拆分成字符并存入列表里面
#               list.append(val)在列表尾部追加内容
#               list.insert(index,val)在指定下标前面插入内容
#               list.pop(index) 取出指定下标的值
#               list.remove(index.max)删除指定下标的内容
#               list.clear()清空列表里面的内容
#               list.reverse()f翻转列表类容，原地翻转地址不变
#               list.extend(list2)拓展列表，把一个列表拼接到另一个后面
#               list.count()查找列表中相同指定值或元素的数量
#               list.copy()浅拷贝
#               copy.deepcopy(list)深拷贝
# 空列表案例

l1 = []
print(type(l1))
print(l1)

# 带值列表案例
l2 = ["1","2","lalla","啦啦啦"]
print(type(l2))
print(l2)

# 使用list()来创建,list()只能用来创建空列表
l3 = list()
print(type(l3))
print(l3)

# 修改列表内容
l = [1,2,3,4,5]
l[1] = 100
print(l[:])

# 修改一部分列表的内容
l = [1,2,3,4,5]
l[1:3] = 100,200
print(l)
# 列表常用操作
      # 访问列表
           # 使用下标操作(索引)，大部分语言索引都是从0开始
           # 列表位置从0开始
           # 语法: list[val]
      # 分片操作（截取操作）
           # 从列表里截取任意一段
           # 语法: list[开始:结束]
      # del(删除命令)
      # 列表的连接
            # 使用乘加来对列表操作
            # 列表成员资格运算
      # 列表的遍历使用
            # 使用for和while来遍历，对比过程
            # 双层列表循环
      # 列表内涵：list content
      # 关于列表的常用函数
# 下标访问列表案例
l = [1,2,4,123,3]
print(l[3])# 下标从0开始，所以截取的下标3为第四个

# 分片操作
# 注意截取范围，一般来说有开始和结束两个下标值都是包括左不包括右
# 案例如下
l = [1,2,4,123,3]
print(l[1:4]) # 截取从第二个到第四个

# 下标值可以为空，如果不屑，左边下标值默认为0，右边下标值默认为最大数加一，也就是说截取到最后一位
# 注意最终打印的结果
# 左右下标完全不写
l = [1,2,4,123,3]
print(l[:])

# 只写左边下标
l = [1,2,4,123,3]
print(l[1:])

# 只写右边下标
l = [1,2,4,123,3]
print(l[:4])

# 分片操作可以控制增长幅度，默认增长幅度为1
l = [1,2,4,123,3]
print(l[1:6:1])

# 打印从下标1到4的数字，每次遍历中间隔开一个
print(l[1:4:2])

# 下标索引可以超出范围，不过超出后不会提示错误并且不考虑多余下标内容
print(l[1:100])

# 下标值和增长幅度可以为负数
# 当下标值为负数时，索引遍历的顺序就会相反，即从右到左
# 当下标值为负数时，列表里最后的内容下标为-1

# 分片操作 下标值为负，案例如下
# 无论下标值是否为负，左边的下标值一定要比右边的下标值小
print(l[-2:-4]) # 执行结果为空
print(l[-4:-2])

# 如果分片的左边下标值要比右边下标值大，则增长幅度要使用负数
# 此案例为一个list直接正反颠覆提供了一种思路
print(l[-2:-4:-1])


# 分片操作是生成一个新的list
       # 内置函数id，负责显示一个遍历或数据的唯一确定编码

# 先解释一下id函数
a = 100
b = 200

# 从得出的值判断是否同一个变量
print(id(a))
print(id(b))
# 通过a来对c赋值，再对比a和c的编码是否相同
c = a
print(id(c))
# 这里更改了a的值，按照逻辑，c的值也应该更改，但是我们看编码，c的值并没有发生变化，这就是顺序结构的影响，c所接收的值是还没更改的a的值，再a更改过后，c并未接收到指令需要再次更改
a = 101
print(id(a))
print(id(c))
# 当c再次接收指令需要更改值时的编码
c = a
print(id(a))
print(id(c))
print(id(a)==id(c)) # 返回的结果为true

# 使用id内置函数来判断截取的list是否是新生成的列表
l = [3,2,1,23,3]
ll = l[:] # 通过截取方式赋值
lll = l# 直接进行赋值

# 对比三者的编码
print(id(l))
print(id(ll))
print(id(lll))# 很明显，直接赋值的编码跟原来的list完全一致

# 我们再次通过修改列表的内容,来证实
l[1] = 100
print(l)
print(ll)
print(lll)
# 通过结果可以看出截取的list并未发生任何变化，反之直接赋值的list就跟原本list发生了相同的变化

# del 删除命令
     # 语法:
          # del 列表名称[需要删除内容的下标]
a = [1,2,3,4,5]
del a[2]
print(a)

# 利用id内置函数查看删除过后的list是否还是原来的列表，还是系统给重新生成了一个
a = [1,2,3,4,5]
print(id(a)) # 删除前
del a[2]
print(id(a)) # 删除后
# 从id给的编码看得出来，并没有不同，证明删除的内容是直接从list里删除，而不是将不需要删除的内容重新放置到一个新的list里面

# del删除了一个变量之后不能再继续使用该变量
a = [1,2,3,4,5]
del a
# print(a)# 删除列表类型的变量

b = 1
del b
# print(b)# 删除普通变量
# 无论删除任何类型的变量，后面都不能再继续使用该变量

# 列表的连接使用

# 使用加号连接两个列表
# 直接相加即可
a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = a + b
print(c)

# 使用乘号操作列表
# 列表直接与一个整数相乘
a = [1,2,3,4,5]
b = a * 3
print(b)
# 得到的值相当于n和相同的列表相加

# 列表成员资格运算
# 使用in成员运算符进行操作(关于in函数前面"表达式章节有讲")
a = [1,2,3,4,5]
b = 8
print(b in a)# 返回值为布尔值

# 使用not in进行操作
a = [1,2,3,4,5]
b = 8
print(b not in a)

# 列表的遍历
       # for
       # while(凡是关于遍历的大都不推荐)

# 使用for进行遍历操作
# 案例如下
a = [1,2,3,4,5]
for i in a:
    print(i)# 通过遍历打印
    # 对比两种打印之后值的类型
    print(type(i))
print(a)# 直接打印
print(type(a))
# 通过遍历打印和直接打印的最大区别是，前者把整个列表拆散，一个一个去访问里面的值然后进行打印，后者直接看作一个整体进行打印
# 我们可以看到遍历打印之后的值是int类型，而直接遍历的值为list类，看得出来拆分过后的值类型是按照原本它在列表时的类型进行输出

# 有个很有意思的东西，分享给大家，这是大拿老师分享给我们的
# java， c++ 程序员写的python代码是这样的
a = [1,2,3,4,5]
for i in range(0,len(a)):# 他们会把a(列表)看成一个值，把列表的内容获取之后存入range再通过for进行打印
    print(a[i])
    i += 1

# 使用while循环访问list(麻烦死了=-=)
# 不推荐使用while遍历list
# len() 返回对象（字符、列表、元组等）长度或项目个数
a = [1,2,3,4,5]
# 定义index表示list的下标
index = 0
while index < len(a):
    print(a[index])# 将第index个a进行打印
    index += 1# 让下标每遍历一次就进行下一个下标的遍历


# 双层列表循环
a = [["zhansan",12,"游戏"],["lisi",13,"游泳"],["wangwu",15,"篮球"]]
# 打印方法：每个列表有多少个值就用多少个变量进行带出
for k,v,w in a:
    print(k,"--",v,"--",w)

# 循环变量的个数应该于列表解包出来的变量个数一致
# a = [["zhansan",12,"游戏"],["lisi",13,"游泳"],["wangwu",15,"篮球",1,2,3,4,]]
# # 打印方法：每个列表有多少个值就用多少个变量进行带出
# for k,v,w in a:
#     print(k,"--",v,"--",w)

# 列表内涵:list content
       # 通过简单方法创作列表

# 通过for遍历出来的值放置到一个新的列表里面来形成一个列表
a = [1,2,3,4]
# 通过list a 来创建新的list b
b = [i for i in a]
print(a)
print(b)
# 对比id编码是否相等
print(id(a))
print(id(b))
# 通过编码我们可以看出就算b列表的值是从a列表里面获得的，但是编码显示它们不是同一个变量

# 在生成新的列表时，使用乘号对列表值进行操作
# 让b里面的所有值乘以10
a = [1,2,3,4,5]
b = [i*10 for i in a]
print(a)
print(b)


# 还可以通过算法将过滤的内容放置新列表
# 使用for i in range生成从1到34的列表a，将列表a里面的偶数生成一个列表b
a = [i for i in range(1,34)]
b = [r for r in a if r%2 == 0]
print(a)
print(b)

# 列表生成式可以嵌套
a = [i for i in range(1,5)]# 生成 list a
b = [i for i in range(100,500) if i % 100 == 0]

# 将a和b列表里面的值对应相加并且放置新列表c里面
# n将a列表内容逐个遍历，m将b列表内容逐个遍历
c = [n+m for n in a for m in b]
# 分别打印a,b,c列表对比内容
print(a)
print(b)
print(c)

# 将c里面的表达式详细版:案例如下
# 其实就是个嵌套循环
for n in a:
    for m in b:
        print(m+n,end=" ")# end是print内置函数的一个参数，规定空格，默认值end="\n"

# help(print)# 查看print的官方帮助文档，help(函数名) = 查看该函数的官方帮助文档

# 关于列表的常用函数

# 求列表长度
# len(变量)
a = [x for x in range(1,100)]
print(len(a))

# 求列表中最大值
# mxn(变量)
a = [x for x in range(1,100)]
print(max(a))

# 求列表中最小值
# min(变量)
a = [x for x in range(1,100)]
print(min(a))

# 如果获取列表最大值的类型为str，则选择字符最长的为最大值
a = ["a","ab","abc"]
print(max(a))
# min同理
print(min(a))

# 将一段字符串拆分成个体并且赋值给列表
# list(变量)
s = "Baby, there's nothing holding me back"
print(list(s))

# 把range产生的内容转化成list
print(list(range(1,10)))

# append 插入一个内容，在末尾追加
a = [i for i in range(1,10)]
print(a)# 追加前
a.append(100)
print(a)# 追加后

# insert 在指定位置插入内容
# insert(index,data)，插入位置是index前面
a = [i for i in range(1,10)]
print(a)
a.insert(3,100)# 在下标为3的前面插入一个内容
print(a)

# 删除
# del 和 pop的区别，前者为直接删除，后者为取出
# del删除，直接在列表里面删除
a = [i for i in range(1,10)]
print(a)
# del a
# print(a)# 删除之后无法调用

# pop，从对应的下标位置取出一个元素，取出的元素为最后一个
print(a.pop())

# remove在列表中删除指定的值
# 如果被指定要删除的值没在list中，则会报错
# 所以在使用remove时，最好使用先行判断
# 查看remove操作时直接从列表里面进行删除，还是将值取出来放置到一个新的list里面
a = [i for i in range(1,10)]
print(id(a))# 删除前
aa = 8# 指定一个值
if aa in a:
    a.remove(aa)
print(a)
print(id(a))# 删除后

# clear清空
# 使用clear来清空，我们可以看到列表还在，而且里面的地址也是一致的
a = [i for i in range(1,10)]
print(a)
print(id(a))
a.clear()
print(a)
print(id(a))
# 如果不计较地址问题时，我们可以直接使用空的list去替换掉，但这时地址就不一致了
a = []
print(a)
print(id(a))


# reverse:翻转列表内容，原地翻转
a = [1,2,3,4,5]
print(a)# 翻转前
print(id(a))
a.reverse()
print(a)# 翻转后
print(id(a))# 翻转过后还是同一个列表

# extend：拓展列表，两个列表，把一个直接拼接到后一个上
a = [1,2,3,4]
b = [6,7,8,9,10]
print(a)# 拼接前
print(id(a))
a.extend(b)
# print(a)# 拼接后
# print(id(a))
print(a+b)# 使用拼接手法来拓展列表，能使拓展列表原来的地址保存，而直接相加来拓展，则会生成一个新的列表
print(id(a+b))

# count:查找列表中指定值或元素的个数
a = [1,2,3,3,4,2]
print(a)
print(a.count(2))# 列表中有两个2

# copy：拷贝，此函数是浅拷贝
# 关于拷贝和直接赋值的区别
# 直接赋值案例：
a = [1,2,3,4,5]
b = a
print(id(a))
print(id(b))
# 直接赋值的id是一致的，那就是说无论在何处修改修改a或b另一个都会发生改变
b[3] = 111
print(a)
print(b)

# 拷贝案例
a = [1,2,3,4,5]
b = a.copy()
print(id(a))
print(id(b))
# 通过a拷贝的b列表里面的id与a列表完全不符合，这就可以在修改a或b时不会影响到另一个列表了
a[1] = 888
print(a)
print(b)

# 浅拷贝和深拷贝的区别
# copy函数只是个浅拷贝函数，只拷贝一层内容
a = [1,2,3,[1,2,3,4]]
b = a.copy()
print(id(a))
print(id(b))
# 这时使用id函数访问a列表里面的双层列表
print(id(a[3]))
print(id(b[3]))
# 由此可见，浅拷贝无法拷贝双层列表里面的内容
# 我们通过修改来查看区别
# 修改双层列表内容
a[3][2] = 636
print(a)
print(b)
# 修改列表内容
a[1] = 111
print(a)
print(b)
# 只有双层列表里面的内容可以被修改

# 使用深拷贝来拷贝双层列表
# 引入copy库
import copy
a = [1,2,3,[1,2,3,4]]
b = copy.deepcopy(a)
print(a)
print(id(a))
print(b)
print(id(b))
# 再查看双层列表的id
print(id(a[3]))
print(id(b[3]))
# 这时双层列表内容的id也发生了变化
# 通过改变a双层列表里面的内容来观察变化
a[3][2] = 666
print(a)
print(b)
# 这时b列表的双层列表并没有发生变化，这就是浅拷贝和深拷贝的区别

# 关于传值和传址的区别
def int(n):
    n += 100
    print(n)

def list(n):
    n[2] = 100
    print(n)
    return None

n1 = 1
n2 = [1,2,3,4,5]

print(n1)
int(n1)
print(n1)

print(n2)
list(n2)
print(n2)
# 我们可以看到两个函数，经过函数改变之后，函数局部打印和全局打印列表是一致的，反之int方面则不同
# 因为对于列表来说传入的参数为传址，所以在全局打印时访问的地址和局部的相同，则打印的内容也相同
# 而int传入的参数为传值，因为局部访问时访问的是参数的值，当全局访问时无法获得经过函数改之后参数的值，所以值没发生改变

