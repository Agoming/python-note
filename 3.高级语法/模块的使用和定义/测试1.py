# 模块的默认路径和系统自带模块
import  sys
import abc
print(type(sys.path))  # sys是以list方式将包的路径放置
for i in sys.path:
    print(i)# 打印目前py所引入的包
    print(type(i))



# 测试包的导入和模块导入
# import  cemo # 单导入包
import  cemo.o # 导入包+模块
from cemo.o import aa  as  ab# 导入包加模块加类+别名
from cemo.o import a as aab
aab.aaa(aab)
ab()