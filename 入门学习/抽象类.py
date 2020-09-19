#coding:utf-8
#抽象类的实现
import abc
#声明一个类并且指定当前类的原类（括号内是固定的）
class Human(metaclass=abc.ABCMeta):
    #定义一个抽象方法
    @abc.abstractmethod
    def smoking(self):
        pass
    #定义类抽象方法
    @abc.abstractclassmethod
    def drink(self):
        pass
    #定义静态抽象方法
    @abc.abstractstaticmethod
    def play(self):
        pass
    def sleep(self):
        print('sleeping.....')

#自己组装类 1
#类可以当变量使用
class A():
    pass
def say(self):
    print('Saying......')
say('x')
#类当变量使用与以上直接调用是一样的
A.say = say
a = A()
a.say()

#Python的面向对象概念比较淡薄
class B():
    def say(self):
        print('say ok')
b = B()
b.say()
print('=============')
#自己组装类 2
'''
class A():
    pass
def say(self):
    print('Saying......')

这个执行会报错，缺少参数
即：绑定类是可以的，但是绑定实例不允许
如果要绑定实例，需要借助一个工具，即从types中导入MethodType
a = A()
a.say = say
a.say()
'''
from types import MethodType
class A():
    pass
def say(self):
    print('Saying......')

a = A()
a.say = MethodType(say,A)
a.say()

print("==========================")

#利用type创建一个类
#通过help(type)查看使用方法
###type(name,bases,dict)；其中name使用时可以自定义，bases表示父类，dict是个字典
#首先定义类应该具有的成员函数
def say(self):
    print('Saying......')
def talk(self):
    print('Talking......')
#用type创建一个类
#
#（object，）这个是一个tuple类型，写的是父类名，即元组，只有一个参数也要加 逗号，代表是一个元组
A = type("AName",(object,),{"class_say":say,"class_talk":talk})

#然后可以像正常访问一样使用类
a = A()
#__bases__不支持对象实例
#print(a.__bases__)
print(A.__bases__)
a.class_say()

# 元类演示
#元类写法是固定的，必须继承于type
#元类一般命名以MetaClass结尾

class TulingMetaClass(type):
    #注意以下写法
    def __new__(cls, name, bases,attrs):
        #自己的业务处理
        print('哈哈，我是元类')
        attrs['id'] = '00000'
        attrs['addr'] = 'najing'
        return type.__new__(cls, name, bases,attrs)
#元类定义完就可以使用了，使用注意写法
class Teacher(object,metaclass=TulingMetaClass):
    pass

t = Teacher()
print(t.__dict__)
print(t.id)



