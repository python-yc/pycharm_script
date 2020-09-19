# -*- coding: utf-8 -*-
import time

# https://www.cnblogs.com/wf-linux/archive/2018/08/01/9400354.html

'''
 time模块中时间表现的格式主要有三种：

　　a、timestamp时间戳，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量

　　b、struct_time时间元组，共有九个元素组。

　　c、format time 格式化时间，已格式化的结构使时间更具可读性。包括自定义格式和固定格式。
'''

"""
时间格式转换关系:
Format_time --(strptime)--> struct_time --(mktime)--> Timestamp
Timestamp --(localtime/gmtime)--> struct_time --(strftime)--> Format_time

struct_time --(asctime)--> %a %b %d %H:%M:%S %Y
Timestamp --(ctime)--> %a %b %d %H:%M:%S %Y

struct_time元组元素结构:
属性                            值
tm_year（年）                  比如2011 
tm_mon（月）                   1 - 12
tm_mday（日）                  1 - 31
tm_hour（时）                  0 - 23
tm_min（分）                   0 - 59
tm_sec（秒）                   0 - 61
tm_wday（weekday）             0 - 6（6表示周日）
tm_yday（一年中的第几天）        1 - 366
tm_isdst（是否是夏令时）        默认为-1
"""

# 主要time生成方法和time格式转换方法实例：
# 生成timestamp
print(time.time())

# 通过timestamp 获取11位数字
print(type(time.time()))
print(int(time.time() * 10))

# struct_time --(mktime)--> Timestamp
print(time.mktime(time.localtime()))

'''北京时差:(UTC_GMT_格林威治时间)格林威治时间比北京时间晚8小时'''
# 生成struct_time
# Timestamp --(localtime/gmtime)--> struct_time  本地时间
# time.struct_time(tm_year=2020, tm_mon=9, tm_mday=13, tm_hour=10, tm_min=36, tm_sec=56, tm_wday=6, tm_yday=257, tm_isdst=0)
print(time.localtime())
print(time.localtime(time.time()))

# Timestamp --(localtime/gmtime)--> struct_time  格林威治时间
# time.struct_time(tm_year=2020, tm_mon=9, tm_mday=13, tm_hour=2, tm_min=36, tm_sec=56, tm_wday=6, tm_yday=257, tm_isdst=0)
print(time.gmtime())
print(time.gmtime(time.time()))

# Format_time --(strptime)--> struct_time
# time.struct_time(tm_year=2020, tm_mon=9, tm_mday=13, tm_hour=16, tm_min=37, tm_sec=6, tm_wday=6, tm_yday=257, tm_isdst=-1)
print(time.strptime('2020-09-13 16:37:06', '%Y-%m-%d %X'))

# 生成format_time
# struct_time --(strftime)--> Format_time
# 2020-09-13 11:01:29
print(time.strftime("%Y-%m-%d %X", time.localtime()))

# 生成固定格式的时间表示格式
# Sun Sep 13 11:02:36 2020
print(time.asctime())
print(time.ctime())

# timestamp加减单位以秒为单位
import time

t1 = time.time()
t2 = t1 + 10

print(time.ctime(t1))  # Wed Oct 26 21:15:30 2016
print(time.ctime(t2))  # Wed Oct 26 21:15:40 2016

'''
format time结构化表示

格式	含义
%a	本地（locale）简化星期名称
%A	本地完整星期名称
%b	本地简化月份名称
%B	本地完整月份名称
%c	本地相应的日期和时间表示
%d	一个月中的第几天（01 - 31）
%H	一天中的第几个小时（24小时制，00 - 23）
%I	第几个小时（12小时制，01 - 12）
%j	一年中的第几天（001 - 366）
%m	月份（01 - 12）
%M	分钟数（00 - 59）
%p	本地am或者pm的相应符
%S	秒（01 - 61）
%U	一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周。
%w	一个星期中的第几天（0 - 6，0是星期天）
%W	和%U基本相同，不同的是%W以星期一为一个星期的开始。
%x	本地相应日期
%X	本地相应时间
%y	去掉世纪的年份（00 - 99）
%Y	完整的年份
%Z	时区的名字（如果不存在为空字符）
%%	‘%’字符
'''
