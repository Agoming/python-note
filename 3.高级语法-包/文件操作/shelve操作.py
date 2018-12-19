# -*- coding: utf-8 -*-
import shelve

shv = shelve.open(r"shv.db")
shv["one"] = 1
shv["two"] = 2
shv["three"] = 3
shv.close()
# shelve自动创建的不止有shv.db，还有其他文件

# # 读取shelve
# shv = shelve.open(r"shv.db")
# try:
#     print(shv['one'])
# finally:
#     shv.close()

# # 使用shelve特性只读

# so = shelve.open(r"shv.db",flag="r")# 为了解决多个应用并行写入，使用参数flag = r
# try:
#     k1 = so["one"]
#     print(k1)
# finally:
#     so.close()

# 修改shelve里内容
shv = shelve.open(r"shv.db")
try:
    shv["one"] = {"asdasd":1,"asd":2}
finally:
    shv.close()

so = shelve.open(r"shv.db")
try:
    print(so["one"])
finally:
    so.close()


# 关于shelve写回问题
# 强制写回
shv = shelve.open(r"shv.db")
try:
    k1 = shv['one']
    print(k1)
    # shelve还没关闭，数据还在内存里面，并没存入数据库，所以要进行强制将数据写回
    k1["asd"] = 100  # 如果该数据被传回了则证明有写回
finally:
    shv.close()

# 检测asd = 100是否有传回
so = shelve.open(r"shv.db")
try:
    k1 = so['one']
    print(k1) # 事实证明并没传回
finally:
    so.close()

# 强制写回的写法
shv = shelve.open(r"shv.db",writeback=True)
try:
    k1 = shv['one']
    print(k1)
    k1["asd"] = 100
finally:
    shv.close()

so = shelve.open(r"shv.db")
try:
   k1 = so["one"]
   print(k1)
finally:
    so.close()

# 使用with搭配shelve
with shelve.open(r"shv.db",writeback=True) as shv:
    k1 = shv['one']
    print(k1)
    k1["asd"] = 199

with shelve.open(r'shv.db') as so:
    print(so["one"])

