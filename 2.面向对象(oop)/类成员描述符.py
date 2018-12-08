# python 描述器和描述符


class b():
    def __init__(self,name = "asd"):# 构建一个带值的name
        self.name = name

    def __get__(self, instance, owner):# 获取构建函数属性的值
        return self.name*2

    def __set__(self, instance, value):# 修改构建函数属性的值
        self.name = value

class a():
    b = b()# 将b类赋值给变量b
    b.__set__(b,"asds")# 修改属性值
aa = a()
print(aa.b) # 调用a类里面的b属性，并打印出来

# property 案例
class A():
    def fget(self):
        return self._name * 2
    def fset(self,name):
        self._name = name.upper()
    def fdel(self):
        self._name = "asd"

    name = property(fget,fset,fdel,"对name属性进行操作")

p = A()
p.name = "qqq"
print(p.name)


class Person():
    '''
    这是一个人，一个高尚的人，一个脱离了低级趣味的人
    他还他妈的有属性
    '''

    # 函数的名称可以任意
    def fget(self):
        return self._name * 2

    def fset(self, name):
        # 所有输入的姓名以大写形式保存
        self._name = name.upper()

    def fdel(self):
        self._name = "NoName"

    name = property(fget, fset, fdel, "对name进行下下操作啦")# property(fget=None,fset=None,fdel=None,doc=None) doc为说明文档

p = Person()
p.name = "asd"
print(p.name)
del p.name
print(p.name)

# @property



class Screen(object):
    @ property # property代表的是被读取的内容
    def Width(self):
        return self._width

    @Width.setter # 被读取的函数名.setter就是引用，用于设置被获取的值
    def Width(self,value):
        self._width = value

    @ property
    def Height(self):
        return self._height

    @ Height.setter
    def Height(self,value):
        self._height = value

    @ property
    def Resolution(self):
        return self._height * self._width



s = Screen()
s.Width = 1024
s.Height = 768
print('resolution =', s.Resolution)
if s.Resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
