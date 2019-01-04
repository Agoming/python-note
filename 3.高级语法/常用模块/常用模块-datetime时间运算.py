# datetime模块
  # datetime提供日期和时间的运算和表示


import datetime # 引入包

# date提供一个自制的日期
# date(year,month,day)
dt = datetime.date(2018,11,26)
print(dt)
# 你还可以调用date的属性
print(dt.year)
print(dt.month)
print(dt.day)

 # time 提供fold hour microsecond minute second tzinfo的属性
tt = datetime.time(hour=11,minute=12)
print(tt.hour)
print(tt.minute)
# help(datetime.time)

# datetime 提供日期和时间的组合,必须书写其年月日
# 常用方法：
# today = 今天
# now = 该对象设置为此计算机上的当前日期和时间，表示为本地时间。在中国就是北京时间。
# utcnow  = 该对象设置为此计算机上的当前日期和时间，表示为协调世界时 (UTC)。通俗点就是格林威治时间的当前时间。
print(datetime.datetime(year=2018,month=11,day=26))
# help(datetime.datetime)
dd = datetime.datetime(2018,11,26)
print(dd.today())
print(dd.now())
print(dd.utcnow())



# timedelta 提供一个时间差，时间长度
t1 = datetime.datetime.now()# 获取当前时间
print(t1)
td = datetime.timedelta(hours=1)# 让时间往后移一个小时
print(t1+td)

# datetime.datetime模块
  # 提供比较好用的时间
  # 类属性
  #  class datetime.datetime(year, month, day[, hour
  #           [, minute
  #           [, second
  #           [, microsecond
  #           [, tzinfo]]]]])
  # # The year, month and day arguments are required.
  # MINYEAR <= year <= MAXYEAR
  # 1 <= month <= 12
  # 1 <= day <= n
  # 0 <= hour < 24
  # 0 <= minute < 60
  # 0 <= second < 60
  # 0 <= microsecond < 10**


# datetime.fromtimestamp(timestamp[, tz]): 根据时间戳返回本地的日期和时间.tz指定时区.

import  time
t = time.time()# 获取时间戳
s = datetime.datetime.fromtimestamp(t)
print(s)

# datetime.utcfromtimestamp(timestamp): 根据时间戳返回 UTC datetime.

s = datetime.datetime.utcfromtimestamp(t)
print(s)

# datetime.fromordinal(ordinal): 根据Gregorian ordinal 返回datetime.
# datetime.datetime.today().toordinal() 返回日期对象位于公历的序数也就是西方的日历Gregorian ordinal
t = datetime.datetime.today().toordinal()# 先获取Gregorian ordinal
print(t)
s = datetime.datetime.fromordinal(int(t))# 将获取的Gregorian ordinal 转化为int
print(s)

# datetime.combine(date, time): 根据date和time返回一个新的datetime.
tt = datetime.datetime.combine(datetime.date(2018,11,26),datetime.time())
print(tt)



# datetime.strptime(date_string, format): 根据字符串格式的日期+需要转化的格式=新的日期
ds = datetime.datetime.strptime("2018-11-26 06:29:31","%Y-%m-%d %H:%M:%S")
print(ds)