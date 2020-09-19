# -*- coding: utf-8 -*-
"""
lambda 关键字在 Python 表达式内创建匿名函数;

然而，Python 简单的句法限制了 lambda 函数的定义体只能使用纯表达 式。换句话说，
lambda 函数的定义体中不能赋值，也不能使用 while 和 try 等 Python 语句;
"""

# 使用lambda 这样就不用单独写个函数了
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=lambda word: word[::-1]))
