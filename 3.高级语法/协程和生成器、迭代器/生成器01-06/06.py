# encoding:utf-8
def triangles():
    N = [1] # 作为整个杨辉三角的第一个实数
    while True:
        yield N # 生成器返回值
        S = N[:] # 将N列表的东西赋值给S 方便统计行数长度
        S.append(0) # 作为每次循环生成下一个数的加入成员
        N = [S[i - 1] + S[i] for i in range(len(S))]# 第一行有一个0所以循环一次，s[1 - 1] +s[1] = s[1],但是原本N里面就有一个 1 ,所以次一次生成过后的列表值为[1,1]

n = 0
results = []
for t in triangles(): # 这个循环只是将上面获得的数据分好一行一行
    print(t)
    results.append(t) # 将遍历出来的数据放置到results列表
    n = n + 1
    if n == 10: # 当遍历次数达到10此就退出
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')