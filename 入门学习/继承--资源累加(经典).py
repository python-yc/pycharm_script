# -*- coding: utf-8 -*-
"""
一、属性、方法
1、类属性；
2、实例属性；
3、实例方法（不可以直接使用类进行调用，需实例化）；
4、类方法(实例化调用和类直接调用都支持)；
5、静态方法(实例化调用和类直接调用都支持)；

二、继承
继承的同时，新增属性和功能
# 通过super调用父类初始化方法，实现属性增加；
# super().__init__()
# 除了super还有一种方式，使用类名调用父类方法资源
# 即B.__init__(self) # 此处需要传入一个self
B.t1(self)
super().t1()
"""


class B:
    # 类属性
    a = 'a'

    # 实例属性
    def __init__(self, name):
        self.b = 'b'

    # 实例方法（不可以直接使用类进行调用，需实例化）
    def t1(self):
        print('t1')

    # 类方法(实例化调用和类直接调用都支持)
    @classmethod
    def t2(cls):
        print('t2')

    # 静态方法(实例化调用和类直接调用都支持)
    @staticmethod
    def t3():
        print('t3')


class A(B):
    c = 'c'
    def __init__(self):
        # 调用父类的初始化方法，不主动调用，则会被覆盖，然后再实例化A调用父类的属性则报错

        # 除了super还有一种方式，使用类名调用父类方法资源
        # 即B.__init__(self) # 此处需要传入一个self
        # 通过super调用父类初始化方法，实现属性增加；
        super().__init__('yc')

        # A类自己新增属性（还有一种就是直接将父类的属性再次重写一次，不太好）
        self.d = 'd'

    def t1(self):
        # 调用父类中的t1，不主动调用，则被覆盖，不能达到使用相同名称方法，新增功能
        print('A类中的t1执行结果')
        B.t1(self)
        super().t1()
        print('首先主动调用父类中的t1方法，然后在A类中新增更多功能同名的t1')


a_obj = A()
print(A.a)
print(a_obj.b)
print(a_obj.__dict__)
a_obj.t1()
A.t2()
A.t3()
print(a_obj.d)
a_obj.t1()

