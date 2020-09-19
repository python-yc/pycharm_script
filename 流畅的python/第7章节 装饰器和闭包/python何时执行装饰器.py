# -*- coding: utf-8 -*-
"""
装饰器的一个关键特性是，它们在被装饰的函数定义之后立即运行。这 通常是在导入时（即 Python 加载模块时）
如下例子
"""
"""
如果导入 registration.py 模块（不作为脚本运行）输入如下：
running register(<function f1 at 0x000001BA651B22F0>)
running register(<function f2 at 0x000001BA651B26A8>)

更加证明了：装饰器在被装饰的函数定义之后立即运行
函数装饰器在导入模块时立即执行，而被装饰的 函数只在明确调用时运行。
这突出了 Python 程序员所说的导入时和运 行时之间的区别。
"""
registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()
