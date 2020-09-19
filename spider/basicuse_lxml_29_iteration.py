# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup

url = "https://www.hao123.com/"

rsp = request.urlopen(url)

# 使用beautifulsoup就不需要对数据解码了
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

print(soup.name)

for node in soup.head.contents:
    if node.name == "meta":
        print("##" * 12)
        print(node)
    if node.name == "title":
        print("==" * 12)
        print(node.string)

