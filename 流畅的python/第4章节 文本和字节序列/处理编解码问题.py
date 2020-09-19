# -*- coding: utf-8 -*-
"""
出现与Unicode有关的错误时，首先要明确异常的类型。导致编码问题的是UnicodeEncodeError、
UnicodeDecodeError，还是如SyntaxError的其他错误？解决问题之前必须清楚这一点.
"""

'''4.4.1 处理 UnicodeEncodeError 示例：'''
city = 'São Paulo'
print(city.encode('utf-8'))
print(city.encode('utf-16'))
print(city.encode('iso8859-1'))

# UnicodeEncodeError
# print(city.encode('cp437'))

# 以上编码错误可以通过参数跳过
# error='ignore'处理方式悄无声息地跳过无法编码的字符；这样做通常很是不妥。
print(city.encode('cp437', errors='ignore'))  # b'So Paulo'

# 编码时指定error='replace'，把无法编码的字符替换成'?'；数据损坏了，但是用户知道出了问题。
print(city.encode('cp437', errors='replace'))  # b'S?o Paulo'

# 'xmlcharrefreplace'把无法编码的字符替换成XML实体
print(city.encode('cp437', errors='xmlcharrefreplace'))  # b'S&#227;o Paulo'

'''4.4.2　处理UnicodeDecodeError'''
# 使用错误的编解码器可能出现 鬼符 或抛出 UnicodeDecodeError
# 乱码字符称为鬼符（gremlin）
print('=================')

# 这些字节序列是使用latin1编码的“Montréal”；'\xe9'字节对应“é”
octets = b'Montr\xe9al'

# 可以使用'cp1252'（Windows1252）解码，因为它是latin1的有效超集
print(octets.decode('cp1252'))   # Montréal

# ISO-8859-7用于编码希腊文，因此无法正确解释'\xe9'字节，而且没有抛出错误
print(octets.decode('iso8859_7'))   # Montrιal

# KOI8-R用于编码俄文；这里，'\xe9'表示西里尔字母“И”
print(octets.decode('koi8_r'))  # MontrИal

# 使用'replace'错误处理方式，\xe9替换成了“”（码位是U+FFFD），这是官方指定的REPLACEMENT CHARACTER（替换字符），表示未知字符
print(octets.decode('utf_8', errors='replace')) # Montr�al

'''4.4.3　使用预期之外的编码加载模块时抛出的SyntaxError'''
# Python3默认使用UTF-8编码源码，Python2（从2.5开始）则默认使用ASCII。如果加载的.py模块中
# 包含UTF-8之外的数据，而且没有声明编码，会得到类似下面的消息：
# SyntaxError: Non-UTF-8 code starting with'\xe1'in file ola.py on line
# 1,but no encoding declared;see http://python.org/dev/peps/pep-0263/fordetails

# coding: cp1252

print('Olá,Mundo!')

print('\u2126')
