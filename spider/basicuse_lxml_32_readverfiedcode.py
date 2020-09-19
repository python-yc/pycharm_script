# -*- coding: utf-8 -*-

import pytesseract as pt
from PIL import Image

'''
暂时还未安装相应模块
先记录一下学习代码
'''

# 生成图片实例
image = Image.open('C:/1.jpeg')

# 调用pytesseract把图片转换成文字
# 返回结果就是转换后的结果
text = pt.image_to_string(image)
print(text)

