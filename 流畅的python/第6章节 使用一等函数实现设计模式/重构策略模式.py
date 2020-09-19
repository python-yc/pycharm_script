# -*- coding: utf-8 -*-
"""
在 Python 3.4 中，声明抽象基类最简单的方式是子类化 abc.ABC。我在示例 6-1 中就是这么做的。
从 Python 3.0 到 Python 3.3，必须在 class 语句中使用 metaclass= 关键字（例 如，
class Promotion(metaclass=ABCMeta):）
"""

# 实现 Order 类，支持插入式折扣策略
from abc import ABC, abstractmethod
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
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):   # 策略：抽象基类
    @abstractmethod
    def discount(self, order):
        """返回折扣金额（正值）"""


class FidelityPromo(Promotion): # 第一个具体策略
    """为积分为1000或以上的顾客提供5%折扣"""
    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):  # 第二个具体策略
    """单个商品为20个或以上时提供10%折扣"""
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount


class LargeOrderPromo(Promotion):   # 第三个具体策略
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0


# 使用不同促销折扣的 Order 类示例
# 两个顾客：joe 的积分是 0，ann 的积分是 1100
joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
#  有三个商品的购物车
cart = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)]

print(Order(joe, cart, FidelityPromo()))
print(Order(ann, cart, FidelityPromo()))

# banana_cart 中有 30 把香蕉和 10 个苹果
banana_cart = [LineItem('banana', 30, .5),
               LineItem('apple', 10, 1.5)]

print(Order(joe, banana_cart, BulkItemPromo()))

long_order = [LineItem(str(item_code), 1, 1.0)
                for item_code in range(10)]

print(Order(joe, long_order, LargeOrderPromo()))
print(type(joe))
