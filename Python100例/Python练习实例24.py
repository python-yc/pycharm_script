"""
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...
求出这个数列的前20项之和。

程序分析：请抓住分子与分母的变化规律
"""
#方法一：
a = 2.0
b = 1.0
s = 0
for n in range(1,21):
    s += a/b
    t = a
    a = a + b
    b = t
print(s)

#方法二：
a = 2.0
b = 1.0
s = 0
for n in range(1,21):
    s += a/b
    a,b = a+b,a
print(s)

#方法三：

from functools import reduce
a = 2.0
b = 1.0
l = []
l.append(a/b)
for n in range(1,20):
    b,a = a,a + b
    l.append(a/b)
print(reduce(lambda x,y: x + y,l))
