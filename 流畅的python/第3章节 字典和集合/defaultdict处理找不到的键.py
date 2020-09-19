# -*- coding: utf-8 -*-
"""
有时候为了方便起见，就算某个键在映射里不存在，我们也希望在通过这个键读取值的时候能得到一个
默认值。有两个途径能帮我们达到这个目的，一个是通过defaultdict这个类型而不是普通的dict，
另一个是给自己定义一个dict的子类，然后在子类中实现__missing__方法。下面将介绍这两种方法
"""

import sys, re
import collections

word_re = re.compile(r'\w+')

index = collections.defaultdict(list)
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in word_re.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location)

# 以字母顺序打印出结果
for word in sorted(index, key=str.upper):
    print(word, index[word])
