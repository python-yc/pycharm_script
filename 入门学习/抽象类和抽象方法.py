# -*- coding: utf-8 -*-

"""
抽象类、抽象方法：
不具体描述的类和方法，比如：类：动物、方法：叫

抽象类不能直接被实例化，同理抽象方法，也不能直接调用；直接使用会报错
作用：只能被用于继承使用。通常被称为ABC类

在 Python 3.4 中，声明抽象基类最简单的方式是子类化 abc.ABC。我在示例 6-1 中就是这么做的。
从 Python 3.0 到 Python 3.3，必须在 class 语句中使用 metaclass= 关键字（例 如，
class Promotion(metaclass=ABCMeta):）
"""
import abc

class Animal(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def bark(self):
        pass

    # 'abstractclassmethod' is deprecated. Use 'classmethod' with
    #     'abstractmethod' instead.
    @abc.abstractclassmethod
    def atest(cls):
        pass


# 一个类只要继承了一个抽象类，那么这个类中必须实现原类中的方法，否则报错
# 即此处只写bark方法，将报错
# class Dog(Animal):
#     # def bark(self):
#     #     print("汪汪汪")
#     pass

# d = Dog() # TypeError: Can't instantiate abstract class Dog with abstract methods bark

class Dog(Animal):
    def bark(self):
        print("汪汪汪")

    def atest(cls):
        print("cls")

class Cat(Animal):
    def bark(self):
        print("喵喵喵")


# a = Animal()    # TypeError: Can't instantiate abstract class Animal with abstract methods bark
d = Dog()

d.bark()
d.atest()

# 若继承的抽象方法未全部实现，则报错
# TypeError: Can't instantiate abstract class Cat with abstract methods atest
# c = Cat()
# c.bark()
