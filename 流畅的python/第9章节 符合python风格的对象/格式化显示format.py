# -*- coding: utf-8 -*-
"""
对微语言的扩展还会用到浮 点数的格式代码 'eEfFgGn%'，而且保持原意，因此绝对要避免重 用代码。
整数使用的格式代码有 'bcdoxXn'，字符串使用的是 's'。

内置的 format() 函数和 str.format() 方法把各个类型的格式化方式 委托给相应的
 .__format__(format_spec) 方法。format_spec 是格 式说明符,
 它是：
 format(my_obj, format_spec) 的第二个参数，或者
 str.format() 方法的格式字符串，{} 里代换字段中冒号后面的部 分
"""

brl = 1 / 2.43
print(format(brl, '0.4f'))

print('1 BRL = {rate:0.2f} USD'.format(rate=brl))

print('1 BRL = {:0.2f} USD'.format(brl))


"""
str.format() 方法使用的 {:} 代换字段表示法（包含转换标 志 !s、!r 和 !a）
！后面可以加s r a 分别对应str() repr() ascii()

格式规范微语言为一些内置类型提供了专用的表示代码,如：
b、d、o、x分别是二进制、十进制、八进制、十六进制  的int型
f 表示小数形式的 float 类型，而 % 表示百分数形式
"""
print('======')
print("{!s}".format('2'))
print("{!r}".format('2'))
print("{!a}".format('2'))

print(42, 'b')
print(format(2/3, '.1%'))
print('{:0.1%}'.format(2/3))

"""
格式规范微语言是可扩展的，因为各个类可以自行决定如何解释format_spec 参数。
例如， datetime 模块中的类，它们的 __format__ 方法使用的格式代码与 strftime() 函数一样
"""
from datetime import datetime
now = datetime.now()

print(format(now, '%H:%M:%S'))
print("It's now {:%I:%M %p}".format(now))


from array import array
import math

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    # def __format__(self, fmt_spec=''):
        # components = (format(c, fmt_spec) for c in self)
        # return '({}, {})'.format(*components)

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)



print('Vector2d class...')
v1 = Vector2d(3, 4)
print(format(v1))
print(format(v1, '.2f'))

print(format(Vector2d(1, 1), 'p'))
print(format(Vector2d(1, 1), '.3ep'))
print(format(Vector2d(1, 1), '0.5fp'))
