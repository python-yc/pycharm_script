# -*- coding: utf-8 -*-

# 笔记中写直接open，这里只用with方式；

# 只读模式；文件必须存在，否则报错
# f = open('a.txt', 'r') 或以下写法
with open('a.txt', 'r') as f:
    print(f.read())
# 只写，不追加
with open('a.txt', 'w') as f:
    f.write('abc')
# 只写，追加
with open('a.txt', 'a') as f:
    f.write('abc')
    f.seek(2)
    f.seek(2, 0)
    print(f.tell())

# 直接跳转查看函数的具体使用可能看不到，使用帮助文档可以查看
# with open('a.txt', 'r') as f:
#     print(help(f.seek))
