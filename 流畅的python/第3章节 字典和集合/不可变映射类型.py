# -*- coding: utf-8 -*-
"""
从Python3.3开始，types模块中引入了一个封装类名叫MappingProxyType。如果给这个类一个映射，
它会返回一个只读的映射视图。虽然是个只读视图，但是它是动态的。这意味着如果对原映射做出了改动，
我们通过这个视图可以观察到，但是无法通过这个视图对原映射做出修改.
"""

from types import MappingProxyType

d = {'a': 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy['a'])

# TypeError: 'mappingproxy' object does not support item assignment
# d_proxy['b'] = 'B'
# print(d_proxy)

"""d_proxy是动态的，也就是说对d所做的任何改动都会反馈到它上面"""
d['b'] = 'B'
print(d_proxy)
print(d_proxy['b'])
