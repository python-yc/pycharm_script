# -*- coding: utf-8 -*-
"""
在 Python 中，函数是一等对象。编程语言理论家把“一等对象”定义为满 足下述条件的程序实体：
1/在运行时创建
2/能赋值给变量或数据结构中的元素
3/能作为参数传给函数
4/能作为函数的返回结果
"""

def factorial(n):
    """return n!"""
    return 1 if n < 2 else  n * factorial(n-1)


print(factorial(5))

fac = factorial
print(type(fac))
print(fac.__doc__)
