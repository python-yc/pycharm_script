# -*- coding: utf-8 -*-

print('sort==')
"""
list.sort方法会就地排序列表，也就是说不会把原列表复制一份。这也是这个方法的返回值
是None的原因，提醒你本方法不会新建一个列表。在这种情况下返回None其实是Python的一个
惯例：如果一个函数或者方法对对象进行的是就地改动，那它就应该返回None，好让调用者知
道传入的参数发生了变动，而且并未产生新的对象。例如，random.shuffle函数也遵守了这个
惯例
"""
print('sorted==')
"""
与list.sort相反的是内置函数sorted，它会新建一个列表作为返回值。这个方法可以
接受任何形式的可迭代对象作为参数，甚至包括不可变序列或生成器（见第14章）。而
不管sorted接受的是怎样的参数，它最后都会返回一个列表
"""

# list.sort方法还是sorted函数，都有两个可选的关键字参数

# 1、reverse：如果被设定为True，被排序的序列里的元素会以降序输出
# 2、key：一个只有一个参数的函数，这个函数会被用在序列里的每一个元素上，所产生的
#   结果将是排序算法依赖的对比关键字。比如说，在对一些字符串排序时，可以用key=str.lower
#   来实现忽略大小写的排序，或者是用key=len进行基于字符串长度的排序。这个参数的默认值是
#   恒等函数（identityfunction），也就是默认用元素自己的值来排序

fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))
print("key=len:")
print(sorted(fruits, key=len, reverse=True))

print('=====')
# 惯例：如果一个函数或者方法对对象进行的是就地改动，那它就应该返回None
print(fruits.sort(reverse=True))
print(fruits)
