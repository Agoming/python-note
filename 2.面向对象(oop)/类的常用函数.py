# issubclass：检测一个类是否是另一个类的子类
class A():
    pass

class B(A):
    pass

class C():
    pass

print(issubclass(B,A)) # 测试B是否是A的子类
print(issubclass(C,B)) # 测试C是否是B的子类
# help(issubclass()) # 查看issubclass的说明文档

# isinstance：检测一个对象是否是一个类的实例
class A():
    pass

class B():
    pass

a = A()
b = B()
print(isinstance(a,A))# 检测a是否是A的实例对象
print(isinstance(b,A))# 检测b是否是A的实例对象
# help(isinstance)# 查看isinstance说明文档

# hasattr： 查看一个类是否有某成员变量
class A():
    aa = "属性"

a = A()
print(hasattr(A,"aa"))# 在A类里面查找是否有aa这个属性
print(hasattr(A,"haha"))# 查找haha属性
# help(hasattr)


# getattr：或者某类的一个成员属性
class A():
    name = "asd"

print(getattr(A,"name"))

# 当查看的属性没有时系统会报错
# print(getattr(A,"age"))

# 但我们设置一个返回值就不会报错了
print(getattr(A,"age",10))

# help(getattr)

# setattr：设置某类的一个成员属性
class A():
    name = "asd"

print(A.name) # 打印获取前的属性
print(setattr(A,"name","hahah")) # 修改name的值，并且返回一个None
print(A.name) # 打印修改后的属性值
# help(setattr)

# delattr ：删除一个类的某个属性
class A():
    name = "asd"

print(A.__dict__)# 打印删除前的类里面的东西
print(delattr(A,"name")) # 返回None
print(A.__dict__)# 打印删除后的类的东西

# dir ：
class A():
    a = "asd"

class B():
    def __dir__(self):
        a = "asd"
        pass
print(dir())
print(dir(A)) # 该参数没设置dir方法 所以被最大程度的收集
print(dir([A]))
print(dir([B])) # 查看列表的方法