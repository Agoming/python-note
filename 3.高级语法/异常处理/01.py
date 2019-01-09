# 简单异常案例
# try:
#     num = int(input("请输入一个数字"))
#     rst = 100/num
#     print("计算结果:{0}".format(rst))
# except:
#     print("请输入数字")
#     exit() # exit = 退出程序，意指已经执行完了


# 有准确解决方法的案例
# try:
#     num = int(input("请输入一个数字"))
#     rst = 100/num
#     print(rst)
# except ZeroDivisionError as e:
#     # 解决如果输入数字为0时的异常
#     # 与调用包相似 as是为了将ZeroDivisionError异常实例化，并且可以通过实例化返回信息
#     print("请不要输入数字0")
#     print(e)# 打印出异常捕获的信息
#     exit()# 退出异常处理


# 多个异常处理
# try:
#     num = int(input("请输入一个数字"))
#     rst = 100/num
#     print(rst)
# # 如果是多个异常处理的话，越是具体并容易犯的错误，就越往前放
# # 在异常继承关系中，越是子类的异常，越要往前放置
# # 例如exception这个异常，是所有异常的父类，如果放置第一位，其它异常则会被拦截住
# except ZeroDivisionError as e:
#     print("请不要输入数字0")
#     print(e)# 打印出异常捕获的信息
#     exit()# 退出异常处理
# except NameError as e:
#     print("名字出错了")
#     print(e)
#     exit()
# except AttributeError as e:
#     print("属性出错了")
#     print(e)
#     exit()
# except Exception as e:
#     print("在最后放置所有异常的父类，可以应对一些不知会出错的异常并且在接受异常信息时候补全")
#     print(e)
#     exit()

# 用户手动引发异常案例
# try:
#     print("hahah")
#     # 只是打印一句话，不存在引发异常
#     raise ValueError # 手动抛出一个值异常
#     print("异常被触发了")# 检测在异常触发后下面还是否会执行
# except NameError as e:# 写一个不可能被触发的异常处理
#     print("名字出错了")
#     print(e)
#     exit()
# except ValueError as e:# 编写关于手动抛出的异常的处理
#     print("我处理了")
#     print(e)
#     exit()
# except Exception as e:# 编写所有异常的父类
#     print("我也不知道哪里出错了")
#     print(e)
#     exit()

# 手动触发自定义异常案例
# class wodeyichang(ValueError):# 继承系统异常
#     pass
# try:
#     print("hahaha")
#     raise wodeyichang # 抛出自己编写的异常
# except NameError as e:
#     print("名称出错了")
#     print(e)
#     exit()
# except wodeyichang as e:
#     print("我的异常出来了")
#     print(e)
#     exit()
# except Exception as e:
#     print("好像有异常")
#     print(e)
#     exit()

# else和finally的使用案例
# try:
#     num = int(input("请输入一个数字"))
#     rst = 100/num
#     print("计算结果:{0}".format(rst))
# except Exception as e:
#     print("有异常")
#     print(e)
#     exit()
# else: # 没有异常则触发
#     print("哈哈没异常")
# finally:# 有没有异常都会被触发
#     print("反正我都会被触发")

