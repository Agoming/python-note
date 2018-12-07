# MethodType
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186739713011a09b63dcbd42cc87f907a778b3ac73000
def set_name(self,name):
    self.name = name
    return self.name
class A():
    pass

# 使用类来创建一个方法
a = A()
from types import MethodType
a.set_name = MethodType(set_name,a)# 通过methodType将其把指定方法放置到制定类里面
a.set_name("haha")
print(a.set_name)

# 使用type创建类
# https://www.cnblogs.com/caoxing2017/p/8010695.html
def set_name(self):
    print("hello")

Hello = type("Hello",(object,),dict(set_name = set_name))# 注意定义时候的逗号，先定义类名，然后指明类型，最后通过字典的方式把函数传入到指定类里面
h = Hello()
print(h.set_name)


# 元类
# http://python.jobbole.com/88795/
#https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000
class SayMetaClass(type):# ying为元类是由type衍生而出，所以需要传入type
    def __new__(cls, name,bases,attrs):
        print("这是我的元类")
        attrs['id'] = 'asd'
        attrs["addr"] = "哈哈哈"
        return type.__new__(cls,name,bases,attrs)

class S(object,metaclass=SayMetaClass):
    pass

s = S()
s.id


