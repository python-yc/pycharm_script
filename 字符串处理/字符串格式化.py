# -*- coding:utf-8 -*-
s = "I am very very very lucky"
for i in range(len(s)):
    print(str(i)+s[i],end=" ")

"""
1、字符串的格式化是一种拼接字符串输出样式的手段，更灵活方便
    join拼接只能使用分隔符，且要求被拼接的是可迭代对象
    + 拼接字符串还算方便，但是非字符串需要先转换为字符串才能拼接
2、在2.5版本之前，只能使用printf style风格的print输出
    printf-style formatting，来自于C语言的printf函数
    格式要求
        占位符：使用%和格式字符组成，例如%s、%d等；
            s调用str()，r会调用repr()。所有对象都可以被这两个转换。
        占位符中还可以插入修饰字符，例如%03d###表示打印3个位置，不够前面补零###；
        format % values，格式字符串和被格式的值之间用%分隔；
        values只能是一个对象，或是一个和格式字符串占位符串占位符数目相等的元组，或一个字典。
输出20%的方式
    print("%s%%"%20)
    ***print("%s\%"%20) #这个不可以***
print("I am %-5d" %(20))  # 这个%-5d中的-表示左对其方式，默认不加为右对齐，5表示占5个字符位
    
3、format函数格式化字符串语法--Python鼓励使用
    "{}{xxx}".format(*args,**kwargs) ->str
    args是位置参数，是一个元组
    kwargs是关键字参数，是一个字典
    花括号表示占位符
    {}表示按照顺序匹配位置参数，{n}表示取位置参数索引为n的值
    {xxx}表示在关键字中搜索名称一致的     如：print("{server}: {}".format('ok',server='Web server info'))
    {{}}表示打印花括号
4、对齐
'{0}*{1}={2:<2}'.format(3,2,3*2)        < 表示左对齐，2表示占两个位置
'{0}*{1}={2:<02}'.format(3,2,3*2)       < 表示左对齐，02表示不足两个位置右边补零2*3=60
'{0}*{1}={2:>02}'.format(3,2,3*2)       > 表示右对齐，（不需要添加，默认就是右对齐），不足左边补零2*3=06
'{:^30}'.format('centered')              #           centered           ：居中，默认两天添加空格
'{:*^30}'.format('centered')             #***********centered***********：居中，两边*补齐
5、进制
"int:{0:d}; hex:{0:x}; oct:{0:o}; bin:{0:b}".format(42)
"int:{0:d}; hex:{0:#x}; oct:{0:#o}; bin:{0:#b}".format(42)
octets = [192,168,0,1]
'{:02X}{:02X}{:02X}{:02X}'.format(*octets)

"""
print()
a = "Hello"
print(a+",I am %03d old." %18)
print("i am %s,my number is %05d" %("yucai",18))
print("i am %s,my number is %-5d" %("yucai",18))
print("i am %s,my number is %5d" %("yucai",18))
print("i am %s,my number is %3.2f" %("yucai",18))

print("%s%%" % 20)
# %x表示用16进制，X表示大写
print('%3.2f%%,0x%x,0X%02X' %(85.7654,10,15))

print('%10.2f%%,0x%x,0X%02X' %(85.7,10,15))

# %30.2f中30表示占位数，由于又限制了小数的位数，所以小数末尾无法加0
print('%30.2f%%,0x%x,0X%02X' %(12385.7654,10,15))
# 解除对小数的限制，则会在末尾加0
print('%10f%%,0x%x,0X%02X' %(12385.7654,10,15))

print('%010.2f%%,0x%x,0X%02X' %(12385.7654,10,15))
print('%010f%%,0x%x,0X%02X' %(85.7654,10,15))

print("I am %-5d old" %(20))
print("I am %5d old" %(20))
print("format 的使用")
"""
3、format函数格式化字符串语法--Python鼓励使用
    "{}{xxx}".format(*args,**kwargs) ->str
    args是位置参数，是一个元组
    kwargs是关键字参数，是一个字典
    花括号表示占位符
    {}表示按照顺序匹配位置参数，{n}表示取位置参数索引为n的值
    {xxx}表示在关键字中搜索名称一致的
    {{}}表示打印花括号
"""
#位置参数
print("{}:{}".format('192.168.1.100',8080))
#关键字参数、索引
print("{server}   {1}:{0}".format(8080,'192.168.1.100',server='Web server info'))
#访问元素
print("{0[0]}.{0[1]}".format(('magedu','com')))
#对象属性访问
from collections import namedtuple
Point = namedtuple('Point','x y')
p = Point(4,5)
print("{{{0.x},{0.y}}}".format(p))

# format这样玩
t = ('magedu','com')
print("{}.{}".format(t[0],t[1]))
# 如果没有上面这一步，直接看这个会感觉很怪异
print("{}.{}".format(('magedu','com')[0],('magedu','com')[1]))
# 这个就会报错，因为前面是位置参数，后面就一个参数，所以报错
#print("{}.{}".format(('magedu','com')[0]))
# 但是可以重复使用
print("{0}.{0}".format(('magedu','com')[0]))

a = '{0}*{1}={2:<2}'.format(3,2,3*2)
print(a)
print('{0}*{1}={2:02}'.format(3,2,3*2))
print('{0}*{1}={2:>02}'.format(3,2,3*2))
print('{:^30}'.format('centered'))              #           centered           ：居中，默认两天添加空格
print('{:*^30}'.format('centered'))             #***********centered***********：居中，两边*补齐

print("进位制用法")
print("int:{0:d}; hex:{0:x}; oct:{0:o}; bin:{0:b}".format(42))
print("int:{0:d}; hex:{0:#x}; oct:{0:#o}; bin:{0:#b}".format(42))

octets = [192,168,0,1]
print('{:02X}{:02X}{:02X}{:02X}'.format(*octets))

a,b,c,d = octets
print(a,b,c,d)
e,f,*g = octets
print(e,f,g)

for i in range(6,0,-1):
    print(i)
