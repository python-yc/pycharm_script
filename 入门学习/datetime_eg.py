#coding:utf-8
import datetime
#datetime常见属性
#datetime.date()：一个理想和的日期，提供year，month，day属性
dt = datetime.date(2018,3,26)
print(dt)
print(dt.day)
print(dt.year)
print(dt.month)

#datetime.time:提供一个理想和的时间
#datetime.datetime:提供日期与实践的组合
#datetime.timedelta:提供一个时间差，时间长度
from datetime import datetime
import time
#常用类方法：today、now、utcnow、fromtimestamp（从时间戳中返回本地时间）
dt = datetime(2018,2,26)    #此处的时间没有用到，但是需要这三个参数，删除报错
print(datetime.today())
print(dt.now())
print(dt.fromtimestamp(time.time()))
print("===============11111111")
#datetime.timedelta:表示一个时间间隔
from datetime import datetime,timedelta
t1 = datetime.now()
print(t1.strftime("%Y-%m-%d %H:%M:%S"))
#td表示以小时的时间长度
td = timedelta(hours=1)
print(td)
#当前时间加上时间间隔后，把得到的一小时后的时间格式化输出
print((t1+td).strftime("%Y-%m-%d %H:%M:%S"))
##timeit-时间测量工具
###- 测量程序运行时间间隔实验
print("===============222222")
def p():
    time.sleep(3.6)
t1 = time.time()
p()
print(time.time() - t1)
print("===========3333333333")
#利用timeit调用代码，执行100000次，查看运行时间
#格式timeit.timeit(stmt=c,number=10000),c可以是函数，也可以是字符串式的代码块
####字符串代码块形式s='''内容在三引号之间'''
#timeit可以执行一个函数，来测量函数的执行时间，如：
import timeit
def doIt():
    num = 2
    for i in range(num):
        print("Repeat for {0}".format(i))
#执行函数，重复10次
print(doIt)
print(type(doIt))
t = timeit.timeit(stmt=doIt,number=10)
print(t)
print("=============或者这样同上一个")
import timeit
s ='''
def doIt(num):
    num = 2
    for i in range(num):
        print("Repeat for {0}".format(i))
'''
#执行函数，重复10次
#执行doIt(num)，setup负责把环境变量准备好
#实际相当于给timeit创造一个小环境，在创造的小环境中，代码的执行顺序大致是
#
'''
def doIt(num):
    ......
num = 2
doIt(num)
'''
#此处的setup后的num=2循环输出的范围（即for后range的参数），number后的数字表示的循环次数
t = timeit.timeit("doIt(num)",setup=s+"num=0",number=10)
print(t)

# help(timeit.timeit)




