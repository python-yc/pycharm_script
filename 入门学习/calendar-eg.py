import calendar
#可以无参数
# cal = calendar.calendar(2019)
# print(type(cal))
# print(cal)

'''
可以有参数w、c、l
w = 每个日期之间的间隔字符串
c = 每个月之间的间隔字符数
l = 每周所占的行数
'''

cal = calendar.calendar(2019,l=0,c=2)
print(cal)

#内有isleap：判断某一年是否是闰年
print(calendar.isleap(2018))
print(calendar.isleap(2020))

#leapdays:获取指定年份之间闰年的个数
help(calendar.leapdays)
print(calendar.leapdays(2001,2020))
print(calendar.leapdays(2023,2020))

#monthranage() 获取某个月的日历字符串
#格式：calendar.monthranage(年,月)
#返回值：元组（周几开始，总天数）
#注意：周默认0-6 表示 周一到周天
x = calendar.monthrange(2019,6)
print(x)
k,v = calendar.monthrange(2019,6)
print(k)
print(v)
print(k+1)
#help(calendar)





