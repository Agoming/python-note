# random
  # 随机数
  # 所有的随机模块都是伪随机

import  random

# random 获取0-1之间的随机小数
# 返回值 随机0-1之间的小数

print(random.random())

# randint 生成随机整数
# randint（a,b） 包含左 不包含右
print(random.randint(0,101))

# choice 随机返回序列中的某个值
r = random.choice([i for i in range(1,10)])
print(r)

# shuffle 随机打乱列表
# 返回值:返回打乱的列表
l = [i for i in range(10)]
print(l)# 原列表
random.shuffle(l)
print(l)


