s1 = "I'm \ta super student."

a1 = s1.split()

'''
字符串分割*
###split系： 将字符串按照分隔符分割成若干字符串，并返回列表；
##partition系： 将字符串按照分隔符分割成两段，返回这两段和分隔符的元组；
#split系：
（1）split(sep=None,maxsplit=-1) -> list of string
    1、从左向右；
    2、sep 指定分割字符串，缺省值的情况下##空白##作为分隔符；
    3、maxsplit 指定分割次数，-1表示遍历整个字符串；
（2）rsplit 与split用法相同，只是方向相反，但输出顺序不变。
（3）splitlines([keepends]) -> list of string
    1、按照行来切分字符串
    2、keepends 指的是是否不留行分隔符，保留参数为True，反之False，默认False
    3、行分隔符包括\n、\r\n、\r等
#partition系：
（1）partition(sep) ->(head,sep,tail)
    1、从左至右，遇到分隔符就把字符串分割成两部分，返回头、分隔符、尾三部分的三元组；如果
    没有找到分隔符，就返回头、2个空元素的三元组；
    2、sep 分割字符串，必须指定。
(2)rpartition(sep) ->(head,sep,tail)
    与partition用法相同，但是从右向左执行，同时结果顺序也会与正向相反
字符串修改：
#replace(old,new[,count]) -> str
    字符串中找到匹配的字符替换为子字符串，返回新字符串；
    count表示替换几次，不指定就是全部替换
字符串查找
#find(sub[,start[,end]]) -> int
    在指定的区间[start[,end]]，从左至右，查找字串sub。找到返回索引，没找到返回-1
#rfind(sub[,start[,end]]) -> int
    在指定的区间[start[,end]]，从右至左，查找字串sub。找到返回索引，没找到返回-1
(# 注意使用find进行判断返回值是否包含自己想要的内容)(可以用count直接当条件判断，但是count遍历整个内容,find找到停止)

##find与index的区别是，find找不到返回-1，index则抛异常，用法一样##

## 直接使用split不能同时使用多个分隔符，但是可以通过re来实现
import re
str1 = "pas,xyz"
print(re.split('[a,]', str1))

'''
s1 = "I'm \ta super student."

a1 = s1.split()

a2 = s1.split('s')

a3 = s1.split('super')

a4 = s1.split('super ')

a5 = s1.split(' ')

a6 = s1.split(' ', maxsplit=2)

a7 = s1.split('\t', maxsplit=2)

print(a1, ':', a2, ':', a3, ':', a4, ':', a5)
print(a6, '##', a7)

a8 = "ab c\n\nde fg\rkl\r\n".splitlines()
print("a8:", a8)

a9 = "ab c\n\nde fg\rkl\r\n".splitlines(True)
print("a9:", a9)

'''
(1)partition(sep) ->(head,sep,tail)
    1、从左至右，遇到分隔符就把字符串分割成两部分，返回头、分隔符、尾三部分的三元组；如果
    没有找到分隔符，就返回头、2个空元素的三元组；
    2、sep 分割字符串，必须指定。
(2)rpartition(sep) ->(head,sep,tail)
    与partition用法相同，但是从右向左执行，同时结果顺序也会与正向相反
'''
s1 = "I'm a super student."

b1 = s1.partition('s')
print("b1:", b1)

b2 = s1.partition('stu')
print("b2:", b2)

# b3 = s1.partition('')
# print("b3:",b3)
print("不指定分隔符，将执行报错，可以什么都不写，默认空白")

b4 = s1.partition('abc')
print("b4:", b4)

# swapcase()交互大小写，即大写变小写，小写变大写
s2 = "abCDefGH"
c = s2.swapcase()
print(c)

'''
字符串修改：
#replace(old,new[,count]) -> str
    字符串中找到匹配的字符替换为子字符串，返回新字符串；
    count表示替换几次，不指定就是全部替换
'''
s3 = 'www.magedu.com'

d1 = s3.replace('w', 'p')
d2 = s3.replace('w', 'p', 2)
print(d1)
print(d2)

'''
字符串查找
#find(sub[,start[,end]]) -> int
    在指定的区间[start[,end]]，从左至右，查找字串sub。找到返回索引，没找到返回-1
#rfind(sub[,start[,end]]) -> int
    在指定的区间[start[,end]]，从又至左，查找字串sub。找到返回索引，没找到返回-1

'''
s = "I am very very lucky"

e1 = s.find('very')
e2 = s.find('very', 6)
e3 = s.find('very', 6, 13)
e4 = s.find('very', 10, -1)  # 表示第11个到最后一个字符之间
e5 = s.rfind('very', 10, -1)  # 表示第11个到最后一个字符之间
print(e1, e2, e3, e4, e5)

str1 = "pas,xyz"
print(str1.split("a"))

# 直接使用split不能同时使用多个分隔符，但是可以通过re来实现
import re

str1 = "pas,xyz"
print(re.split('[a,]', str1))
