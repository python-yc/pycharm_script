# -*- coding: utf-8 -*-

"""
struct模块提供了一些函数，把打包的字节序列转换成不同类型字段组成的元组，还有一些函数用于执行
反向转换，把元组转换成打包的字节序列。struct模块能处理bytes、bytearray和memoryview对象
"""

import struct
import sys

# 结构体的格式：<是小字节序，3s3s是两个3字节序列，HH是两个16位二进制整数
fmt = '<3s3sHH'

try:
    with open('filter.gif', 'rb') as fp:
        # 使用内存中的文件内容创建一个memoryview对象
        img = memoryview(fp.read())
except FileNotFoundError as e:
    print('e:', e)
    sys.exit()

# 使用它的切片再创建一个memoryview对象；这里不会复制字节序列
header = img[:10]
print(bytes(header))

# 拆包memoryview对象，得到一个元组，包含类型、版本、宽度和高度
print(struct.unpack(fmt, header))

# 删除引用，释放memoryview实例所占的内存
del header
del img

# 注意，memoryview对象的切片是一个新memoryview对象，而且不会复制字节序列。
# [本书的技术审校之一LeonardoRochael指出，如果使用mmap模块把图像打开为内存映射文件，那么会复制少量字节
