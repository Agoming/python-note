# 四类参数
#      普通参数
#      默认参数
#      关键字参数
#      收集参数
#          关键字收集参数

# 普通参数
# 普通参数又名为位置参数，没有默认值，根据具体使用位置进行传值
# 普通参数和默认参数的不同
# 普通参数就是如同名字一般普通,没有默认值
# 而默认参数则可以规定默认值（也就是规定了默认值的普通参数而已）
# 但是默认参数要牢记一点：默认参数必须指向不变的对象值
# 请看下面例子

def  add_end(L=[]):
    L.append('END') # 这里已经添加了一个END
    return L

# 正常调用
print (add_end([1,2,3]))  # [1, 2, 3, 'END']

# 使用默认参数调用时，一开始也是对的，但是再次调用时，结果就不一样了
print (add_end())  # ['END']

print(add_end())  # ['END', 'END']

print(add_end()) # ['END', 'END', 'END']
# 也就是说赋值给默认参数的对象应该为常量

# 如果需要修改正确，则需要判断传入时参数是否为空
def  add_end2(L=None):
    if L is None:# 这里的is是身份函数的一种，请翻回上一篇“变量”文章
        L=[]
    L.append('END')
    return  L



# 关键字参数
    # 语法
    #       def func(p1=v1,p2=v2):
              # 语句1
              # 语句2
    # 调用函数：
    #       func(p1=value1,p2=value2)

# 好处：不容易混淆。一般实参和形参只是按照位置，一一对应即可，容易出错，使用关键字参数，可以不考虑参数位置
# 坏处：比较麻烦

# 关键字案例
# 打印基本信息
def stu(name,age,addr):
    print("我是{0},我今年{1}，我住在{2}".format(name,age,addr))

# 定义参数值
n = "zhansan"
a = 18
addr = "广州"
# 普通参数传递，只按照位置传递，容易出错
stu(a,n,addr)
# 关键字传递，虽然麻烦，但是不容易出错
stu(age=a, name=n, addr=addr)

# 收集参数
# 把没有位置，不能和定义时的参数位置相对应的参数，放入一个特定的数据结构(tuple)中
# 语法
#        def func(*args):
#               func_body
#               按照tuple使用方式访问args得到传入的参数
#        调用：
#        func(p1, p2, p3, .....)
# 参数名args不是必须怎么写的，但是推荐使用（约定俗称）
# 收集参数参数名前需要带有星号(*)
# 收集参数可以和其他参数共存，事实上全部类型参数都可以同时出现在同一个函数里面

# 收集参数案例
# 函数模拟学生自我介绍，但是并不是每个学生都有相同的喜好，有的多，有的少
# 把收集参数看作一个tuple
# type为查看内容的类型
# type语法： type(args) args=需要查询的内容
def stu(*args):
    print("hello,大家好，我先做下自我介绍：")
    print(type(args))# 查看args(收集参数)的类型
    for item in  args: # 因为收集函数是一个tuple，所以使用循环将其全部打印
        print(item)

# 调用收集参数
# 有同学介绍内容多
stu("zhangsan",18,"广州","篮球","游戏")
# 有同学介绍内容不多
stu("lisi")# 即便只有一个值也使用tuple进行收集
# 收集的内容也能为空
stu()

# 使用关键字参数的格式进行调用，则会出错
# stu(name="wangwu")# 当前我们自己知道那个是name(没有设定)


# 关键字收集参数
# 把关键字参数按字典(dict)格式存入收集参数
# 语法
#       def func(**kwargs):# 注意是双（*）星号
#            func_body
#      # 调用：
#       func(p1=v1, p2=v2, p3=v3........)
# kwargs也是约定俗成
# 调用的时候，把多余的关键字参数放入kwargs
# 访问kwargs需要按字典格式访问

