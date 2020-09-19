# -*- coding: utf-8 -*-

import re

hello = u'你好，世界'

pattern = re.compile(r'[u4e00-u9fa5]+')

reg = pattern.findall(hello)
# 匹配失败，未知，以后再说
print(reg)

