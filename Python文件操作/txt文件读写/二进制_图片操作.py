# -*- coding: utf-8 -*-

# 当前路径图片处理(picture.png)
"""
这两个with也可以直接合并在一起使用
"""
with open('picture.png', 'rb') as f:

    # 读取并打印
    first_content = f.read()
    print(first_content)

# 写入到另一个文件，如target_file.png
# 1、打开目标文件；2、然后将前面一个文件中的一般写入到目标文件
with open('target_file.png', 'wb') as f:
    # 这样写会正常完全写入到目标文件
    # second_content = first_content

    # 取一部分写入，图片也就会写入一部分，从pycharm中就看不到，
    # 可以进入文件路径然后查看图片是有内容的
    second_content = first_content[:len(first_content)//2]
    f.write(second_content)


