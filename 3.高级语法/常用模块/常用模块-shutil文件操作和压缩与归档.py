# shutil 高级文件操作，目录树的操作，文件赋值，删除，移动
import shutil # 导入包

# copy()
#  格式：shutil.copy(来源路径，目标路径)
#  返回值：返回目标路径
# 拷贝的同时，可以给文件重命名
# r = shutil.copy("e:/a.txt","e:/b.txt")
# print(r)

# copy2 复制文件，保留元数据
#  格式：shutil.copy2(来源路径，目标路径)
#  返回值：返回目标路径
#  注意：copy和copy2的唯一区别在于copy2复制文件时尽量保留元数据
# r2 = shutil.copy2("e:/a.txt","e:/b.txt")
# print(r2)

# copyfile 将一个文件中的内容复制道另一个文件当中
#  格式：shutil.copyfile（'源路径','目标路径')
#  返回值：无
# c = shutil.copyfile("e:/a.txt","e:/b.txt")
# print(c)

# move 移动文件或文件夹
#  格式：shutil.move(源路径，目标路径)
#  返回值：目标路径！
# r = shutil.move("e:/a.txt","e:/编程笔记")
# print(r)

# 归档和压缩
# 归档：把多个文件或者文件夹合并到一个文件当中
# 压缩：用算法把对个文件或者文件夹无损或者有损合并到一个文件当中

# make_archive 归档操作
#  格式:shutil.make_archive('归档之后的目录和文件名','归档文件后缀名','需要归档的文件夹')
#  返回值：归档之后的地址
r = shutil.make_archive("e:/a","zip","e:/a")
print(r)

# unpack_archive 解包
# 格式：shutil.unpack_archive('归档文件地址','解包之后的地址')
# 返回值：解包之后的地址
r = shutil.unpack_archive("e:/a.zip","e:")
print(r)

