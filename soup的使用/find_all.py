# -*- coding: utf-8 -*-

"""
# 取a标签的文本的方式
print(soup.a.text)
print(soup.a.string)
print(soup.a.get_text())

find_all() 
find_all，顾名思义，就是查询所有符合条件的元素。给它传入一些属性或文本，
就可以得到符合条件的元素，它的功能十分强大。

find_parents()和find_parent()：前者返回所有祖先节点，后者返回直接父节点。 
find_next_siblings()和find_next_sibling()：前者返回后面所有的兄弟节点，后者返回后面第一个兄弟节点。 
find_previous_siblings()和find_previous_sibling()：前者返回前面所有的兄弟节点，后者返回前面第一个兄弟节点。 
find_all_next()和find_next()：前者返回  节点后  所有符合条件的节点，后者返回第一个符合条件的节点。 
find_all_previous()和find_previous()：前者返回  节点前  所有符合条件的节点，后者返回第一个符合条件的节点

此处是以find_all()为例
"""
# (1)name
# 我们可以根据节点名来查询元素，示例如下：
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(name='ul'))
# 同时使用多个元素精确定位
print(soup.find_all(name='ul', attrs={"class":"list","id": "list-1"}))
print('======')
print(type(soup.find_all(name='ul')[0]))

# 获取所有ul标签内容，然后筛选出li标签，在对li标签循环出值
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)

# (2)attrs
# 除了根据节点名查询，我们也可以传入一些属性来查询，示例如下：
# 这里直接传入id=’list-1’，就可以查询id为list-1的节点元素了。而对于class来说，由于class在Python里是一个关键字，
# 所以后面需要加一个下划线，即class_=’element’，返回的结果依然还是Tag组成的列表。
print("attrs===" * 50)
print(soup.find_all(attrs={'id': 'list-1'}))
print("======")
print(soup.find_all(id="list-1"))
print("here===========",soup.find_all(class_="list"),"======here")
print("===")
rsp = soup.find_all(attrs={'name': 'elements'})
print(type(rsp))
print(rsp)

for index, content in enumerate(rsp):
    print(index,content)
print("###")
print(rsp[0].li)
print(rsp[0].find_all('li'))
print("可以从列表中下标拿取", rsp[0].find_all('li')[1])
print("可以从列表中下标拿取", rsp[0].find_all('li')[1].string)
print(type(rsp[0].find_all('li')))
print("gogo" * 10)
print(rsp,"=======look")

# (3)text
# text参数可用来匹配节点的文本，传入的形式可以是字符串，可以是正则表达式对象，示例如下：
# 这里有两个a节点，其内部包含文本信息。这里在find_all()方法中传入text参数，该参数为正则表达式对象，
# 结果返回所有匹配正则表达式的节点文本组成的列表
import re
html='''
<div class="panel">
    <div class="panel-body">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link, too</a>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(text=re.compile('link')))
print(soup.find_all(text=re.compile('link'), name="a"))

# 除了find_all()方法，还有find()方法，只不过后者返回的是单个元素，也就是第一个匹配的元素


