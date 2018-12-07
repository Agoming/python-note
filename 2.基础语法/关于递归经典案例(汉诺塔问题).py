# 汉诺塔问题
   # 一共A,B,C三座塔，将A塔上面所有的盘子移动到C塔上面
   #  n：代表几个盘子
   #  a：代表第一个塔，开始的塔
   #  b：代表第二个塔，中间过渡的塔
   #  c：代表第三个塔, 目标塔
   # 规则：(我们将塔比喻成盘子)
        # 1.每次移动一个盘子
        # 2.任何时候大盘子都在下面，小盘子在上面
   # 方法:
        # 1. n = 1 :直接把A上的一个盘子移动到c上，A -> C
        # 2. n = 2 :
                 # 把小盘子从A放到B上， A->B
                 # 把大盘子从A放到C上， A->C
                 # 把小盘子从B放到C上， B->C
        # 3.n = n(大于2):
                 # 1.把A上的n-1个盘子，借助于C，移动到B上去，调用递归
                 # 2.把A上的最大盘子，也是唯一一个，移动到C上，A->C
                 # 3.把B上n-1个盘子，借助于A，移动到C上， 调用递归


# 当n = 1
a = "A"
b = "B"
c = "C"
def ta(n,a,b,c):
    if n == 1:
        print(a+"->"+c)
        return None

# ta(1,a,b,c)

# 当n = 2
a = "A"
b = "B"
c = "C"
def ta(n,a,b,c):
    if n == 1:
        print(a+"->"+c)
        return None
    if n == 2:
        print(a+"->"+b)
        print(a+"->"+c)
        print(b+"->"+c)
        return None

ta(2,a,b,c)

# 当n = 3或者更多
a = "A"
b = "B"
c = "C"
def ta(n,a,b,c):
    if n == 1:
        print(a+"->"+c)
        return None
    if n == 2:
        print(a+"->"+b)
        print(a+"->"+c)
        print(b+"->"+c)
        return None
    ta(n-1,a,c,b)# 让它的盘子数量-1进入递归
    print()