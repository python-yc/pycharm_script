# -*- coding: utf-8 -*-

"""
任务：
完成一个对当前实例数统计的一个封装类，
即：产生一个实例，计数加1；删除一个实例，计数减1
"""

class Person():
    # 定义一个统计数量的全局变量，为保证不被随便修改，设置为私有
    # 同时也不能被实例直接修改
    __COUNT_INSTANCE = 0

    def __init__(self):
        # 产生一个实例，默认自动调用此函数，因此在此处+1
        # 由于我们想要的数据不能被实例直接修改
        # 因此不能直接使用self进行给值，需使用类进行赋值
        Person.__COUNT_INSTANCE += 1

    def __del__(self):
        # 因此不能直接使用self进行给值，也可以通过实例找到对应的类进行赋值
        self.__class__.__COUNT_INSTANCE -= 1

    # 此处使用类方法，传入一个cls，对其变量进行管理
    @classmethod
    def log(cls):
        print("当前Person类的实例数为 {} 个.".format(cls.__COUNT_INSTANCE))


p1 = Person()
p2 = Person()

# 由于实例也会被删除，所以没必要使用实例进行调用log函数，直接使用类调用，就不会有找不到问题了
Person.log()
del p1
Person.log()
