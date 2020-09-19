# -*- coding: utf-8 -*-
import re
"""
本来呢: ^只匹配字符串的开头，$只匹配字符串结尾，.不匹配换行符.
re.S做的事情是: 让.也匹配换行符
re.M做的事情是: 让^匹配每行的开头，$匹配每行的结尾
re.I表示不区分大小写
"""


a = """sdfkhellolsdlfsdfiooefo:
8778hello98989worldafdsf"""
b = re.findall('hello(.*?)world',a)
c = re.findall('hello(.*?)world',a,re.S)
print ('b is ' , b)
print ('c is ' , c)

print('==========')
a = """sdfkhellolsdlfsdfiooefo:
8778hello98989WOrldafdsf"""
b = re.findall('hello(.*?)world',a, re.I)
c = re.findall('hello(.*?)world',a,re.S | re.I)
print ('b is ' , b)
print ('c is ' , c)

print('====================')

text = """First line.
Second line.
Third line."""

pattern = "^(.*?)$"  # Match anything from the start to end. 非贪婪匹配

# 让^、$只匹配字符串的开头、结尾, .不匹配换行符
ret1 = re.search(pattern, text)
print('ret1:', ret1)

# 让.匹配换行符
ret2 = re.search(pattern, text, re.S)
print('ret2:', ret2)

# 让^、$匹配每行的开头、结尾, 同时让.匹配换行符, 且pattern是非贪婪匹配
ret3 = re.search(pattern, text, re.M | re.S)
print('ret3:', ret3)

# 让^、$匹配每行的开头、结尾, 同时让.匹配换行符, 且pattern是贪婪匹配
ret4 = re.search("^(.*)$", text, re.M | re.S)
print('ret4:', ret4)

# 让^、$匹配每行的开头、结尾, 非贪婪
ret5 = re.findall(pattern, text, re.M)
print('ret5:', ret5)

ret6 = re.search(pattern, text, re.M)
print('ret6:', ret6)

print('======')
print(ret4.groups())
print('----')
print(ret4.group(1))
