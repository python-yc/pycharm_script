# -*- coding: utf-8 -*-

"""
不仅 Python 函数是真正的对象，任何 Python 对象都可以表现得像函 数。为此，只需实现实例方法 __call__
"""

import random

class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


bingo = BingoCage(range(3))
print(bingo.pick())

# 实现__call__魔法函数后，实例可以当函数调用
print(bingo())
print(callable(bingo))
