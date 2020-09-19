# -*- coding: utf-8 -*-
import collections

card = collections.namedtuple('card', ['rank', 'suit'])

print(card)

"""
ranks = [str(n) for n in range(2, 11)] + list('JQKA')
suits = 'spades diamonds clubs hearts'.split()
cards = []

for suit in suits:
    for rank in ranks:
        cards.append((rank, suit))

print(cards)
print(len(cards))
"""

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len((self._cards))

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
print(len(deck))
print(deck[0])
from random import choice
# print(choice(deck))
print(deck[:3])
print(deck[12:13])
print(deck[12::13])
