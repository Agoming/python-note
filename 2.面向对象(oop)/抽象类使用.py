import abc

class A(object):
    # 定义抽象实例方法
    @abc.abstractmethod
    def H(self):
        pass

    # 定义抽象类方法
    @abc.abstractclassmethod
    def HH(cls):
        pass

    # 定义抽象静态方法
    @abc.abstractstaticmethod
    def HHH(cls):
        pass


# 通过子类进行实现
class B(A):
    def H(self):
        print("这是个抽象实例方法")
    def HH(cls):
        print("这是抽象类方法")
    def HHH(cls):
        print("这是个抽象静态方法")

# 进行调用
b = B()
print(b.H())
print(b.HH())
print(b.HHH())
print(B.HH(B))
print(B.HHH(B))
# 在不设置返回值时统一返回值为None




