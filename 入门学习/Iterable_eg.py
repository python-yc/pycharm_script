#通过isinstance判断某个变量是否是一个实例

#判断是否可迭代
from collections import Iterable
ll = [1,2,3,4,5]

#返回True为可迭代，但不代表是迭代器
print(isinstance(ll,Iterable))

#这个可以判断出是否是一个迭代器
#返回True为真
from collections import Iterator
print(isinstance(ll,Iterator))

print("iter()函数的使用介绍及结果如下")

#iter函数
s = 'i love python'

print(isinstance(s,Iterable))
print(isinstance(s,Iterator))

s_iter = iter(s)
print(isinstance(s_iter,Iterable))
print(isinstance(s_iter,Iterator))

# 直接使用生成器
L = [x*x for x in range(5)] #放在中括号中是列表
g = (x*x for x in range(5)) #放在小括号中就是生成器

print(type(L))
print(type(g))
print("#################生成器的案例##############")
#在函数odd()中，yield负责返回
def odd():
    print("Step 1")
    yield 1
    print("Step 2")
    yield 2
    print("Step 3")
    yield 3
#odd()是调用生成器，不可以直接使用，需要next调用
#不可以直接多次这样去掉用，这样的结果每次都是从头执行
# one = next(odd())
# print(one)
# two = next(odd())
# print(two)

#声明一个生成器
g = odd()
one = next(g)
print(one)

two = next(g)
print(two)
print("############")
##使用for循环调用生成器
def fib(max):
    n,a,b = 0,0,1   #注意写法，多个变量同时定义的写法
    while n < max:
        yield b
        a,b = b,a+b   #注意写法
        n += 1
    #需要注意，爆出异常的返回值是return的返回值
    return 'Done'

g = fib(5)

for i in range(8):
    rst = next(g)
    print(rst)


