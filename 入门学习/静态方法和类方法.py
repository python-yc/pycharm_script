# 装饰器不仅可以装饰函数，还可以装饰类；还有一种类装饰器，也可以装饰别人

"""
静态方法：
    1、在类定义中，使用@staticmethod装饰器修饰的方法
    2、调用时，不会隐式的传入参数
        静态方法，只是表明这个方法属于这个这个名词空间。
        函数归在一起，便于管理。
    
"""


def setnameproperty(name):
    def wrap(cls):
        cls.NAME = name
        print(cls.NAME)
        return cls

    return wrap


@setnameproperty('MY CLASS')
class MyClass():
    pass


print(MyClass.__dict__)


########################################################
class MyClass():
    """this is a class"""
    xxx = "XXX"

    def foo(self):
        print("foo")

    # 此处虽然python报错，但是格式是正确的，只是python不建议这样干，
    # 要你绑定实例，不要直接绑定类；即此处不加参数不可以使用实例对象调用
    # 不推荐使用，如果非要不加第一个参数，请使用静态方法，添加一个@staticmethod
    def bar():
        print('bar')

    # 类方法
    # 添加上这个装饰器后，下面的默认参数就不是实例的类或者类本身了
    @classmethod
    def clsmtd(cls):  # 这时回车默认第一个参数就不是self，而是cls
        print('{}.xxx={}'.format(cls.__name__, cls.xxx))  # 实例没有__name__属性，类有

    # 静态方法
    @staticmethod
    def staticmtd():  # 默认没有第一个参数，而且也不出现报错
        print('static')


mc = MyClass()
print(mc.foo())

# 使用实例调用非绑定实例的函数，这样会报错，不可以
# print(mc.bar())
# 同样实例方法也不可以用类去调用，但是加了装饰器的类方法就不同
# MyClass.foo()

# 就需要使用类进行调用，虽然允许，但是不建议
print(MyClass.bar())

# 加了装饰器的类方法两者都可以调用
MyClass.clsmtd()
mc.clsmtd()

MyClass.staticmtd()
mc.staticmtd()

# 这个也是实例化对象后的调用，只是没有赋值给一个参数罢了
MyClass().staticmtd()
