# -*- coding: utf-8 -*-


import re

pattern = re.compile(r'\d+')

reg = pattern.findall("i am 18 years old and 175 high")

print(reg)


reg = pattern.finditer("i am 18 years old and 175 high")

print(type(reg))    # <class 'callable_iterator'>,所以使用group方法

for i in reg:
    print(i.group())

