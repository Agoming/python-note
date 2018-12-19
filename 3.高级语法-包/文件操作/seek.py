# seek基础案例
# 条件：从文件的第5个字节开始读取
with open(r't01.txt',"r+") as f:
    # 此时指针在0
    f.seek(6,0)
    fr = f.read()
    print(fr)


# 打开文件，每三个字符一组的形式打开内容，并显示在屏幕上
# 每读一次休息一秒
# import  time
# with open(r"t01.txt","r+") as f:
#     str = f.read(3)# 设置每次读取三个字符
#     while str:
#         print(str)
#         time.sleep(1)
#         str = f.read(3)
#

# tell显示当前指针位置
with open(r"t01.txt","r+") as f:
    ft = f.tell()
    print(ft)
    f.seek(3,0)# 移动3个字节
    fts = f.tell()
    print(fts)



