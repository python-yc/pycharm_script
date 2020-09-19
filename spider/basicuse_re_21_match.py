# -*- coding: utf-8 -*-

import re

s = r'([a-z]+) ([a-z]+)'
pattern = re.compile(s, re.I)

reg = pattern.match("Hello world wide web")

s = reg.group(0)
print(s)

a = reg.span(0) # 返回匹配成功的 整个字串的跨度
print(a)

s = reg.group(1)
print(s)

a = reg.span(1)
print(a)


