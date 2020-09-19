# -*- coding: utf-8 -*-

"""
在函数式编程范式中，最为人熟知的高阶函数有 map、filter、reduce 和 apply。
apply 函数在 Python 2.3 中标记为过 时，在 Python 3 中移除了，因为不再
需要它了。如果想使用不定量的参 数调用函数，可以编写 fn(*args, **keywords)，
不用再编写 apply(fn, args, kwargs)。
"""

"""
函数式语言通常会提供 map、filter 和 reduce 三个高阶函数（有时 使用不同的名称）。
在 Python 3 中，map 和 filter 还是内置函数，但 是由于引入了列表推导和生成器表达式，
它们变得没那么重要了。列表 推导或生成器表达式具有 map 和 filter 两个函数的功能，
而且更易于 阅读
"""


def factorial(n):
    """return n!"""
    return 1 if n < 2 else n * factorial(n - 1)


fact = factorial

l1 = list(map(fact, range(6)))
print("l1:", l1)
l2 = [fact(n) for n in range(6)]
print("l2:", l2)

l3 = list(map(factorial, filter(lambda n: n % 2, range(6))))
print("l3:", l3)
l4 = [factorial(n) for n in range(6) if n % 2]
print("l4:", l4)

l5 = list(filter(lambda n: n % 2, range(6)))
print("lambda:", l5)

"""
在 Python 2 中，reduce 是内置函数，但是在 Python 3 中放到 functools 模块里了。
这个函数最常用于求和，自 2003 年发布的 Python 2.3 开始，最好使用内置的 sum 函数。
在可读性和性能方面，这是一项重大改善.


all 和 any 也是内置的归约函数:
all(iterable)
如果 iterable 的每个元素都是真值，返回 True；all([]) 返回 True;
any(iterable)
只要 iterable 中有元素是真值，就返回 True；any([]) 返回 False
"""

l6 = [6, 6]
l7 = []
l8 = [0, 6]

print(all(l6))
print(all(l7))
print(all(l8))
