# 变量作用域
#      变量由作用范围限制
#      两种不同的作用域:
#            全局(global):在函数外部定义
#            局部(local):在函数内部定义
#      变量的作用范围
#            全局变量
#                 在整个程序范围都有效
#                 全部变量可以在局部范围里面使用（即函数内部可以方位函数外部定义的变量）
#                 局部变量在局部范围内可以使用
#                 局部变量无法在全局范围内使用
#      LEGB原则
#            L（Local）局部作用域
#            E（Enclosing function locale）外部嵌套函数作用域(命名空间)
#            G（Global module）全局变量，函数定义所在模块的命名空间
#            B（Buildin）:python内置作用域或又名 内部建模的命名空间

# 全局变量和局部变量例子

glo = "我是全局"
def func():
    print(glo) # 在函数内部调用全局变量
    print("*"*20)
    loc = "我是局部" # 定义局部变量
    print(loc)# 在函数内部调用局部变量

func()# 调用函数，查看函数内部调用内容
print("下面为全局范围的调用")
print(glo)# 在全局范围里调用全局变量
# print(loc)# 在全局范围里调用局部变量，但是无法调用，会报错


# 如何把局部变量提升为全局变量
    # 使用global
    # 使用格式：
          # global val    (val为局部变量名字)

# 案例,我复制了上面的例子进行修改，把loc能在全局范围里调用
glo = "我是全局"
def func():
    print(glo) # 在函数内部调用全局变量
    print("*"*20)
    global loc # 为loc局部变量提升为全局变量
    loc = "我是局部" # 定义局部变量
    print(loc)# 在函数内部调用局部变量

func()# 调用函数，查看函数内部调用内容
print("下面为全局范围的调用")
print(glo)# 在全局范围里调用全局变量
print(loc)# 不知道什么原因，尽管可以调用，但是pycharm这里还是显示变量为红色(报错)，但是可以运行


# 如何查看整个程序有多少局部或全局变量
       # 通过globals和locals显示
       # global和locals都为内建函数(系统给的)

# 查看变量案例
# 因为程序内部可能没有这么多局部函数,所以我们先定义一些
a = 1
b = 2
def func(d,e):
    c = 3
    print(locals())
    print(globals())

func(100,200)
# 最终打印
    # 局部变量为 d e c，这样我们可以发现从调用里面传入的参数值也是函数内部的局部变量，而a,b是我们在全局范围里定义的，所以并没有定义
    # 全局变量则一大堆，因为这些都是系统附带的，一个程序的允许，需要一推东西，而这堆东西系统都准备好了

# eval()函数
     # 把一个字符串当成一个表达式来执行，返回表达式执行后的结果
     # 语法:
         # eval(string_code,globals=None,locals=None)
# exec()函数
     # 跟eval功能相似，但是不返回结果
     # 语法：
         # exec(string_code,globals=None,locals=None)

# 使用字符串进行算术 案例如下
x = 199
y = 1
z1 = x + y # 使用值来计算
z2 = eval("x+y") # 用字符串来计算

# 最后比较一下两个计算是否相等
print(z1)
print(z2)
print(z1 == z2)# 值为true
print(type(z2))# 返回值的类型为int

# 使用exec来计算 案例如下
x = 199
y = 1
zi = x + y
# 在exec中打印结果，注意看字符串引号的用法
# 对比exec执行过程和执行结果
z2 = exec("print('x+y:',x+y)")
# 在打印过程中，exec内部的print先打印，因为还没经过exec所以带有结果，我们可以看到结果为200
print(z1)
print(z2)
print(z1 == z2)# 因为最终结果返回值为None，所以不相等
print(type(z2))# 因为结果是None,所以无类型


# 递归函数
#    函数直接或者间接调用自身
#    优点：简洁，容易理解
#    缺点：对递归深度有限制，过多会导致消耗资源
#    python对递归深度有限制(自我调用997次)，超出限制自动报错

# 测试python递归深度的限制
# a = 1
# def func():
#     global a
#     a += 1
#     print(a)
#     func()
#
# func()
# 所以在使用递归时候一定要注意结束条件，否则会崩溃+浪费资源

# 举一个带有结束条件的例子
# 斐波那契数列
# 一列数字，第一个值是1， 第二个也是1， 从第三个开始，每一个数字的值等于前两个数字出现的值的和
# 数学公式为： f(1) = 1, f(2) = 1, f(n) = f(n-1) + f(n-2)
# 例如： 1,1，2，3,5,8,13.。。。。。。。。

# n表示求第n个数子的斐波那契数列的值
def func(n):
    # 进行第一和第二次值为1 2 的递归时如果不使用指定返回值的话，后面无法进行递归运算
    if n == 1:
        return 1
    if n == 2:
        return 1
    return func(n-1)+func(n-2)
    # 如果n等于1，不加判断使其获得返回值时，表达式为 func(1-1)+func(1-2) 则func(0)和func(-1)，慢慢变负数，无法获得返回值，最终超出递归深度
    # 简单来说，两个判断句就是用来修正n不会变成负数
print(func(3)) #  1,1,2 我求的是第三位，所以等于3、

# 但是n一开始就为负数，如何修正
# 修正问题：
    # 1.让传入的值去除负号
    # 2.让传入的值不再进入递归
    # 两种方法都行
def fab(n):
    if n >= 0:
        if n <= 2:
            return 1
        else:return fab(n-1)+fab(n-2)
print(fab(-4))

# 关于递归限制问题
# 使用sys库里面的setrecursionlimit(val)函数可以解决
# import sys
# sys.setrecursionlimit(1000000)