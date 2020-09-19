# -*- coding: utf-8 -*-
"""
functools.singledispatch 是 Python 3.4 增加的
单分派泛函数
假设我们在开发一个调试 Web 应用的工具，我们想生成 HTML，显示不 同类型的 Python 对象
我们可能会编写这样的函数:
"""
import html

def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


print(htmlize({1, 2, 3}))
print(htmlize(abs))
print(htmlize('Heimlich & Co.\n- a game'))
# ===================
"""
Python 3.4 新增的 functools.singledispatch 装饰器可以把整体方案 拆分成多个模块，
甚至可以为你无法修改的类提供专门的函数。

singledispatch 创建一个自定义的
htmlize.register 装饰器，把多个函数绑在一起组成一个泛函数
"""
print("===============")
from functools import singledispatch
from collections import abc
import numbers

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


#  各个专门函数使用 @«base_function».register(«type») 装饰
@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)


@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'
