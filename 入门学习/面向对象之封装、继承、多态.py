# coding:utf-8
class Person():
    # name是共有的成员
    name = "liuying"
    # age是私有的成员
    __age = 18
    _sex = "boy"


p = Person()
# name是公有变量
print(p.name)
# age是私有变量
# 注意报错信息
# print(p.__age)
# name mangling技术
print(Person.__dict__)
# 受保护的访问语法
print(p._sex)
# 私有变量的访问方式
print(p._Person__age)
print("=============")


# 继承的语法
class Person():
    name = "Ada"
    age = 1

    def sleep(self):
        print("Sleeping......")


# 父类写在括号内
class Teacher(Person):
    pass


t = Teacher()
print(t.name)
print(Teacher.name)
print("=============")


# 构造函数
class Animal():
    def __init__(self):
        print("Animal")

    pass


class PaxingAni(Animal):
    def __init__(self, name):
        print("Paxing Dowu")

    pass


class Dog(PaxingAni):
    # __init__就是构造函数
    # 每次实例化的时候，第一个被调用
    # 因为主要工作是进行初始化，所以得名
    # 构造函数有一特点，实例化时自动被执行
    def __init__(self):
        print("I am init in dog")


# 实例化的时候，括号内的参数跟构造函数参数匹配
# 实例化Dog时，找到Dog的构造函数后，参数匹配，不会向上查找
kaka = Dog()


class Cat(PaxingAni):
    pass


# 如果直接Tom = Cat()构造，由于Cat没有构造函数，则会向上查找，但是由于参数不匹配，则报错
# TypeError: __init__() missing 1 required positional argument: 'name'

class Fish():
    def __init__(self):
        self.name = name

    def swim(self):
        print("i am swimming......")


class Bird():
    def __init__(self, name):
        self.name = name

    def fly(self):
        print("I am flying......")


class Person():
    def __init__(self, name):
        self.name = name

    def work(self):
        print("working......")


class SuperMan(Person, Bird, Fish):
    def __init__(self, name):
        self.name = name


print("多继承")
# 多继承的例子
s = SuperMan("xs")
s.fly()
s.swim()
print("单继承")
# 单继承
n = "xiaoming"
st = Person(n)
st.work()
# print(SuperMan.__mro__)

print(SuperMan.__bases__)
lst = SuperMan.__bases__
for i in lst:
    print(i)
