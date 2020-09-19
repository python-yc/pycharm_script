# -*- coding: utf-8 -*-
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for coutry, _ in traveler_ids:
    print(coutry)

"""
元组拆包形式就是平行赋值，也就是说把一个可迭代对象里的元素，
一并赋值到由对应的变量组成的元组中.
"""
latitude, longitude = lax_coordinates  # 元组拆包
print(latitude, longitude, sep='\t\t')

# 还可以用*运算符把一个可迭代对象拆开作为函数的参数
t = (20, 8)
print(divmod(*t))
quotient, remainder = divmod(*t)

print(quotient)

"""
下面是另一个例子，这里元组拆包的用法则是让一个函数可以用元组的形式返回多个值，
然后调用函数的代码就能轻松地接受这些返回值。比如os.path.split()函数就会返回以
路径和最后一个文件名组成的元组(path,last_part)
"""

import os

"""
在进行拆包的时候，我们不总是对元组里所有的数据都感兴趣，_占位符能帮助处理这种情况
"""
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print(filename)

# 在平行赋值中，*前缀只能用在一个变量名前面，但是这个变量可以出现在赋值表达式的任意位置
a, b, *rest = range(5)
a, *body, c, d = range(5)


"""嵌套元组解包"""
# 每个元组内有4个元素，其中最后一个元素是一对坐标
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('DelhiNCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('MexicoCity', 'MX', 20.142, (19.433333, -99.133333)),
    ('NewYork-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('SaoPaulo', 'BR', 19.649, (-23.547778, -46.635833))
]

# ^ 表示居中; .4f 表示保留4位小数
print('{:15}|{:^9}|{:^9}'.format('','lat.','long.'))
fmt='{:15}|{:9.4f}|{:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))
