# -*- coding: utf-8 -*-
"""
用namedtuple构建的类的实例所消耗的内存跟元组是一样的，因为字段名都被存在对应的类
里面。这个实例跟普通的对象实例比起来也要小一些，因为Python不会用__dict__来存放这
些实例的属性.
"""

"""
创建一个具名元组需要两个参数，一个是类名，另一个是类的各个字段的名字。后者可以
是由数个字符串组成的可迭代对象，或者是由空格分隔开的字段名组成的字符串
"""
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')

"""
存放在对应字段里的数据要以一串参数的形式传入到构造函数中
（注意，元组的构造函数只接受单一的可迭代对象）
"""
# City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
# 你可以通过字段名或者位置来获取一个字段的信息
print(tokyo.population)
print(tokyo[1])

# _fields属性是一个包含这个类所有字段名称的元组
print(City._fields)

print('===============')
#　类名：LatLong；参数为：lat long
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('DelhiNCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
print(delhi_data)

# 用_make()通过接受一个可迭代对象来生成这个类的一个实例，它的作用跟City(*delhi_data)是一样的。
delhi = City._make(delhi_data)

#　_asdict()把具名元组以collections.OrderedDict的形式返回，我们可以利用它来把元组里的信息友好地呈现出来
print(delhi._asdict())
