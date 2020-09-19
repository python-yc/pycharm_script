# -*- coding: utf-8 -*-

"""
为什么切片和区间会忽略最后一个元素:
在切片和区间操作里不包含区间范围的最后一个元素是Python的风格，这个习惯
符合Python、C和其他语言里以0作为起始下标的传统。这样做带来的好处如下:

1、我们也可以快速看出切片和区间里有几个元素：range(3)和my_list[:3]都返回3个元素;
2、这样做也让我们可以利用任意一个下标来把序列分割成不重叠的两部分，只要写成my_list[:x]和my_list[x:]就可以了;
"""

# 对对象进行切片：
# s[a:b:c]的形式对s在a和b 之间以c为间隔取值。c的值还可以为负，负值意味着反向取值；
"""[a:b:c] 对应 start stop step 3个参数"""
s = 'bicycle'
print(s)
print(s[::3])
print(s[::-1])

"""
另一个例子是在第1章中用deck[12::13]的形式在未洗过的牌里把每种花色的A拿出来
deck[12::13]
[Card(rank='A',suit='spades'),Card(rank='A',suit='diamonds'),Card(rank='A',suit='clubs'),Card(rank='A',suit='hearts')]
"""


invoice="""
0.....6................................40........52...55........
1909  PimoroniPiBrella                     $17.50
14896 mmTactileSwitchx20                    $4.95
1510  PanaviseJr.-PV-201                   $28.00
1601  PiTFTMiniKit320x240                  $34.95
"""

SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(50, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
# print(line_items)

for item in line_items:
    print(item[UNIT_PRICE].replace(' ', '', 3), item[DESCRIPTION])


# 给切片赋值
l = list(range(10))
print(l)
l[2:5] = [20, 30]
print(l)
del l[5:7]
print(l)
l[3::2] = [11, 22]
print(l)
# l[2:5] = 100    # TypeError: can only assign an iterable
l[2:5] = [100]
print(l)
