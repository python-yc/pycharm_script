# -*- coding: utf-8 -*-
"""
当字典d[k]不能找到正确的键的时候，Python会抛出异常，这个行为符合Python所信奉的“快速失败”哲学。
也许每个Python程序员都知道可以用d.get(k,default)来代替d[k]，给找不到的键一个默认的返回值
（这比处理KeyError要方便不少）。但是要更新某个键对应的值的时候，不管使用__getitem__还是get
都会不自然，而且效率低。就像示例3-2中的还没有经过优化的代码所显示的那样，dict.get并不是处理找
不到的键的最好方法.
"""

import sys
import re

if len(sys.argv) == 1:
    print(sys.argv)
    sys.exit()

word_re = re.compile(r'\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in word_re.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            """其实这是一种很不好的实现, 这样写只是为了证明论点"""
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences

"""以字母顺序打印出结果"""
for word in sorted(index, key=str.upper):
    print(word, index[word])


# 使用setdefault处理
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in word_re.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            """其实这是一种很不好的实现, 这样写只是为了证明论点"""
            # occurrences = index.get(word, [])
            # occurrences.append(location)
            # index[word] = occurrences
            index.setdefault(word, []).append(location)

"""以字母顺序打印出结果"""
for word in sorted(index, key=str.upper):
    print(word, index[word])
