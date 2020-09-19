'''
返回函数：
    可以返回具体的值
    也可以返回一个函数作为结果
'''
def myF(a):
    print('In myF')
    return None

a = myF(8)
print(a)
#函数作为返回值返回，被返回的函数再函数体内定义
def myF2():
    def myF3():
        print("In myF3")
        return 5
    return myF3

#使用上面定义
#调用myF2，返回一个函数myF3，赋值给f3
f3 = myF2()
#打印出f3是一个函数##########
print(type(f3))
print(f3)
print(f3())
myF2()

#复杂一点的返回函数的例子
#args：参数列表
#1、myF4定义函数，返回内部定义的函数myF5
#2、myF5使用了外部的变量，这个变量是myF4
def myF4(*args):
    def myF5():
        rst = 0
        for n in args:
            rst += n
        return rst
    return myF5

f5 = myF4(1,2,3,4,5,6,7,8)
#f5的调用方式
print(f5())
f6 = myF4(10,20,30,40,50)
print(f6)
print(f6())
#myF4是一个标准的闭包
#闭包的坑
def count():
    #定义列表，列表里存放的是定义的函数
    fs  = []
    for i in range(1,4):
        #定义一个函数f ，f是一个闭包结构
        def f():
            return i * i
        fs.append(f)
    return fs

f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())
'''
###出现的问题：
- 造成上述这种状况的原因是，返回函数引用了变量i，i并非立即执行，
而是当三个函数都返回的时候才统一使用，此时i已经变成了3，最终调用
的时候，都返回的是3*3。
- 此问题描述成：返回闭包时，返回函数不能引用任何循环变量
- 解决方案：再创建一个函数，用该函数的参数绑定循环变量的当前值，无论
循环变量以后如何改变，已经绑定函数参数值不在改变
'''
print("======================")
def count1():
    def f(j):
        def g():
            return j * j
        return g
    #定义列表，列表里存放的是定义的函数
    fs  = []
    for i in range(1,4):
        fs.append(f(i))
    return fs

f1,f2,f3 = count1()
print(f1())
print(f2())
print(f3())


