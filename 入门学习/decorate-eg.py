#装饰器
def hello():
    print("Hello world")

hello()
f = hello
f()
#证明f与hello是同一个函数，可用id或者默认属性__name__
print(id(hello))
print(id(f))
print(hello.__name__)
print(f.__name__)
print("=======装饰器的使用介绍及结果如下==============")
"""
装饰器（Decorator）：
- 在不改动函数代码的基础上无限制扩展函数功能的一种机制，本质上讲，
装饰器是一个返回函数的高阶函数
- 装饰器的使用：使用@语法，即在每次要扩展到函数定义前使用@+函数名

装饰器格式：以函数作为参数传入，并且返回一个函数

现在有新的需求：
1、对hello功能进行扩展，每次打印hello之前打印当前系统时间
2、而这个功能又不能改动现有代码
3、==>使用装饰器
"""
import time
#高阶函数，以函数作为参数传入
def printTime(f):
    def wrapper(*args,**kwargs):
        print("Time:",time.ctime())
        #这个是调用传进来的函数
        return f(*args,**kwargs)
    #此处调用wapper函数
    return wrapper
#上面定义了装饰器，使用的时候需要用到@，此符号是python的语法糖
@printTime
def hello():
    print("Hello world")
hello()
#装饰器的好处是，一旦定义，则可以装饰任意函数
#一旦背其装饰，则则把装饰器的功能直接添加到定义函数的功能上
@printTime
def hello2():
    print("I am happy today")
    print("more selection")

hello2()
print("#############===手动执行装饰器===========#########")
'''
装饰器格式：以函数作为参数传入，并且返回一个函数

上面对函数的装饰使用了系统定义的语法糖
下面开始手动执行装饰器
'''
def hello3():
    print("我是手动执行的")
hello3()
hello3 = printTime(hello3)
hello3()
print("解释这个为什么执行两次的结果")
f = printTime(hello3)
f()
print("===========偏函数的使用和结果如下===========")
'''
##偏函数
- 参数固定的函数，相当于一个有特定参数的函数体
- functools.partial的作用，是把一个函数某些参数固定，返回一个新函数

'''
# 把字符串转化成十进制数字
print(int("123456"))
# 求八进制的字符串12345，表示成十进制的数字是多少
#base默认为10，表示十进制
x = int("12345",base=8)
print(x)
print("###########自定义偏函数，如下#########")
#新建一个函数，此函数是默认输入的字符串是16进制数字
#把字符串返回十进制的数字
def int16(x,base=16):
    return int(x,base)

print(int16("12345"))

import functools
int16 = functools.partial(int,base=16)
print(int16("12345"))
