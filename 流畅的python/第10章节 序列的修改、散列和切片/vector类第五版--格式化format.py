# -*- coding: utf-8 -*-
"""
对微语言的扩展还会用到浮 点数的格式代码 'eEfFgGn%'，而且保持原意，因此绝对要避免重 用代码。
整数使用的格式代码有 'bcdoxXn'，字符串使用的是 's'。
"""
from array import array
import reprlib
import math
import numbers

import functools
import operator


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components))

    # def __eq__(self, other):
    #     return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    # 以下为比第一版新添加
    def __len__(self):
        return len(self._components)

    # def __getitem__(self, index):
    #     return self._components[index]

    # 对 getitem方法改进
    # 能处理切片的__getitem__方法
    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    """
    Vector2d 变成 Vector 之后，就没办法通过名称访问向量的分量了 （如 v.x 和 v.y）。现在我们
    处理的向量可能有大量分量。不过，若能 通过单个字母访问前几个分量的话会比较方便。比如，用 x、y
    和 z 代 替 v[0]、v[1] 和 v[2]。

    >>> v.y, v.z, v.t 
    (1.0, 2.0, 3.0)
    """

    shortcut_names = 'xyzt'

    def __getattr__(self, name):
        cls = type(self)

        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    # def __eq__(self, other):
    #     return tuple(self) == tuple(other)

    # 为了提高比较的效率，Vector.__eq__ 方法在 for 循环中使用 zip 函数
    # zip 函数生成一个由元组构成的生成器，元组中的元素来自参数传入 的各个可迭代对象。
    # 如果不熟悉 zip 函数，请阅读 出色的 zip 函数
    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for a, b in zip(self, other):
            if a != b:
                return False
        return True

    """
    # all 函数调用; 与上述逻辑一样
    def __eq__(self, other):
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))
    """

    """
    使用 reduce 函数时最好提供第三个参 数，reduce(function, iterable, initializer)，
    这样能避 免这个异常：TypeError: reduce() of empty sequence with no initial value（
    这个错误消息很棒，说明了问题，还提供了 解决方法）。如果序列为空，initializer 是返回的结果；
    否 则，在归约中使用它作为第一个参数，因此应该使用恒等值。比 如，对 +、| 和 ^ 来说， 
    initializer 应该是 0；而对 * 和 & 来 说，应该是 1
    """
    def __hash__(self):
        # hashes = (hash(x) for x in self._components)
        # 或者用 map方法代替
        hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes, 0)

    def angle(self, n):
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n-1])
        if (n == len(self) - 1) and  (self[-1] < 0):
            return math.pi * 2 -a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_spec=''):
        import itertools
        if fmt_spec.endswith('h'):
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(components))
