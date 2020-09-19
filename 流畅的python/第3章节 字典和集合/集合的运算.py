# -*- coding: utf-8 -*-
"""
给定两个集合a和b，a|b返回的是它们的合集，a&b得到的是交集，而a-b 得到的是差集。合理地利用
这些操作，不仅能够让代码的行数变少，还能减少Python程序的运行时间。
"""
needles = {1, 3, 'a'}
haystack = {3, 'a', 5}

found = len(needles & haystack)
print(needles & haystack)
print(found)

# 就算手头没有集合，我们也可以随时建立集合
found = len(set(needles) & set(haystack))
# 另一种写法：
found = len(set(needles).intersection(haystack))
print(found)

needles.add('b')
needles.add('a')
print(needles)
