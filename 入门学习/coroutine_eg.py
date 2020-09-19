'''
#协程代码案例：
def simple_coroutine():
    print("--> start")
    x = yield
    print("--> received",x)

# 主线程
#生成一个协程实例
sc = simple_coroutine()
print(111)
#可以使用sc.send(None)，效果一样
next(sc)    #预激，先准备好

print(222)
sc.send("zhexiao")
#执行完成后会生成一个StopIteration错误
'''
"""
print("协程的状态，案例2")
def simple_coroutine(a):
    print("--> start")

    b = yield a
    print("--> received",a,b)

    c = yield a + b
    print("--> received",a,b,c)

#runc
sc = simple_coroutine(5)

aa = next(sc)
print(aa)
bb = sc.send(6) #5,6
print(bb)
cc = sc.send(7) #5,6,7
print(cc)


此段代码结果：
协程的状态，案例2
--> start
5
--> received 5 6
11
--> received 5 6 7
"""
'''
#案例3
def gen():
    for c in 'AB':
        yield from c
#list直接用生成器作为参数,list转化后的是一个列表，并不是生成器了
print(list(gen()))

def gen_new():
    yield from 'AB'

print(list(gen_new()))
案例3结果如下：
['A', 'B']
['A', 'B']
'''
# 案例4，委派生成器
from collections import namedtuple

'''
解释：
1、外层for循环每次迭代会新建一个grouper实例，赋值给coroutine变量，grouper是委派生成器
2、调用next(coroutine)，预激委派生成器grouper，此时进入while循环，调用子生成器average
3、内层for循环调用coroutine.send(value)，直接把值传给子生成器average，同时，当前的grouper...
4、内层循环结束后，grouper实例依旧在yield from表达式处暂停，因此，gouper函数定义体中...
5、coroutine.send(None)终止average子生成器，子生成器抛出StopIteration异常并将返回的...
'''
RestClass = namedtuple('Rest','count average')

#子生成器
def average():
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield
        #生成特殊符号，终止
        if term is None:
            break
        total += term
        count += 1
        average = total/count

    return RestClass(count,average)

#委派生成器
def grouper(storages,key):
    while True:
        #获取average()返回的值
        storages[key] = yield from average()

#客户端代码
def client():
    process_date = {
        'boys_2':[39.0,40.8,43.2,40.8,43.1,38.6,41.4,40.6,36.3],
        'boys_1':[1.38,1.32,1.25,1.37,1.48,1.25,1.49,1.46]
    }
    storages = {}
    for k,v in process_date.items():
        #获得协程
        coroutine = grouper(storages,k)

        #预激协程
        next(coroutine)

        #发送数据到协程
        for dt in v:
            coroutine.send(dt)

        #终止协程
        coroutine.send(None)
    print(storages)

#run
client()

