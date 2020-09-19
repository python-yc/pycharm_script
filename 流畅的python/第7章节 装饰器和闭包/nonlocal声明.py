# -*- coding: utf-8 -*-
def make_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager

"""
make_averager 函数的方法效率不高。在示例 7-9 中，我们 把所有值存储在历史数列中，
然后在每次调用 averager 时使用 sum 求 和。更好的实现方式是，只存储目前的总值和元
素个数，然后使用这两 个数计算均值。

def make_averager(): 
    count = 0 
    total = 0 
    def averager(new_value): 
        count += 1 
        total += new_value 
        return total / count 
    return averager
avg = make_averager()
print(avg(10))

这个执行有报错：
Traceback (most recent call last): 
... 
UnboundLocalError: local variable 'count' referenced before assignment
"""
# 当 count 是数字或任何不可变类型时，count += 1 语句的作 用其实与 count = count + 1 一样。
# 因此，我们在 averager 的定义 体中为 count 赋值了，这会把 count 变成局部变量。total 变量
# 也受 这个问题影响。
######
## 最上面没遇到这个问题，因为我们没有给 series 赋值，我们只是调 用 series.append，
# 并把它传给 sum 和 len。也就是说，我们利用了 列表是可变的对象这一事实。
# 但是对数字、字符串、元组等不可变类型来说，只能读取，不能更新
'''
为了解决这个问题，Python 3 引入了 nonlocal 声明。它的作用是把 变量 标记为自由变量，
即使在函数中为变量赋予新值了，也会变成自由变 量。如果为 nonlocal 声明的变量赋予新值，
闭包中保存的绑定会更 新。
'''
# 正确的实现方式
def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


avg = make_averager()
print(avg(10))
print(avg(12))
