# -*- coding: utf-8 -*-

from lxml import etree
from bs4 import BeautifulSoup

# 使用beautifulsoup4读取时，需要先使用read将文件读取出来，然后再进行使用
with open("./test.xml") as f:
    html = f.read()
soup = BeautifulSoup(html, 'lxml')
print(soup.find("book"))
print('-'*10)
print(soup.find(name="book"))
print('=========================='*10)

html = etree.parse("./test.xml")
print(type(html))

rst = html.xpath('//book[@category="sport"]')
rst = rst[0]

print(type(rst))
print(rst, "===")
print(rst.tag)
print("===================================")

rst = html.xpath('//book')
print(rst)




