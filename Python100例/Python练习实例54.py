"""
题目：取一个整数a从右端开始的4〜7位。

程序分析：可以这样考虑： 
(1)先使a右移4位。 
(2)设置一个低4位全为1,其余全为0的数。可用~(~0<<4) 
(3)将上面二者进行&运算
"""
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    a = int(input('input a number:\n'))
    b = a >> 4
    c = ~(~0 << 4)
    d = b & c
    # 转换成八进制
    #print('%o\t%o' %(a,d))
    print(d)

x = 10
print('%o' %x)
z = 27
print('%x' % z)


