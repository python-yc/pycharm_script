# -*- coding: utf-8 -*-
"""
Python 把被装饰的函数作为第一个参数传给装 饰器函数。那怎么让装饰器接受其他参数呢？
答案是：创建一个装饰器 工厂函数，把参数传给它，返回一个装饰器，然后再把它应用到要装饰 的函数上。
"""
registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


print('running main()')
print('registry ->', registry)
f1()

'''一个参数化的注册装饰器'''
print('====一个参数化的注册装饰器======')
registry = set()
def register(active=True):
    def decorate(func):
        print('running register(active=%s)->decorate(%s)'
              % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)

        return func
    return decorate


#  @register 工厂函数必须作为函数调用，并且传入所需的参数
@register(active=False)
def f1():
    print('running f1()')


# 即使不传入参数，register 也必须作为函数调用
@register()
def f2():
    print('running f2()')


def f3():
    print('running f3()')


print(registry)
print('===')
# register() 表达式返回 decorate，然后把它应用到 f3 上
register()(f3)
print(register()(f3))
print(registry)
# # register(active=False)(f2)
# print(registry)


print('=======')


@register()
def f4():
    print('running in f4')
