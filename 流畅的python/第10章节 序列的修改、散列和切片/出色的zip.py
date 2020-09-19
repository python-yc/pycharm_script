# -*- coding: utf-8 -*-
"""
出色的 zip 函数 使用 for 循环迭代元素不用处理索引变量，还能避免很多缺陷，但 是需要一些特殊的
实用函数协助。其中一个是内置的 zip 函数。使 用 zip 函数能轻松地并行迭代两个或更多可迭代对象，
它返回的元 组可以拆包成变量，分别对应各个并行输入中的一个元素.

zip 函数的名字取自拉链系结物（zipper fastener），因为 这个物品用于把两个拉链边的链牙咬合在
一起，这形象地说明 了 zip(left, right) 的作用。zip 函数与文件压缩没有关 系
"""

"""
为了避免在 for 循环中手动处理索引变量，还经常使用内置的 enumerate 生成器函数。如果
你不熟悉 enumerate 函数，一定要 阅读“Build-in Functions”文档 
https://docs.python.org/3/library/functions.html#enumerate）。
"""

z1 = zip(range(3), 'ABC')
print(z1)
print(list(z1))

# zip 有个奇怪的特性：当一个可迭代对象耗尽后，它不发出警告 就停止
z2 = list(zip(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3]))
print(z2)

from itertools import zip_longest

#  itertools.zip_longest 函数的行为有所不同：使用可选的 fillvalue（默认值为 None）
# 填充缺失的值，因此可以继续产 出，直到最长的可迭代对象耗尽
z3 = list(zip_longest(range(3), 'ABC',  [0.0, 1.1, 2.2, 3.3], fillvalue=-100))
print(z3)
