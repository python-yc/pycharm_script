# -*- coding: utf-8 -*-

# r、r+

# 文件要存在，这个只读不可写
# with open('a.txt', 'r') as f:
#     f.read()


# 可读可写
# 同时执行读写时，会根据指针位置进行插入；即读完后在写，会末尾追加
# 其它使用时尝试一下即可
with open('a.txt', 'r+') as f:
    f.write("qq")
    print(f.read())

with open('a.txt', 'r+') as f:
    f.write("qq")
    print(f.read())


