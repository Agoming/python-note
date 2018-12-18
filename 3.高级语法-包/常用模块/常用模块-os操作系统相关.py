
# os - 关于操作系统
  # 跟操作系统相关，主要是文件操作
  # os 的三个模块
    # os  操作系统目录相关
    # os.path 系统路径相关操作
    # shutil 高级文件操作，目录树的操作，文件赋值，删除，移动
  # 路径
    # 绝对路径 ：从根目录上开始
    # 相对路径 ：基于当前环境为开始的一个相对的目录或地方


# os 模块
import  os # 导入模块

# getcwd 获取当前的工作目录
# 当前工作目录则是当前程序运行的目录
print(os.getcwd())

# chdir 改变当前的工作目录
# chdir = change directory
os.chdir("E:\编程笔记")
print(os.getcwd())

# listdir 获取一个目录中所有子目录和文件的名称列表
print(os.listdir())

# makedirs 在本目录下创建一个文件夹
# 无返回值
# rst = os.makedirs("haha")
# print(rst)
# print(os.listdir())

# system 运行系统cmd命令
# 返回值: 失败返回-1 成功返回0


# 打开e盘
r = os.system("cd/编程笔记/python")
print(r)
print(os.getcwd())# 查看目录，可以看出他只是运行但并未改变工作目录

# os.popen(command[, mode[, bufsize]]) 通过一个cmd命令打开一个管道
# command -- 使用的命令。
# mode -- 模式权限可以是 'r'(默认) 或 'w'。
# bufsize -- 指明了文件需要的缓冲大小：0意味着无缓冲；1意味着行缓冲；其它正值表示使用参数大小的缓冲（大概值，以字节为单位）。负的bufsize意味着使用系统的默认值，一般来说，对于tty设备，它是行缓冲；对于其它文件，它是全缓冲。如果没有改参数，使用系统的默认值。
# os,popen和os.system的取别：
  # os.system(cmd)的返回值只会有0(成功),1,2
  # os.popen(cmd)会吧执行的cmd的输出作为值返回。

# a = 'mkdir nwdir'
#
# b = os.popen(a,'w',1)
#
# print(b)

# subprocess.popen
# 参数太多了 看下面文章
# https://blog.csdn.net/bcfdsagbfcisbg/article/details/78134172?locationNum=7&fps=1
# https://www.cnblogs.com/zhoug2020/p/5079407.html

# getenv 获取指定的系统环境变量值
# 返回值: 返回指定系统环境变量名对应的值
print(os.getenv("PATH"))

# putenv # 改变系统环境变量

# exit 退出当前程序
print("as")
# exit()
print("as")# 此as 不打印

# 值部分
  # os.curdir ：curretn dir 当前目录
  # os.pardir ：parent dir 父级目录
  # os.sep ：当前系统的系统分隔符
    # windows ："\"
    # linux ："/"
  # os.linesep：当前系统的换号符号
    # windows："\r\n"
    # linux,unix,macos ："\n"
  # os.name : 当前系统名称
    # windows : nt
    # mac,unix,linux: posix

# os.pardir
print(os.pardir)
# os.curdir
print(os.curdir)

# os.sep
print(os.sep)
# os.linesep
print(os.linesep)

# 在关于路径path的编写时，千万不要手动编写地址，这样编写的地址不具有可移植性
# 可移植性:同一句path移动到其他系统，但有可能系统辨别的分隔符不一样，那么就会出错

# 无移植性
path = "c:\\as\\"+"haha"+"\\"+"aa"
print(path)

# 可移植性
p = os.sep
path2 = "c:"+p+"as"+p+"haha"+p+"aa"
print(path2)

# name 系统名称
print(os.name)

# os.path 路径相关的模块

import  os.path as op # 弄个别名

# abspath("路径")
a = op.abspath(".") # 获取当前目录路径
print(a)
aa = op.abspath("..")# 获取父级目录路径
print(aa)

# basename 获取路径中文件名部分
a = op.basename("e:编程笔记\python\python讲义")
print(a)

# join 将多个路径拼合成一个路径
a1 = "e:编程笔记"
a2 = "python\python讲义"
print(op.join(a1,a2))# 他会自动帮你补充分隔符

# split 将路径分割为文件夹和当前文件部分
# 返回值为元祖类型，可以通过kv获取
t = op.split("e:编程笔记\python\python讲义")
print(type(t))
print(t)
k,v = t
print(k,v)

# isdir 检测一段路径是否是目录
r = op.isabs("e:编程笔记\python\python讲义")
print(r)
r2 = op.isabs("E:\编程笔记")
print(r2)

# exists 检测文件或者目录是否存在
print(op.exists("E:\编程笔记"))
print(op.exists("asd"))
