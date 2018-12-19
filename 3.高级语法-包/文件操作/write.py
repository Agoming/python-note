# # write基础用法
# with open(r"t01.txt","a") as f:
#     f.write("生活不仅有眼前的苟且,\n 还有狗屎")
#

# 直接以行写入writelines
with open(r't01.txt',"a") as f:
    f.writelines("haha")
    f.writelines("asd")
    # 但不会分行，只是以行的形式写入


l = ["l","love","xuexi"]
with open(r't01.txt','w') as f:
    f.writelines(l)
