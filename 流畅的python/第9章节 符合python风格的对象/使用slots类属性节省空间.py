# -*- coding: utf-8 -*-
"""
默认情况下，Python 在各个实例中名为 __dict__ 的字典里存储实例属 性
为了使用底层的散列表提升访问速度，字典会消 耗大量内存。如果要处理数百万个属性不多的实例，通过 __slots__ 类属性，能节省大量内存
方法是让解释器在元组中存储实例属性，而不用字典

继承自超类的 __slots__ 属性没有效果。Python 只会使用 各个类中定义的 __slots__ 属性
"""
import math

class Vector2d:
    __slots__ = ('__x', '__y')
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.__x, self.__y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.__x, self.__y)

    def __bool__(self):
        return bool(abs(self))

    # def __format__(self, fmt_spec=''):
        # components = (format(c, fmt_spec) for c in self)
        # return '({}, {})'.format(*components)

    def angle(self):
        return math.atan2(self.__y, self.__x)

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


"""
在类中定义 __slots__ 属性的目的是告诉解释器：“这个类中的所有实 例属性都在这儿了！”
这样，Python 会在各个实例中使用类似元组的结 构存储实例变量，从而避免使用消耗内存的
 __dict__ 属性。如果有数 百万个实例同时活动，这样做能节省大量内存

__slots__ 的问题:
1/每个子类都要定义 __slots__ 属性，因为解释器会忽略继承的 __slots__ 属性
2/实例只能拥有 __slots__ 中列出的属性，除非把 '__dict__' 加 入 __slots__ 中（这样做就失去了节省内存的功效）
3/如果不把 '__weakref__' 加入 __slots__，实例就不能作为弱引 用的目标
"""

print(Vector2d.typecode)
v = Vector2d(2, 3)
print(v.typecode)


# AttributeError: 'Vector2d' object attribute 'typecode' is read-only
# 将 __slots__ = ('__x', '__y') 注释即可运行下面的赋值
# 私有化变量，使其成为只读 变量

# v.typecode = 'f'
# print(v.typecode)
# print(Vector2d.typecode)
