# -*- coding: utf-8 -*-

"""
像人类语言也有规则和限制一样，只要假定字节流是人类可读的纯文本，就可能通过试探和分析找出编码。
例如，如果b'\x00'字节经常出现，那么可能是16位或32位编码，而不是8位编码方案，因为纯文本中不能包含空字符
"""

'''
统一字符编码侦测包Chardet就是这样工作的，它能识别所支持的30种编码。Chardet是一个Python库，可以在程序中使用，
'''
from chardet import detect

s = 'hello'.encode('utf-8')
print(list(s))
print(s[0])
print(s[0:1])

print('===')
print(s)    # {'encoding': 'UTF-16', 'confidence': 1.0, 'language': ''}

d = detect(s)
print(d)

print(s.decode(d['encoding']))
