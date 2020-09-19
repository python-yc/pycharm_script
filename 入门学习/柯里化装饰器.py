import datetime
import time

"""
装饰器：
    函数作为它的参数
    返回值也是一个函数
可以使用@functionname方式，简化调用

分类：有参数装饰器和无参数装饰器：
"""

def logger(fn):
    # 收集可能传入的所有参数
    def wrap(*args,**kwargs):
        # before
        print("args={}, kwargs={}.".format(args,kwargs))
        start = datetime.datetime.now()
        # 这个函数内的*表示对传入的参数进行解包
        # 同时这个是所要执行的函数，其他上下文都是装饰用的
        ret = fn(*args,**kwargs)
        # after
        delta = (datetime.datetime.now()-start).total_seconds()
        if delta > 0.5:
            print("{} took {}s.".format(fn.__name__,delta))
        else:
            print("so fast")
        return ret
    return wrap

@logger # 等价于 add = logger(add)，此处是无参的，如果有参再加上参数即可，如：@logger(args)
def add(x,y):
    time.sleep(0.5)
    return x + y

# add = logger(add)
# print(add(4,6))

print(add(x=4,y=6))

# def feibo(n):
#     if n <= 1:
#         return n
#     elif n <= 2:
#         return 1
#     else:
#         return feibo(n-1) + feibo(n-2)
#
# print(feibo(5))
#
# # n = int(input(">>> input an integer number:"))
# n = 7
# lt = [feibo(i) for i in range(1,n+1)]
# print(lt)


