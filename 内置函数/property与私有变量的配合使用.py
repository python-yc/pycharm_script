# -*- coding: utf-8 -*-
"""
私有变量，在变量前面添加两个下划线，目的是将特殊的属性保护起来，不让别人使用；
如果真的使用当然可以使用： 
1、实例名._类名__属性；如：print(p._Person__age);一般不这样使用；
2、通过添加函数对这个私有变量进行返回处理；如下；
class Person:
    def __init__(self):
        self.__age = 18

    def get_age(self):
        return self.__age

p = Person()
print(p.get_age())
p.__age = 20
print(p.get_age())
这样在用户修改这个属性值时误以为修改成功；
如：p.__age = 20；实际是新增了一个属性，并不是改变了__age的值；
这时通过property就可以处理了
"""

class Person:
    def __init__(self):
        self.__age = 18

    # 主要作用是：可以以使用属性的方式，来使用这个函数
    @property
    def age(self):
        return self.__age

p = Person()
print(p.age)
# 这个时候对python这种使用方式熟悉的人就知道不能用这种方式去修改私有变量了，已被保护
# p.age = 20
# print(p.age)

# 通过函数进行处理
class Person:
    def __init__(self):
        self.__age = 18

    def set_age(self, value):
        self.__age = value

    def get_age(self):
        return self.__age

p = Person()
p.set_age(20)
print(p.get_age())

"""
property:
作用：将一些‘属性的操作方法’，关联到某一个属性中；(删改查，详细内容内置解释查看)
补充知识：1、经典类(只有在python2中有，即不继承任何类即可；)：没有继承object；2、新式类：继承object；
"""
print("property第一种方式的使用：")
# 第一种使用方式：
# 注意：python2中不支持这种方式
class Person(object):
    def __init__(self):
        self.__age = 18

    def get_age(self):
        print("---get")
        return self.__age

    def set_age(self, value):
        print("---set")
        self.__age = value

    age = property(get_age, set_age)

p = Person()
print(p.age)

p.age = 21
print(p.age)
print(p.__dict__)

# 第二种使用方式
print("property第二种方式的使用：")
class Person(object):
    def __init__(self):
        self.__age = 18

    @property
    def age(self):
        print("---get")
        return self.__age

    @age.setter
    def age(self, value):
        print("---set")
        self.__age = value

p = Person()
print(p.age)
p.age = 19  # 此处对私有变量age进行修改
print(p.age)
