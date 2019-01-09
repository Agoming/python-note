# encoding:utf-8
# 使用getpid和getppid获取线程的父线程的id和子线程的id
import multiprocessing
import os # 引入os(文件管理)包查询

def info(title):
    print(title)
    print("module name:",__name__)
    print("parent process:",os.getppid()) # 获取父id
    print("process id:",os.getpid())# 获取子id


if __name__ == '__main__':
    info("main")
    p = multiprocessing.Process(target = info,args = ("info",))
    p.start()
    p.join()

    # 总结:说明子线程info是继承父线程main的，但他们的id基于物理储存环境，所以每次启动都不一样