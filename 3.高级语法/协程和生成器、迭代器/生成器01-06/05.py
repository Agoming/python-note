# encoding:utf-8
# 解决使用for循环调用generator时拿不到return语句的返回值
# 解决方案：比抓StopIteration错误，因为返回值就包含在StopIteration的Value中

def fid(max):
    n,a,b = 0,0,1
    while n < max:
        # print(b) # 不能使用print  要使用yield 不然就变成不可迭代对象，就无法被捕抓错误
        yield b
        a,b = b,a+b
        n = n + 1
    return 'None'

f = fid(6)

# 开始捕抓错误
while True: # 一直循环直到break
    try:
        x = next(f)
        print("f",x)
    except StopIteration as e:
        print("Generator return Value:",e.value)
        break



