# -*- coding: utf-8 -*-
import operator

method = [name for name in dir(operator) if not name.startswith('_')]

"""
operator 模块以函数的形式提供了 Python 的全部中缀 运算符
['abs', 'add', 'and_', 'attrgetter', 'concat', 'contains', 'countOf', 
'delitem', 'eq', 'floordiv', 'ge', 'getitem', 'gt', 'iadd', 'iand', 
'iconcat', 'ifloordiv', 'ilshift', 'imatmul', 'imod', 'imul', 'index', 
'indexOf', 'inv', 'invert', 'ior', 'ipow', 'irshift', 'is_', 'is_not', 
'isub', 'itemgetter', 'itruediv', 'ixor', 'le', 'length_hint', 'lshift', 
'lt', 'matmul', 'methodcaller', 'mod', 'mul', 'ne', 'neg', 'not_', 'or_', 
'pos', 'pow', 'rshift', 'setitem', 'sub', 'truediv', 'truth', 'xor']
"""
# print(method)
