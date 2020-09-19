# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup

url = "https://www.hao123.com/"

rsp = request.urlopen(url)

# 使用beautifulsoup就不需要对数据解码了
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

# bs4自动转码
content = soup.prettify()
# print(content)

# print("=head=" * 12)
# print(soup.head)
# print("=meta=" * 12)
# print(soup.meta)
# BeautifulSoup
print(soup.name)
print('-'*50)
# tag
print(soup.link)
print(soup.link.name)
print('-'*50)
print(soup.link.attrs)
print(soup.link.attrs['href'])
print('-'*50)

# NavigableString
print(soup.title.name)
print(soup.title.string)

# print(soup)
