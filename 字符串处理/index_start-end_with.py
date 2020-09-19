# 字符串查找
s = "I am very very very lucky"

for i in range(len(s)):
    print(str(i)+s[i],end=" ")

'''
注意负索引的使用
##find与inde的区别是，find找不到返回-1，index则抛异常，用法一样
1、index(sub[,start[,end]]) -> int
    在指定的区间[start,end)，从左至右查找子串sub，找到返回索引，没找到抛异常ValueError
    注意右边是开区间
   rindex(sub[,start[,end]]) -> int
    在指定的区间[start,end)，从右至左查找子串sub，找到返回索引，没找到抛异常ValueError
2、count(sub[,start,[,end]) -> int
    在指定的区间[start,end)，从左至右统计子串sub出现的次数
3、startswith(prefix[,start[,end]]) -> bool
    在指定的区间[start,end)，字符串是否是prefix开头
   endswith(suffix[,start[,end]]) -> bool
    在指定的区间[start,end)，字符串是否是suffix结尾
字符串判断is系列
比较常用：
    isidentifier()是不是字母和下划线开头，其他都是字母、数字、下划线
    islower()是否都是小写
    isupper()是否都是大写
不常用：（正则比较方便）
    isalnum() -> bool是否是字母和数字组合
    isalpha() 是否是字母
    isdecimal()是否只包含十进制数字
    isdigit()是否全部数字（0~9）
    isspace()是否只包含空白符

'''
print()
a1 = s.index("very")
a2 = s.index("very",5)
# 这个由于右边是开区间，这个第13个不包括，抛出异常
#a3 = s.index("very",6,13)
a3 = s.index("very",6,14)
a4 = s.rindex("very",10)
print(a1,a2,a3,a4,)
a5 = s.rindex("very",-10,-1)
print(a5)

'''
startswith(prefix[,start[,end]]) -> bool
    在指定的区间[start,end)，字符串是否是prefix开头
endswith(suffix[,start[,end]]) -> bool
    在指定的区间[start,end)，字符串是否是suffix结尾
'''
s = "I am very very very lucky"

print("#############")
b1 = s.startswith('very')
b11 = s.startswith('I')
b2 = s.startswith('very',5)
b3 = s.startswith('very',5,9)
print(b1,b11,b2,b3)

b4 = s.endswith('very',5,9)
b5 = s.endswith('lucky',5,9)
b6 = s.endswith('lucky',5)
b7 = s.endswith('lucky',5,-1)
print(b4,b5,b6,b7)

a = [1,2,3]
b = [i for i in a]
print(b)

name = ['a','b','c','d']
age = [20,21,22]
info = dict(zip(name,age))
print(info)

for i in range(100,len(a)+100):
    print(i)

# 不定义a为字典，直接从下面第二行向下写，会报错，不是shelve那样的，shelve是已有的一种持久化工具
a = {}
a['one'] = 1
a['two'] = 2
print(a)
