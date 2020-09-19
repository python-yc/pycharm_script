# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

"""
# 取a标签的文本的方式
print(soup.a.text)
print(soup.a.string)
print(soup.a.get_text())
"""

# url = "http://www.htqyy.com/top/hot"
#
# # content = requests.get(url).text
# # soup = BeautifulSoup(content, 'lxml')
# # print(soup)
# # 同样这个获取页面的也不打开了
# # ids = soup.select('#musicList > li:nth-child(1) > span.title')
#
# # 只是这样把值取出来，就是一个列表字符串，因此还需要解析成html格式,下面有例子了，这个就不打开了
# # ids = ['<span class="title"><a href="/play/33" sid="33" target="play" title="清晨">清晨</a></span>']
# print(ids)
# print(ids[0])
# # ids = BeautifulSoup(ids[0], 'lxml')
# print(ids[0].text)
# print(ids[0].string)
# print(ids[0].a)
# print(ids[0].a.string)
# print(ids[0].a.get('href')) # /play/33
# print(ids[0].a.get('href').split('/')[2])


print("=" * 50)
html = '<span class="title"><a href="/play/33" sid="33" target="play" title="清晨">清晨</a></span>'

soup = BeautifulSoup(html, 'lxml')
print(soup)
print(soup.a)
# 取a标签的文本的方式
print(soup.a.text)
print(soup.a.string)
print(soup.a.get_text())
print("*"*50)
print(soup.span.get('class'))
print(soup.span.a.get('href'))
# 使用split分割取值
print(soup.span.a.get('href').split('/')[2])
print('=' * 20)
print(soup.span.a.get('sid'))
print(soup.span.a.get('target'))
print(soup.span.a.get('title'))

print('#' * 50)
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story P!!!</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
print(type(soup.title))
# 可以直接通过属性然后获得文本
print(soup.title.string)
print(soup.head)
# 我们发现结果是第一个p节点的内容，后面的几个p节点并没有选到。也就是说，当有多个节点时，
# 这种选择方式只会选择到第一个匹配的节点，其他的后面节点都会忽略
print(soup.p)
print(soup.title)
# 可以利用name获取标签名
print("name:", soup.title.name)
# 每个节点可能有多个属性，比如id和class等，选择这个节点元素后，可以调用attrs获取所有属性
# 也可以使用print(soup.p.get('name'))方式获取
print(soup.p.attrs)
print(soup.p.attrs['name'])
print(soup.p.get('name'))
print(soup.p.get('class'))
print(soup.p.children)  # 是一个列表对象,可以使用循环输出
for i, child in enumerate(soup.p.children):
    print(i, child)
