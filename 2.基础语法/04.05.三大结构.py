# 三大结构
    # 顺序
    # 分支
    # 循环

# 分支
   # 分支的基本语法
        # if 条件表达式:
        # 语句1
        # 语句2 等等....
   # 条件表达式就是计算结果必须为布尔值的表达式
   # 不同于java，python分支表达式使用了冒号来代替大括号
   # 注意表达式后面出现的语句，如果属于同一级别，则必须同一距离缩进
   # 条件表达式结果为True执行下面同一级别的语句块
   # 关于条件表达式的运算符是比较运算符(如不知道请去找字符串+变量的文章)
   # if语句可以嵌套使用，但不推荐
   # python没有switch-case语句，乖乖用if吧

# if语句例子
# 条件：如果age小于18岁，则打印“你还未成年，请去请示你家长”

age = 17
if age < 18:
    print("你还未成年，请去请示你家长")


# 关于if语句级别问题
age = 18 # 我们可以在这里测试一下
if age < 18:
    print("你还未成年，请去请示你家长") # 下面的句子与if为同一级别，所以不进入if的判断机制
print("这个句子不进入if判断语句中")

# 双向分支
    # if..else..语句
          # 语法：
          # if 条件表达式:
               # 语句1
               # 语句2
          # else:
               # 语句1
               # 语句2
    # 双向分支由两个分支，当程序执行到if...else语句的时候，一定会执行其中一个，也仅仅执行一个(如果你的双向分支语句两个分支都没执行，那一定是你程序问题)
    # 缩进问题,else和if是同一级别，其余的语句也同一个级别

# 双向分支例子
age = 18
if age < 18:
    print("你还未成年，请去请示你家长")
else:
    print("你已经成年，需要担负成年的责任了")

# 多路分支
   # 当双向分支已经不足以去判断很多分支的情况下，请使用多路分支
   # 多路分支语法
          # if..else..语句
          # if 条件表达式:
               # 语句1
               # 语句2
          # elif 条件表达式:
               # 语句1
               # 语句2
               # ...
          # else:
               # 语句1
               # 语句2

# 使用双向分支去完成多路分支的工作 例子:
# input()：在控制台商输出括号内的字符串，接收用户在控制台上输入的内容并返回(返回的值一定是字符串类型)
# 例子条件
# 90以上： 输出优秀
# 80-90：良
# 70-80：中
# 60-70：平
# 60以下： 输出：请补考
# 这样子显得代码很繁杂，没有联动性
# score = input("请输入你的成绩:")
# score = int(score)# 将字符串转化为整数
# if score >= 90:
#     print("优秀")
# if score < 90 and score >= 80:
#     print("良")
# if score < 80 and score >= 70:
#     print("中")
# if score < 70 and score >= 60:
#     print("平")
# if score< 60:
#     print("请补考")

# 还是刚刚的例子，这次用多路分支来实现
# score = input("请再次输入你的成绩:")
# score = int(score)
# if  score >= 90: # 是不是感觉清晰很多
#     print("优秀")
# elif score >= 80:
#     print("良")
# elif score >= 70:
#     print("中")
# elif score >= 60:
#     print("平")
# else :
#     print("请补考")


# 循环语句
    # 重复执行某些固定动作或者处理基本固定的事物
    # 分类
       # for循环
         # for循环语法：  (不同于java C#，python的for语法跟foreache相似)
            # for 变量 in 序列:
                # 语句1
                # 语句2
                # ....
       # while 循环
          # 表示当某条件成立的时候，就循环
          # 不知道具体循环次数，但能确定循环的成立条件的时候用while循环
          # while语法：
            # while 条件表达式：
                # 语句1


# 序列=一列数字或者其他值，一般用中括号"[]"表示
# 例如 ['haha','hihi','wawa']
# for循环例子:
# 条件：打印学生列表姓名
for name in ['zhangsan','lisi','wangwu']:
    print(name)

# for循环嵌套if语句使用
for name in ['zhangsan','lisi','wangwu']:
    if name == "wangwu":
        print("{0}同学犯错了，请罚站".format(name))
    else :
        print("{0}同学做的不错，奖励".format(name))

# range
    # 生成一个数字序列
    # 具体范围可以设定
    # 在python，如果有表示数字范围的两个数，一般左边的数字为首，右边的数字为尾但是不包含
    # range函数在python2和python3里面右严重的区别（这里以python3为例子）

# range例子
# 条件：打印1到10的数字
for i in range(1,11):
    print(i)

# for-else语句
    # 当for循环结束的时候，就会执行else语句（跟if有区别，前者是当for执行完才执行，后者是只执行一个）
# 我个人喜欢数字3 ，所以当循环到数字3时候就打印出来，其他则打印"我不喜欢这个数字"，在整个循环结束之后打印“我热爱数字”这句话
for i in range(1,11):
    if i == 3:
        print("我喜欢数字{0}".format(i))
    else: # 这里请看仔细，两个else的阶级是不一致的，一个是if的else，一个是for的else
        print("我不喜欢这个数字")
else:
    print("我热爱数字")

# 关于循环的关键字：break ，contineu ， pass
       # break ：无条件结束整个循环，简称循环猝死
       # continei: 无条件结束本次循环，重新进入下一轮循环
       # pass:表示略过，通常用于占位

# for 循环中的变量表示，一般用i,k,m,n之类的（约定俗成）
# 如果循环变量不重要，可以用下划线（_）表示
# break关键字例子
# 在数字1到10里面寻找3，找到之后打印并且马上结束循环，可以避免过多的进程
for _ in range(1,11):
    if _ == 3:
        print("我找到了{0}".format(_))
        break
    else:
        print(_)# 打印到2

# contineu关键字例子
# 在数字1到10里面寻找所有偶数，并且打印出来
a = 1
for i in range(1,11):
    if i%2 == 1:
        continue; # 直接本次循环结束，也不进行a的运算
        a += 1;
    else:
        print("{0}是偶数".format(i))
        print("a的值为{0}".format(a)) # 如果a的值大于1，则代表没有结束循环

# 有时候，能运用一些细节来缩写代码达到同样的效果
for i in range(1,11):
    if i%2 == 0: # 直接判断是否为偶数，而不是进行筛选
        print("{0}是偶数".format(i))

# pass关键字
# 运用pass关键字进行占位
# 很多时候我们创建一些函数或者循环等等是觉得在后面会有用，但是目前来说不确定里面怎么运算，空着呢又会出错，这时就需要pass来进行占位
for i in range(1,2):
    pass

# while循环列子
# 年利率是6.7%，本利是每年翻滚，则多少年后本钱会翻倍
# 当前知道年利率（循环条件），不知道多少年（循环次数）
year = 0
qian = 100000
while qian < 200000: # 利用知道本钱这个循环条件来建立循环
    year += 1
    qian = qian*(1+0.067)
    print("第{0}年，我现在有{1}".format(year,qian))

# while...else，和for...else...用法一样
# 条件跟前面一致，当本钱翻倍时候，就用print庆祝一下
year = 0
qian = 100000
while qian < 200000:
    qian = qian * (1+0.067)
    year += 1
    print("第{0}年，我现在有{1}".format(year,qian))
else: # 当前else和while处于同一级
    print("终于翻倍了，不容易啊")

# 顺序结构
    # 在不包含分支结构(条件判断)，循环结构(for ,while)情况下一步一步往下执行