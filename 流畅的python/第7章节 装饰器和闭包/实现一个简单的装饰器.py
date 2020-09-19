# -*- coding: utf-8 -*-

"""
定义了一个装饰器，它会在每次调用被装饰的函数时计时， 然后把经过的时间、传入的参数和调用的结果打印出来
"""

import time

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)
"""
等同于这个写法：
def factorial(n): 
    return 1 if n < 2 else n*factorial(n-1) 

factorial = clock(factorial)

# 叠放装饰器
@d1
@d2 
def f(): 
    print('f')

等同于：
def f(): 
    print('f') 
f = d1(d2(f))
"""
print(factorial.__name__)   # clocked;现在 factorial 保存的是 clocked 函数的引用


if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling snooze(3)')
    print('6! =', factorial(6))

# 的 clock 装饰器有几个缺点：不支持关键字参数，而 且遮盖了被装饰函数的 __name__ 和 __doc__ 属性
# functools.wraps 装饰器把相关的属性从 func 复制到 clocked 中
import functools
def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        pass
