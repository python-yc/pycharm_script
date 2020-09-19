# -*- coding: utf-8 -*-
"""
Python 教程没有提到 classmethod 装饰器，也没有提到 staticmethod。学过 Java 面向对象编程的人可能觉得奇怪，为什么 Python 提供两个这样的装饰器，而不是只提供一个？

classmethod 最常见的用途是 定义备选构造方法，例如示例 9-3 中的 frombytes。注意，
frombytes 的最后一行使用 cls 参数构建了一个新实例，即 cls(*memv)。按照约 定，类
方法的第一个参数名为 cls（但是 Python 不介意具体怎么命 名）

staticmethod 装饰器也会改变方法的调用方式，但是第一个参数不是 特殊的值。其实，静态方法就是普通的函数，
只是碰巧在类的定义体 中，而不是在模块层定义。
"""

class Demo:
    @classmethod
    def classmeth(*args):
        return args

    @staticmethod
    def staticmeth(*args):
        return args


"""不管怎样调用 Demo.klassmeth，它的第一个参数始终是 Demo 类"""
print(Demo.classmeth())
print(Demo.classmeth('spam', 'b'))

"""Demo.statmeth 的行为与普通的函数相似"""
print(Demo.staticmeth())
print(Demo.staticmeth('spam', 'b'))

