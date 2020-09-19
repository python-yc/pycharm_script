"""
#关于concurrent的案例
from concurrent.futures import ThreadPoolExecutor
import time

def return_future(msg):
    time.sleep(3)
    return msg

#创建一个线程池
pool = ThreadPoolExecutor(max_workers=2)

#往线程池加入2个task
f1 = pool.submit(return_future,'hello')
f2 = pool.submit(return_future,'world')

#done等待执行完毕
print(f1.done())
time.sleep(3)
print(f2.done())

#打印结果
print(f1.result())
print(f2.result())

#运行结果
False
True
hello
world
"""
###current中的map函数###
import time,re
import os,datetime
from concurrent import futures

data = ['1','2']

def wait_on(argument):
    print(argument)
    time.sleep(2)
    return 'ok'

ex = futures.ThreadPoolExecutor(max_workers=2)
for i in ex.map(wait_on,data):
    print(i)