# 收集关键字参数案例
# 同上自我介绍
# 调用的时候需要使用关键字参数格式调用
# dict里面的items方法返回列表里面可遍历的元素数组
def stu(**kwargs):
    print("hello,大家好，我先做下自我介绍：")
    print(type(kwargs))# 查看收集关键字参数的类型
    for k,v in kwargs.items():# 有两个变量进行循环原因是，不仅仅需要打印参数的值，连同关键字参数的参数名也要打印
        print(k+"---"+v)# 使用---将其分割开来，好看清楚

stu(name="zhangsan",age="18",addr="广州",lover="游戏",lovers="篮球")
print("分割线"+"*"*20)
stu(name="wangwu")


# 关于各类参数调用的顺序问题
# 之前就说过，收集参数，关键字参数，普通参数，默认参数，关键字收集参数
# 使用规则：普通参数，默认参数，收集参数，收集关键字参数
# 混合参数使用案例
def stu(name,age,hobby="没有",*args,**kwargs):# name,age=位置参数，hobby=默认参数，*args=收集参数，**kwargs=收集关键字参数
    print("大家好，我再次介绍一下自己")
    print("我叫{0},今年{1}".format(name,age))
    if hobby == "没有":
        print("对不起，我莫的爱好")
    else:
        print("我的爱好是{0}".format(hobby))
    for i in args:
        print("我住在{0}".format(i))
    for k,v in kwargs.items():
        print("我还有爱好{0}".format(v))

# 开始调用
name = "zhansan"
age = 18
# 示范三种不同的调用方法
stu(name,age)
stu(name,age,hobby="游戏")
stu(name,age,"广州","萝岗区",hobby2="游戏",hobby3="篮球")


# 收集参数的解包问题
     # 把参数放入list和dict中，直接把list和dict的值放入收集参数中

# 解包案例
def stu(*args):
    print("哇哈哈哈")
    # 这里声明一个对象来查看，到底遍历了多少次收集参数
    n = 0
    for i in args:
        print(type(i))
        print(n)
        n += 1
        print(i)
l = ["zhangsan",19,23,"lisi"]# 解包=将元祖或列表转化为字符串的过程呈现
stu(*l)
l2 = ("zhangsan",19,23,"lisi")
stu(*l2)
# 收集关键字参数的解包问题
       # 对dict类型进行解包
       # 需要使用两个星号进行解包

# 解包案例
def stu(**kwargs):
    n = 0;
    for k,v in kwargs.items():
        print(type(v))
        print(n)
        n += 1
        print(k+"---"+v)
l1={'name':'zhangsan','age':"12",'names':'lisi','ages':'23'}# 定义字典
stu(**l1)

# 返回值
   # 函数和过程的区别
         # 有无返回值
   # 需要使用return相似返回内容
   # 如果没有返回，则默认返回None
   # 推荐写法，无论有无返回值，最后都以return结束（毕竟可以None）

# 返回值案例:有无返回值赋值的区别
def func_1():
    print("有返回值")
    return 1

def func_2():
    print("无返回值")

f1 = func_1()
print(f1)

f2 = func_2()
print(f2) # 在无返回值的情况下，系统默认返回None

# 函数文档
   # 函数的文档的作用是对当前函数提供使用相关的参考信息
   # 文档的写法：
        # 在函数内部开始的第一行使用三引号(''' '''，""" """)字符串定义符
        # 必须在函数的首行，经过验证前面有注释性说明是可以的，不过最好函数文档出现在首行
        # 具体格式:
             # 第一行：函数名称
             # 第二行：函数具体功能
             # 第三行：参数名称以及内容
             # 第四行：是否有返回值
   # 文档查看：
        # 是固体不过help函数，形如 help(func)
        # 使用doc
        # help和doc的区别：help的文档查看带有返回值

# 文档写法案例
# 介绍文档内容
def stu(name=10,age=10): # 文档会自动帮我们打印参数信息
    '''
    这是我的文档内容
    :param name:
    :param age:
    :return:
    '''
    print("函数调用成功")# 测试函数是否能成功调用
stu()

# 使用help文档查看案例
print(help(stu))

# 使用doc文档查看案例
print(stu.__doc__)