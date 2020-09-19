# -*- coding: utf-8 -*-
import bisect
import random

"""
排序很耗时，因此在得到一个有序序列之后，我们最好能够保持它的有序。bisect.insort就是
为了这个而存在的。insort(seq,item)把变量item插入到序列seq中，并能保持seq 的升序顺序
"""

size = 7
random.seed(1729)
my_list = []
for i in range(size):
    new_item = random.randrange(size*2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)
