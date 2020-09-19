# -*- coding: utf-8 -*-

"""
接受函数为参数，或者把函数作为结果返回的函数是高阶函数（higher- order function）。
map 函数就是一例

此外，内置函 数 sorted 也是：可选的 key 参数用于提供一个函数，它会应用到各个 元素上进行排序
"""

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))
print(sorted(fruits, reverse=True))

def reverse(word):
    return word[::-1]


print(reverse('testing'))

print(sorted(fruits, key=reverse))
