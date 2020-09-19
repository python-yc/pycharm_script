'''
索引  属性      字段              值
0	tm_year	    4位数年        2008
1	tm_mon	    月            1 到 12
2	tm_mday	    日            1 到 31
3	tm_hour	   小时           0 到 23
4	tm_min	   分钟           0 到 59
5	tm_sec	    秒            0 到 61 (60或61 是闰秒)
6	tm_wday	 一周的第几天     0到6 (0是周一)
7	tm_yday	 一年的第几日     1 到 366(儒略历)
8	tm_isdst    夏令时        -1, 0, 1, -1是决定是否为夏令时的旗帜

'''
#多行一起快捷键注释：Ctrl+/
# 需要单独导入time
#coding:utf-8
import time
#时间模块的属性
#timezone:当前时区和UTC时间相差的秒数，在没有夏令时的情况下间隔
print(time.timezone)
print(time.timezone/3600)
#altzone 获取当前时区和UTC时间相差的秒数，在有夏令时的情况下间隔
print(time.altzone)
print(time.altzone/3600)
#daylight 测当前是否是夏令时时间状态，0 表示是
print(time.daylight)
###当前时间
#localtime()当前时间，返回值为元组形式
t = time.localtime()
print("localtime***",t)
print("============")
#asctime()返回元组的正常字符串转化之后的时间格式
#格式：time.asctime(时间元组)
#返回值：字符串Sun Feb 17 14:20:00 2019
tt = time.asctime(t)
print(type(tt))
print(tt,"asctime")
print("============")
#ctime:获取字符串化的当前时间
t = time.ctime()
print(type(t))
print(t)
print("====****========")
#mktime()使用时间元组获取对应的时间戳
#格式：time.mktime(时间元组)
#返回值：浮点数时间戳
lt = time.localtime()
ts = time.mktime(lt)
print(type(ts))
print(ts)
###sleep:是程序进入睡眠，n秒后继续
for i in range(1,3):
    time.sleep(1)
    print(i)
#报时间表示成2018年3月26日   21:05
#strftime:将时间元组转化为自定义的字符串格式
t = time.localtime()
#这个日期中文编译此处不支持
#ft = time.strftime("%Y年%m月%d日 %H:%M" , t)
ft = time.strftime("%Y-%m-%d %H:%M:%S" , t)
print(ft)

print(time.clock())
print(time.time())
