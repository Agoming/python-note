# ʹ��yield�����ش���generator

def odd():
    print("step 1")
    yield 1
    print("step 2")
    yield 3
    print("step 3")
    yield 5

o = odd()
print(next(o)) # �ᷢ��ÿ�����µ��þͻ��Ǵ���һ�η��ص�yield����п�ʼִ��
print(next(o))
print(next(o))