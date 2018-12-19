# # 使用with打开文件
# with open(r"t01.txt","r") as f:
#     # 跟模块引入一样，可以使用AS获取别名
#     pass
#     # 在本模块中不需要再使用close关闭文件
#
# # 使用with写入文件
#
# with open(r"t01.txt",'w+') as f:
#     f.writelines("hahahah")
#
#
# # 检测是否有写入
# # 之所以不能在同一个打开文件模块中同时检测，是因为，你只是写入，并未保存
# with open(r"t01.txt","r") as f:
#     print(f.readline())

# with 读取多段内容结构
# with open(r"t01.txt","r") as f:
#     fr = f.readline()
#     while fr:
#         print(fr)
#         fr = f.readline()


# list能用打开的文件作为参数，把文件的内容每一行作为一个元素返回
# with open(r't01.txt',"r") as f:
#     l = list(f)
#     print(type(l)) # 此时的文件是list类型
#     for i in l:
#         print(i)


# read的使用
# read允许输入参数决定读取几个字符，如果没有指定，则从当前位置读取到结尾
# 否则则按照输入的参数开始读取字符
with open(r"t01.txt","r") as f:
    fr = f.read(1)
    print(len(fr))# 查看获取长度是否符合参数
    print(fr)