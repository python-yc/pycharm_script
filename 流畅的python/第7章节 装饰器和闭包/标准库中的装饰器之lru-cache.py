# -*- coding: utf-8 -*-
"""
Python 内置了三个用于装饰方法的函数：property、classmethod 和 staticmethod

functools.wraps 只是标准库中拿来即用的装饰器之一。它的作用是协助构建行为 良好的装饰器。
以下介 绍 functools 模块中最让人印象深刻的两个装饰器：lru_cache 和 singledispatch（Python 3.4 新增）。
"""
'''使用functools.lru_cache做备忘
functools.lru_cache 是非常实用的装饰器，它实现了备忘 （memoization）功能。这是一项
优化技术，它把耗时的函数的结果保存 起来，避免传入相同的参数时重复计算。
LRU 三个字母是“Least Recently Used”的缩写，表明缓存不会无限制增长，一段时间不用的缓存 条目会被扔掉
'''
# 生成第 n 个斐波纳契数这种慢速递归函数适合使用 lru_cache，如示例

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


"""
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


[0.00000050s] fibonacci(0) -> 0
[0.00000040s] fibonacci(1) -> 1
[0.00005570s] fibonacci(2) -> 1
[0.00000030s] fibonacci(1) -> 1
[0.00000040s] fibonacci(0) -> 0
[0.00000030s] fibonacci(1) -> 1
...还有很多

以上代码运行：
浪费时间的地方很明显：fibonacci(1) 调用了 8 次，fibonacci(2) 调用了 5 次……

=========
但是，如果增加两行代码，使用 lru_cache，性能会显 著改善
[0.00000050s] fibonacci(0) -> 0
[0.00000050s] fibonacci(1) -> 1
[0.00006470s] fibonacci(2) -> 1
[0.00000090s] fibonacci(3) -> 2
[0.00008380s] fibonacci(4) -> 3
[0.00000070s] fibonacci(5) -> 5
[0.00010290s] fibonacci(6) -> 8
8结束，无重复计算
"""
import functools
#  注意，必须像常规函数那样调用 lru_cache。这一行中有一对括 号：@functools.lru_cache()。
#  这么做的原因是，lru_cache 可以 接受配置参数
# 这里叠放了装饰器：@lru_cache() 应用到 @clock 返回的函数上
@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


"""
lru_cache 可以使用两个可选的参数来配置。它的签名 是：
functools.lru_cache(maxsize=128, typed=False)
maxsize 参数指定存储多少个调用的结果。缓存满了之后，旧的结果会 被扔掉，腾出空间。
为了得到最佳性能，maxsize 应该设为 2 的 幂。typed 参数如果设为 True，把不同参数类型
得到的结果分开保存，即把通常认为相等的浮点数和整数参数（如 1 和 1.0）区分开
"""

if __name__ == '__main__':
    print(fibonacci(6))
