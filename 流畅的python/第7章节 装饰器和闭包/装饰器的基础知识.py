# -*- coding: utf-8 -*-
"""
装饰器是可调用的对象，其参数是另一个函数（被装饰的函数）。
装饰器可能会处理被装饰的函数，然后把它返回，或者将其替换成另一个 函数或可调用对象。
Python 也支持类装饰器
"""

"""
例子：假如有个名为decorate的装饰器
@decorate
def target():
    print('running target()')
==========
def target(): 
    print('running target()') 
target = decorate(target)

两种写法的最终结果一样：
上述两个代码片段执行完毕后得到的 target 不一定是原来那个 target 函数，而是 decorate(target) 返 回的函数。
"""
# 如下：

def deco(func):
    def inner():
        print('running inner()')
        # func()
    return inner


@deco
def target():
    print("running target()")


# running inner()
target()


'''
可看出：
调用被装饰的 target 其实会运行 inner
审查对象，发现 target 现在是 inner 的引用
'''
target = deco(target)

# <class 'function'>
print(type(target))
# <function deco.<locals>.inner at 0x0000029A868526A8>
print(target)

"""
严格来说，装饰器只是语法糖。
装饰器可以像常规的可调用 对象那样调用，其参数是另一个函数。
有时，这样做更方便，尤其是做 元编程（在运行时改变程序的行为）时。

综上，
装饰器的一大特性是，能把被装饰的函数替换成其他函数。
第二 个特性是，装饰器在加载模块时立即执行。
"""
