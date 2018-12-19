# -*- coding: utf-8 -*-
import pickle as p


# dump序列化
age = 1 # 需要序列化的内容
with open(r"t01.txt","wb") as f:
    p.dump(age,f)

# load反序列化
with open(r"t01.txt","rb") as f:
    pl = p.load(f)
    print(pl) # 转化时需要注意转码


# 列表序列化
a = [12,'as',"asd",[1,'a']]
# 存入
with open(r"t01.txt","wb") as f:
    p.dump(a,f)

# 读取
with open(r"t01.txt","rb") as f:
    pl = p.load(f)
    print(pl)