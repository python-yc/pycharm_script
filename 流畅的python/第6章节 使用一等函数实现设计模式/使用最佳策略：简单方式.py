# -*- coding: utf-8 -*-
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:    # 上下文
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


def fidelity_promo(order):
    """为积分为1000或以上的顾客提供5%折扣"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """单个商品为20个或以上时提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


def large_order_promo(order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


# 两个顾客：joe 的积分是 0，ann 的积分是 1100
joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)

"""best_promo 迭代一个函数列表，并找出折扣额度最大 的"""
promos = [fidelity_promo, bulk_item_promo, large_order_promo]

def best_promo(order):
    """"选择可用的最佳折扣"""
    return max(promo(order) for promo in promos)


long_order = [LineItem(str(item_code), 1, 1.0)
                for item_code in range(10)]

print(Order(joe, long_order, best_promo))

banana_cart = [LineItem('banana', 30, .5),
               LineItem('apple', 10, 1.5)]

print(Order(joe, banana_cart, best_promo))


"""
但是有些重复可能会导致不易察觉 的缺陷：若想添加新的促销策略，要定义相应的函数，还要记得把它添
加到 promos 列表中；否则，当新促销函数显式地作为参数传给 Order 时，它是可用的，
但是 best_promo 不会考虑它.

在 Python 中，模块也是一等对象，而且标准库提供了几个处理模块的函 数。
Python 文档是这样说明内置函数 globals 的.

globals()
返回一个字典，表示当前的全局符号表。这个符号表始终针对当前 模块（对函数或方法来说，
是指定义它们的模块，而不是调用它们的模块）。
"""

# 迭代 globals() 返回字典中的各个 name。只选择以 _promo 结尾的名称。
# 过滤掉 best_promo 自身，防止无限递归。
promos = [globals()[name] for name in globals()
          if name.endswith('_promo')
          and name != 'best_promo']

print(promos)
print(globals())
