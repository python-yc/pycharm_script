# -*- coding: utf-8 -*-

"""
如果打开文件是为了写入，但是没有指定编码参数，会使用区域设置中的默认编码，而且使用那个编码也能
正确读取文件。但是，如果脚本要生成文件，而字节的内容取决于平台或同一平台中的区域设置，那么就可
能导致兼容问题.

一定要注意对文件处理时加上编码格式，提高兼容性
"""

'''
除非想判断编码，否则不要在二进制模式中打开文本文件；即便如此，也应该使用Chardet，而不是重
新发明轮子（参见4.4.4 节）。常规代码只应该使用二进制模式打开二进制文件，如光栅图像
'''

fp = open('cafe.txt', 'w', encoding='utf_8')
# 默认情况下，open函数采用文本模式，返回一个TextIOWrapper 对象
print("fp: %s" % fp)
fp.write('café')
fp.close()

import os

print('======')
print(os.stat('cafe.txt').st_size)
fp2 = open('cafe.txt')
print('fp2: %s' % fp2)
print(fp2.read())
fp2.close()
print(fp2.encoding)
print('======')

fp3 = open('cafe.txt', encoding='utf_8')
print('fp3: {}'.format(fp3))
print(fp3.read())
fp3.close()

# 'rb'标志指明在二进制模式中读取文件
# 返回的是BufferedReader对象，而不是TextIOWrapper对象
fp4 = open('cafe.txt', 'rb')
print("fp4: %s" % fp4)
print(fp4.read())
fp4.close()
