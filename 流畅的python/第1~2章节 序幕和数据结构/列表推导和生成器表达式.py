# -*- coding: utf-8 -*-

# 列表推导式
dummy = [x for x in 'ABC']
print(dummy)

"""列表推导同filter和map的比较"""
symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)

"""生成器表达式:
虽然也可以用列表推导来初始化元组、数组或其他序列类型，但是生成器表达式是更好
的选择。这是因为生成器表达式背后遵守了迭代器协议，可以逐个地产出元素，而不是
先建立一个完整的列表，然后再把这个列表传递到某个构造函数里.

生成器表达式的语法跟列表推导差不多，只不过把方括号换成圆括号而已。
"""
## 用生成器表达式初始化元组和数组

# 如果生成器表达式是一个函数调用过程中的唯一参数，那么不需要额外再用括号把它围起来
symbols = '$¢£¥€¤'
tup = tuple(ord(symbol) for symbol in symbols)
print(type(tup))
print(tup)

# array的构造方法需要两个参数，因此括号是必需的。array构造方法的第一个参数指定了数组中数字的存储方式。
import array
print(array.array('I', (ord(symbol) for symbol in symbols)))

# 使用生成器表达式计算笛卡儿积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tup = ('%s %s' %(c, s) for c in colors for s in sizes)
print(type(tup))
print(next(tup))
