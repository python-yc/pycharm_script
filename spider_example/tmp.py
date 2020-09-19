# -*- coding: utf-8 -*-

ss = "xx/sfs/sdsf'45\"123"
# 直接使用字符串分割，不能同时使用多个分隔符
print(ss.split('/'))    # ['xx', 'sfs', 'sdsf\'45"123']

import re
# 使用re可以同时使用多个分隔符分割字符串，优秀
ss = "xx/sfs/sdsf'45\"123"
rg = r'[/\'"]'
print(re.split(rg, ss)) # ['xx', 'sfs', 'sdsf', '45', '123']

def multiSplit(str, sep):
    x = 0
    strlist = str.split(sep[0])
    for i in sep:
        print(i)
        if x==0:
            x += 1
        else:
            # str = str.split(i)
            for j in strlist:
                if i in j:
                    strlist.append(j.split(i))
                else:
                    pass
    return strlist

rst = multiSplit(str=ss, sep="/\"'")
print(rst)

def flatten(items):
    for item in items:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)
        else:
            yield item

print(*rst)
# print(flatten(rst))
# b = flatten(rst)
# for i in range(len(*rst)-1):
#     print(next(b))

from bs4 import BeautifulSoup
soup = BeautifulSoup('<p>Hello</p>', 'lxml')
print(soup.p.string)

print("=" * 50)
html = '<span class="title"><a href="/play/33" sid="33" target="play" title="清晨">清晨</a></span>'

soup = BeautifulSoup(html, 'lxml')
print(soup)
print(soup.string)
print(soup.span.get('class'))
print(soup.span.a.get('href'))
print(soup.span.a.get('sid'))
print(soup.span.a.get('target'))
print(soup.span.a.get('title'))

class Sample:
    def __enter__(self):
        print("In __enter__()")
        return "Foo"
    def __exit__(self, type, value, trace):
        print("In __exit__()")
def get_sample():
    return Sample()
with get_sample() as sample:
    print("sample:", sample)

