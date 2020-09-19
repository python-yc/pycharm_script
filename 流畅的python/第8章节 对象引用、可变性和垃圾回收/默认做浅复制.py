# -*- coding: utf-8 -*-
"""
l1 = [3, [66, 55, 44], (7, 8, 9)]
#  list(l1) 创建 l1 的副本
l2 = list(l1)
还能使用 简洁的 l2 = l1[:] 语句创建副本

构造方法或 [:] 做的是浅复制（即复制了最外层容器，副本中 的元素是源容器中元素的引用）。
如果所有元素都是不可变的，那么这 样没有问题，还能节省内存。但是，如果有可变的元素，可能就会导致 意想不到的问题
"""

l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)

l1.append(100)
l1[1].remove(55)

print('l1:', l1)
print('l2:', l2)

l2[1] += [33, 22]
l2[2] += (10, 11)

print('l1:', l1)
print('l2:', l2)

"""
浅复制没什么问题，但有时我们需要的是深复制（即副本不共享内部对 象的引用）。
copy 模块提供的 deepcopy 和 copy 函数能为任意对象做 深复制和浅复制。
"""
print("===copy module===")
class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


import copy
bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)

print(id(bus1), id(bus2), id(bus3))

# bus1 中的 'Bill' 下车后，bus2 中也没有他了。
#  审查 passengers 属性后发现，bus1 和 bus2 共享同一个列表对 象，因为 bus2 是 bus1 的浅复制副本
bus1.drop('Bill')
print(bus2.passengers)

# bus3 是 bus1 的深复制副本，因此它的 passengers 属性指代另一 个列表。
print(bus3.passengers)
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
