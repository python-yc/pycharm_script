# -*- coding: utf-8 -*-
from array import array
import reprlib
import math
import numbers


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

    def __eq__(self, other):
        return tuple(self) == tuple(other)

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


v = Vector(range(5))
print(v)
print(v.x)
