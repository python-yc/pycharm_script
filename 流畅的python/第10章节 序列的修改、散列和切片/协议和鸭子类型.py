# -*- coding: utf-8 -*-
"""
在 Python 中创建功能完善的序列类型无需使用继 承，只需实现符合序列协议的方法

在面向对象编程中，协议是非正式的接口，只在文档中定义，在代码中 不定义。例如，Python 的
序列协议只需要 __len__ 和 __getitem__ 两 个方法。任何类（如 Spam），只要使用标准的
签名和语义实现了这两 个方法，就能用在任何期待序列的地方。
"""

import collections


Card = collections.namedtuple('Card', ['rand', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


