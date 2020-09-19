# -*- coding: utf-8 -*-

"""
字符的具体表述取决于所用的编码。编码是在码位和字节序列之间转换时使用的算法。在UTF-8编码中，
A（U+0041）的码位编码成单个字节\x41，而在UTF-16LE编码中编码成两个字节\x41\x00。再举个
例子，欧元符号（U+20AC）在UTF-8编码中是三个字节——\xe2\x82\xac，而在UTF-16LE中编码成
两个字节：\xac\x20
"""

# 示例：编码与解码

s = 'café'
print(len(s))
b = s.encode('utf8')
print('b:', b)
print(len(b))
print(b.decode('utf8'))

print('==================')
cafe = bytes('café', encoding='utf_8')
print(cafe)

# 各个元素是range(256)内的整数
print(cafe[0])

# bytes对象的切片还是bytes对象，即使是只有一个字节的切片
print(cafe[:1])
print('==================')
cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-1:])
