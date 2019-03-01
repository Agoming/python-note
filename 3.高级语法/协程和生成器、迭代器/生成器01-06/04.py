# 使用yield来返回创建generator

def odd():
    print("step 1")
    yield 1
    print("step 2")
    yield 3
    print("step 3")
    yield 5

o = odd()
print(next(o)) # 会发现每次重新调用就会是从上一次返回的yield语句中开始执行
print(next(o))
print(next(o))