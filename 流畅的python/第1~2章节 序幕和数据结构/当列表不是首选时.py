# -*- coding: utf-8 -*-

"""
虽然列表既灵活又简单，但面对各类需求时，我们可能会有更好的选择。比如，要存放1000万个浮点数的话，
数组（array）的效率要高得多，因为数组在背后存的并不是float对象，而是数字的机器翻译，也就是字节
表述。这一点就跟C语言中的数组一样。再比如说，如果需要频繁对序列做先进先出的操作，deque（双端队
列）的速度应该会更快
"""

"""
如果在你的代码里，包含操作（比如检查一个元素是否出现在一个集合中）的频率很高，用set（集合）
会更合适。set专为检查元素是否存在做过优化。但是它并不是序列，因为set是无序的
"""

# 2.9.1 数组
"""
如果我们需要一个只包含数字的列表，那么array.array比list更高效。数组支持所有跟可变序列有
关的操作，包括.pop、.insert和.extend。另外，数组还提供从文件读取和存入文件的更快的方法，
如.frombytes和.tofile

以下展示了从创建一个有1000万个随机浮点数的数组开始，到如何把这个数组存放到文件里，再到如何
从文件读取这个数组
"""

from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))
print(floats[-1])

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()


floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])

print(floats2 == floats)
