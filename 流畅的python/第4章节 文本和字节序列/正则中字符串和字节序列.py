# -*- coding: utf-8 -*-
"""
标准库中的一些函数能接受字符串或字节序列为参数，然后根据类型展 现不同的行为。
re 和 os 模块中就有这样的函数
"""
import re
# 前两个正则表达式是字符串类型。
re_numbers_str = re.compile(r'\d+')
re_words_str = re.compile(r'\w+')

# 后两个正则表达式是字节序列类型
re_numbers_bytes = re.compile(rb'\d+')
re_words_bytes = re.compile(rb'\w+')

text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef "
            "as 1729 = 1³ + 12³ = 9³ + 10³.")

# 字节序列只能用字节序列正则表达式搜索。
text_bytes = text_str.encode('utf_8')

print('Text', repr(text_str), sep='\n ')
print('Numbers')
print(' str :', re_numbers_str.findall(text_str))
print(' bytes:', re_numbers_bytes.findall(text_bytes))

print('Words')
print(' str :', re_words_str.findall(text_str))
print(' bytes:', re_words_bytes.findall(text_bytes))
