# -*- coding: utf-8 -*-

from lxml import etree

'''
用lxml来解析HTML代码
'''

text = '''
<div>
    <url>
        <li class="item-0"> <a href="0.html"> first item</a> </li>
        <li class="item-1"> <a href="0.html"> first item</a> </li>
        <li class="item-2"> <a href="0.html"> first item</a> </li>
        <li class="item-3"> <a href="0.html"> first item</a> </li>
        <li class="item-4"> <a href="0.html"> first item</a> </li>
        <li class="item-5"> <a href="0.html"> first item</a> </li>
    </url>
</div>

'''

# 利用etree.HTML把字符串解析成HTML文档
html = etree.HTML(text)
s = etree.tostring(html)
print(s)


