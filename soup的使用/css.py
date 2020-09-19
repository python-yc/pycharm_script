# -*- coding: utf-8 -*-

"""
Beautiful Soup还提供了另外一种选择器，那就是CSS选择器。如果对Web开发熟悉的话，那么对CSS选择器肯定也不陌生。如果不熟悉的话，可以参考http://www.w3school.com.cn/cssref/css_selectors.asp了解。

使用CSS选择器时，只需要调用select()方法，传入相应的CSS选择器即可，示例如下：
"""
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
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
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))

rsp = soup.select('ul li')
print(rsp[1])
print('====')
for i in rsp:
    print(i)

'''
这里我们用了3次CSS选择器，返回的结果均是符合CSS选择器的节点组成的列表。例如，select(‘ul li’)则是选择所有ul节点下面的所有li节点，结果便是所有的li节点组成的列表。

最后一句打印输出了列表中元素的类型。可以看到，类型依然是Tag类型。

嵌套选择 
select()方法同样支持嵌套选择。例如，先选择所有ul节点，再遍历每个ul节点，选择其li节点，样例如下：
'''
for ul in soup.select('ul'):
    print(ul.select('li'))

"""
获取属性 
我们知道节点类型是Tag类型，所以获取属性还可以用原来的方法。仍然是上面的HTML文本，这里尝试获取每个ul节点的id属性：
"""
for ul in soup.select('ul'):
    print("for 循环值====")
    print(ul)
    print(ul['id'])
    print(ul.attrs['id'])

"""
获取文本 
要获取文本，当然也可以用前面所讲的string属性。此外，还有一个方法，那就是get_text()，示例如下
直接使用text也可以
"""
i = 1
for li in soup.select('li'):
    print("取标签文本的三种方式，第 {} 次循环结果如下：".format(i))
    i += 1
    print('Get Text:', li.get_text())
    print('String:', li.string)
    print('Text:', li.text)


