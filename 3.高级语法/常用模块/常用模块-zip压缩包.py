# zip 压缩包
  # zip压缩和归档的取别
    # 归档： 把多个文件或者文件夹合并到一个文件当中
    # 压缩： 用算法把多个文件或者文件夹无损或者有损合并到一个文件当中
  # 模块名称 zipfile

import  zipfile

# zipfile.ZipFile(file[, mode[, compression[, allowZip64]]])
# 创建一个ZipFile对象，表示一个zip文件。参数file表示文件的路径或类文件对象(file-like object)；参数mode指示打开zip文件的模式，默认值为’r’，表示读已经存在的zip文件，也可以为’w’或’a’，’w’表示新建一个zip文档或覆盖一个已经存在的zip文档，’a’表示将数据附加到一个现存的zip文档中。参数compression表示在写zip文档时使用的压缩方法，它的值可以是zipfile. ZIP_STORED 或zipfile. ZIP_DEFLATED。如果要操作的zip文件大小超过2G，应该将allowZip64设置为True
z = zipfile.ZipFile("E:/b.zip")# 为b.zip创建一个对象

# zipfile.ZipFile.getinfo
# 获取zip文档内指定文件的信息，返回一个zipfile.ZipInfo对象，它包括文件的详细信息
zg = z.getinfo("b.txt")# 查看b.zip文件里面的b.txt信息
print(zg)

# zipfile.ZipFile.namelist()
# 获取zip文档内所有文件的名称列表
zn = z.namelist()
print(zn)

# zipfile.ZipFile.extractall([path[, members[, pwd]]])
# 把zip文档的所有文件解压到当前目录，参数members的默认值为zip文档内的所有文件名称列表，也可以自己设置，选择要解压的文件名称
ze = z.extractall("E:/",members=["b.txt"])
print(ze)