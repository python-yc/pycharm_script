# -*- coding: utf-8 -*-
"""
与用户定义的常规类一样，函数使用 __dict__ 属性存储赋予它的用户 属性。
这相当于一种基本形式的注解。一般来说，为函数随意赋予属性 不是很常见的做法，
但是 Django 框架这么做了.
"""
def upper_case_name(obj):
    return ("%s %s" % (obj.first_name, obj.last_name)).upper()

upper_case_name.short_description = 'Customer name'

"""
下面重点说明函数专有而用户定义的一般对象没有的属性。
计算两个属 性集合的差集便能得到函数专有属性列表
"""

class C: pass
obj = C()

def func(): pass

# 用户定义的函数的属性
print(sorted(set(dir(func)) - set(dir(obj))))
