# -*- coding: utf-8 -*-

# 字典的多种创建方式
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})

print(a == b == c == d == e)

# 字典推导式
DIAL_CODES = [
    (86, 'China'), (91, 'India'), (1, 'UnitedStates'), (62, 'Indonesia'),
    (55, 'Brazil'), (92, 'Pakistan'), (880, 'Bangladesh'), (234, 'Nigeria'),
    (7, 'Russia'), (81, 'Japan'),
]

country_code = {country: code for code, country in DIAL_CODES if code > 66}
print(country_code)
