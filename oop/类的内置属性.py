class A(object):
    """
     这是文档信息
    """
    name = "asd"
    def B(self):
        pass

class B(A):
    pass

# 查看类的成员
print(A.__dict__)
# 查看类的文档信息
print(A.__doc__)
# 查看类的名称,在模块里面引用则显示模块的名称
print(A.__name__)
# 获取某类的所有父类，以元组的方式显示，因为元组自带说明
print(B.__bases__)