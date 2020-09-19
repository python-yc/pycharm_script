# -*- coding: utf-8 -*-

# 1.2.1 定位
# f.seek(offset,[0,1,2])  # offset：偏移量；0：开头；1：当前位置；2：末尾；
# ####注意：
# 文本文件模式下，不带b，只能写0；
# 如果想写1/2，必须在二进制文件操作模式下使用
# f.tell() # 输出当前位置

with open('a.txt', 'r') as f:
    print(f.tell())
    f.seek(2, 0)
    # f.seek(2, 1)  can't do nonzero cur-relative seeks
    print(f.tell())

print("############")

with open('a.txt', 'rb') as f:
    print(f.tell())
    f.seek(2, 0)
    f.seek(-1, 1)
    print(f.tell())
    f.seek(1, 2)
    print(f.tell())
