# 常用模块
#   calendar
#   time
#   datetime
#   timeit
#   os
#   shutil
#   zip
#   math
#   string
#   上述所有模块使用理论上都应该先导入,string是特例


# calendar
  # 跟日历相关的模块

import  calendar# 导入模块

# calendar 获取一年的日历字符串
# calendar(w,l,c) w = 每个日期之间的间隔字符数 , l = 每周所占用的行数 c = 每个月之间的间隔字符数
print(calendar.calendar(2018))# 打印2018的日历
print(type(calendar.calendar(2018)))# 查看打印出来的东西是什么类型

# 使用参数改变日历
print(calendar.calendar(2017,l=0,c=5))

# isleap 判断某一年是否为闰年
print(calendar.isleap(2000))

# leapdays：获取指定年份之间的闰年的个数
print(calendar.leapdays(2000,2004))# 算左不算右

# month：获取某个月的日历字符串
print(calendar.month(2018,12))# 第一个参数为年，第二个参数为月

# monthrange：获取某个月是以周几开始和天数
# 其返回的值是元祖(周几开始,天数
k,v = calendar.monthrange(2018,11)
print(k," ",v)

# monthcalendar ：将某个月的每个星期以长方形列表的方式返回
# 返回类型为: 二级列表
# 注意:矩形中没有的天数和第一天用0表示
m = calendar.monthcalendar(2018,11)
print(m)
print(type(m))

# prcal 不需要print直接打印日历
# 无返回值
calendar.prcal(2018)

# promonth 不需要print直接打印整个月的日历
# 无返回值
calendar.prmonth(2018,11)

# weekday 获取周几
# weekday(年，月，日)
print(calendar.weekday(2018,11,27))
