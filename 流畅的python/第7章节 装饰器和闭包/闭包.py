# -*- coding: utf-8 -*-
"""
闭包指延伸了作用域的函数，其中包含函数定义体中引用、但是 不在定义体中定义的非全局变量
"""

'''
注意，series 是 make_averager 函数的局部变量，因为那个函数的定 义体中初始化了 
series：series = []。可是，调用 avg(10) 时，make_averager 函数已经返回了，
而它的本地作用域也一去不复 返了.

在 averager 函数中，series 是自由变量（free variable）。
这是一个 技术术语，指未在本地作用域中绑定的变量

从 series = [] 到 return total/len(series)称之为 闭包；
series为自由变量

同样证明了后面使用装饰器，即：函数中定义函数的理由；而不是直接借助一个函数处理
'''

def make_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager


avg = make_averager()
print(avg(10))
print(avg(12))

"""
averager 的闭包延伸到那个函数的作用域之外，包含自由 变量 series 的绑定
审查返回的 averager 对象，我们发现 Python 在 __code__ 属性（表示 编译后的函数定义体）中保存局部变量和自由变量的名称
"""
print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)
# 综上，闭包是一种函数，它会保留定义函数时存在的自由变量的绑定， 这样调用函数时，
# 虽然定义作用域不可用了，但是仍能使用那些绑定
# 注意，只有嵌套在其他函数中的函数才可能需要处理不在全局作用域中 的外部变量
