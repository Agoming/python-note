# init

class A():
    def __init__(self):
        print("我进行了自我调用")

a = A()# 在类实例化时自我调用

# __call__
class A():
    def __call__(self):
        print("实例化自我调用了")

a = A()
a()

# __str__
class A():
    def __str__(self,value):
        return value

a = A()
print(a.__str__("hahah"))

# __repr__
class A():
    def __repr__(self,value):
        return value

a = A()
print(a.__repr__("hahah"))

# repr和str的区别
# https://blog.csdn.net/luckytanggu/article/details/53649156
class A():
    def __init__(self,value = "hello"):
        self.value = value
        print(id(self.value))

a = A()
print(a)# 直接返回的是对象的内存地址

# 重写repr
class B(A):
    def __repr__(self):
        return "这是通过repr转化之后的字符：(%s)" % self.value

b = B()
print(B)
print(b)
print("我是repr里的value的变量内存地址",id(b.value))
class C(A):
    def __str__(self):
        return "这是通过str转化之后的字符：(%s)" % self.value

c = C()
print(c)
print("我是str里的value的变量内存地址",id(c.value))


# 属性操作符

# getattr
class A():
    name = "Noname"
    age = 18
    def __getattr__(self, name):
        print("找到了")
        print(name) # 打印找到的属性名称

a = A()
print(a.name)
print(a.addr)# 尝试寻找一个不存在的属性，查看会如何
# 在寻找addr这个属性时，系统除了打印了需要寻找的属性名称，也带了一个返回值None

# 下面为伪代码
# # 当我们为这个不存在的属性设置一个值时
# print(a.getattr(a,"attr",1))
# # 并且再次寻找这个属性
# print(a.addr) # 就不会再出现返回值None的操作了

# setattr
class Person():
    def __setattr__(self, key, value):
        print("设置属性: {0}".format(key))
        # 之前说过这个魔法函数使用不好就会自动死循环
        # self.key = value
        # 所以针对这种情况，一般使用父类魔法函数进行调用
        super().__setattr__(key,value)

p = Person()
print(p.__dict__)
# 下面我们查找age属性，会出错
# print(p.age)
# 我们设置一个名为age的属性,并打印出来
p.age = 18
print(p.age)


# getattribute
# https://blog.csdn.net/yitiaodashu/article/details/78974596
class A():
    def __init__(self,name):
        self.name = name
    def __getattribute__(self, item):
        print("haha")# 测试是否会无条件执行一次
        return object.__getattribute__(self,item)

a = A("a")
print(a.name)# 当我把值直接打印时，并不会直接打印，而是先传入到getattribute里面进行操作，然后才会审核


# setitem,getitem,delitem
class A():
    def __getitem__(self, item):
       return self.__dict__[item]
    def __setitem__(self, key, value):
        self.__dict__[key] = value
    def __delitem__(self, key):
        self.__dict__.pop(key)
a = A()
a.age = 10
print(a.age)
del a.age
# 删除之后就没了
# print(a.age)


# 运算分类相关魔法方法
class A():
    def __init__(self,name):
        self.name = name

    def __gt__(self, other):
        print("{0}比{1}大吗".format(self,other))
        return  str(self.name) >other.name

    def __str__(self):# 使用str把两个对象的物理地址改变为str
        return self.name

a1 = A("one")
b1 = A("two")
print(a1 > b1)