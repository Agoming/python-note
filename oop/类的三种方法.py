# 三种方法的案例

# 实例方法
class A():
    # 就是正常编写
    def Haha(self):
        print("我被调用了")

# 实例方法调用
h = A()
h.Haha()

# 类方法
class B():
    # 需要在前面引用classmethod
    @classmethod
    # 区别实例方法，第一个参数为cls
    def Haha(cls):
        print("我被调用了")
# 类方法调用,能使用类调用，也能对象调用
B.Haha()
b = B()
b.Haha()

# 静态方法
class C():
    # static
    @staticmethod
    def Haha():
        print("我被调用了")

# 静态方法调用，能被类调用，也能被对象调用
C.Haha()
c = C()
c.Haha()