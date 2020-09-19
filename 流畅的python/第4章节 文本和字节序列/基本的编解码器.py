# -*- coding: utf-8 -*-

"""
Python自带了超过100种编解码器（codec,encoder/decoder），用于在文本和字节之间相互转换。
每个编解码器都有一个名称，如'utf_8'，而且经常有几个别名，如'utf8'、'utf-8'和'U8'。这些
名称可以传给open()、str.encode()、bytes.decode()等函数的encoding参数。
"""

# 示例： 使用3个编解码器编码字符串“ElNiño”，得到的字节序列差异很大

for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'ElNiño'.encode(codec), sep='\t')

b = b'\xff\xfeE\x00l\x00N\x00i\x00\xf1\x00o\x00'
print(b.decode('utf_16'))
