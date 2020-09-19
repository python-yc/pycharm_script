# -*- coding: utf-8 -*-
"""
collections.deque类（双向队列）是一个线程安全、可以快速从两端添加或者删除元素的数据类型。
而且如果想要有一种数据类型来存放“最近用到的几个元素”，deque也是一个很好的选择。这是因为在
新建一个双向队列的时候，你可以指定这个队列的大小，如果这个队列满员了，还可以从反向端删除过
期的元素，然后在尾端添加新的元素
"""

from collections import deque

# maxlen是一个可选参数，代表这个队列可以容纳的元素的数量,一旦设定，这个属性就不能修改
dq = deque(range(10), maxlen=10)
print(dq)

# 队列的旋转操作接受一个参数n，当n>0时，队列的最右边的n个元素会被移动到队列的左边。
# 当n<0时，最左边的n个元素会被移动到右边
dq.rotate(3)
print(dq)

dq.rotate(-4)
print(dq)

# 当试图对一个已满（len(d)==d.maxlen）的队列做尾部添加操作的时候，它头部的元素会被删除掉。注意在下一行里，元素0被删除了
dq.appendleft(-1)
# dq.append(66)
print(dq)

#　在尾部添加3个元素的操作会挤掉-1、1和2
dq.extend([11, 22, 33])
print(dq)

# extendleft(iter)方法会把迭代器里的元素逐个添加到双向队列的左边，因此迭代器里的元素会逆序出现在队列里
dq.extendleft([10, 20, 30, 40])
print(dq)

print(dq[0])
