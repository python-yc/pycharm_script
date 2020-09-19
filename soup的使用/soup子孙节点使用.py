# -*- coding: utf-8 -*-
# 子孙节点
html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.p.children)
for i, child in enumerate(soup.p.children):
    print(i, child)

# 父节点
print('=' * 50)
print(soup.a.parent)
print('=' * 100)
# print(soup.a.parents)   # 需使用循环遍历,知道表达式即可
# print(list(enumerate(soup.a.parents)))

# 同级节点的表达方式
print('Next Sibling', soup.a.next_sibling)  # a的下一个
print('Prev Sibling', soup.a.previous_sibling)  # a的上一个
print('Next Siblings', list(enumerate(soup.a.next_siblings)))
print('Prev Siblings', list(enumerate(soup.a.previous_siblings)))
