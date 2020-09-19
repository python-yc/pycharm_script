# -*- coding: utf-8 -*-
"""
有一些后缀名不同的文件放在一起，让你将相同后缀文件放在同一个同名目录中；
创建一个同名目录
"""
import os
import shutil

# 0、获取所有的文件名称列表
file_list = os.listdir('files')

# 1、遍历所有文件名称
for file_name in file_list:
    # print(file_name)

    # 2、分解文件的后缀名
    # 2.1、获取最后一个 . 的索引位置 xx.oo.txt
    index = file_name.rfind(".")

    # 容错处理，如果不是文件继续遍历
    if index == -1:
        continue

    # 2.2 根据索引位置，当做起始位置，来截取后续的所有字符串内容
    extension = file_name[index+1:]     # +1会去掉 .
    # print(extension)

    # 3、查看一下是否存在同名目录
    if not os.path.exists("files/" + extension):
        # 4、如果不存在这样的目录 -》 直接创建一个同名目录
        # 5、目录存在 -》 移动过去
        os.mkdir("files/" + extension)

    shutil.move("files/" + file_name, "files/" + extension)

