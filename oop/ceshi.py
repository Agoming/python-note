
def a():
    p = [0] # 直接赋值的话，变量为局部变量，使用下标赋值可以通过传址操作然后让b函数能使用变量p
    def b():
        p[0] += 1
        return p[0]
    return b

A = a()
print(A())
print(type(A()))


# 多重继承
# Mixin
class PersonMixin():
    def run(self):
        print("l can run...")


# class birdMixin():
#     def fly(self):
#         print("l can fly")

class SuperMan(PersonMixin,birdMixin):
    pass

s = SuperMan()
print(s.fly(),s.run())
