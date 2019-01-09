# 打开文件，用写的方式
# r表示后面的字符串内容不需要转义
# 通过将open的内容赋值给的变量，那个变量统称为句柄
f = open(r"t01.txt","r")
print(f.readline()) # 无东西
f.close()# 关闭