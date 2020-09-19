# 页面解析和数据获取
- 结构数据： 先有的结构，再提数据
    - JSON文件
        - JSON Path
        - 转换成Python类型进行操作（json类）
    - XML文件
        - 转换成python类型（xmltodict）
        - XPath、CSS选择器、正则
- 非结构化数据： 先有数据，再谈结构
    - 文本、电话号码、邮箱地址      通常处理此数据使用正则表达式
    - html文件
        - 正则、XPath、CSS选择器
# 正则表达式
- 一套规则，可以在字符串文本中进行搜查替换
- 案例basicuse_re_21_match.py
- 正则常用方法：
    - match：从开始位置开始查找，一次匹配
    - search：从任何位置查找，一次匹配
    - findall：全部匹配，返回列表
    - finditer：全部匹配，返回迭代器
    - split：分割字符串，返回列表
    - sub：替换
    - 案例basicuse_re_22_findxx.py
- 匹配中文
    - 中文unicode范围主要在[u4e00-u9fa5]
    - 案例basicuse_re_23_ch.py
# xml
    - 经典官方文档https://www.w3school.com.cn/xml/index.asp
    - XML（EXtensibleMarkupLanguage）
    - 概念：父节点、子节点、兄弟节点、先辈节点、后辈节点
# Xpath
    - (XML Path Language), 是一门在XML文档中查找信息的语言
    - 经典官方文档https://www.w3school.com.cn/xml/index.asp
    - XPath开发工具
        - 开源的Xpath表达式工具，XMLQuire
        - chrome插件：Xpath Helper
        - Firefox插件：Xpath CHecker
- 常用路径表达式：
    - nodename：选取此节点的所有子节点
    - /：从根节点开始选
    - //：选取元素，而不是考虑元素的具体位置（相对路径）
    - .：当前节点
    - ..：父节点
    - @：选取属性
    
    - 案例：
        - bookstore：选取bookstore下的所有子节点
        - /bookstore：选取根元素
        - bookstore/book：选取bookstore的所有book子元素
        - //book：选取book子元素
        - //@lang：选取名称为lang的所有属性
- 谓语（Predicates）
    - 谓语用来查找某个特定的节点，被放在方括号中
    - /bookstore/book[1]：选取第一个属于bookstore下叫book的元素
    - /bookstore/book[last()]：选取属于bookstore最后一个book的元素
    - /bookstore/book[last()-1]
    - /bookstore/book[last()<3]
    - /bookstore/book[@lang]
    - /bookstore/book[@price < 90]
- 通配符
    - '*'：任何元素节点
    - @*：匹配任何属性节点
    - node()：匹配任何类型的节点
- 选取多个路径
    - //book/title | //book/author ：选取book元素中的title和author元素
    - //title | //price：选取文档中所有的title和price元素

# lxml库
- python的HTML/XML的解析器
- 案例basicuse_lxml_24.py
- 功能：
    - 解析HTML、文件读取
    - 案例basicuse_lxml_25_readhtml.py
    - etree与Xpath结合使用
    - 案例basicuse_lxml_26_etreexpath.py

# CSS选择器 BeautifSoup4
- 安装 pip install bs4/beautifulsoup4(bs4包括后者)
- 几个常用提取信息工具的比较：
    - 正则：很快，不好用，不用安装
    - beautifulsoup：慢，使用简单，安装简单
    - lxml：比较快，使用简单，安装简单
    - 案例basicuse_lxml_27_beautifulsoup.py
- 四大对象
    - Tag、NavigableString、BeautifulSoup、Comment
## Tag
    -对应HTML中的标签
    - 可以通过soup.tag_name
    - 案例basicuse_lxml_28_souptagname.py
    - tag两个重要属性
        - name、attrs    如：soup.name、soup.link.name、soup.link.attrs
## NavigableString
    - 对应内容值
## BeautifulSoup
    - 表示的是一个文档的内容，大部分可以把它当做tag对象
## Comment
    - 特殊类型的NavigableString对象
    - 对其输出，则内容不包括主视符号

### 遍历文档对象
    - contents：tag的子节点以列表的方式给出
    - children：子节点以迭代器形式返回
    - descendants：所有子节点
    - string：节点有内容，就可以使用此函数显示
    - 案例basicuse_lxml_29_iteration.py
### 搜索文档对象
    - find_all(name,attrs, recursive, text, **kwargs)
        - name:按照那个字符串搜索，可以传入的内容为
            - 字符串、正则表达式、列表
        - kwargs：可以用来表示属性
        - text：对应tag的文本值
        - 案例basicuse_lxml_30_findall.py
### css选择器(xpath定位的那一套)
    - 使用soup.select，返回一个列表
    - 通过标签名称：soup.select("tag_name")
    - 通过类名：soup.select(".class")
    - 通过id：soup.select("#name_id")
    - 组合查找：soup.selet("div #input_content")
    - 属性查找：soup.select("img[class='photo']")
    - 获取tag内容：tag.get_text
    - 案例basicuse_lxml_31_css.py



### 验证码校验 ###
- 验证码：防止机器人或者爬虫
- 分类：
    - 简单图片
    - 极验（行为验证）官网www.geetest.com
    - 12306图片选择
    - 语音验证（电话）
    - google验证

- 验证码破解：
    - 通用方法：
        - 下载网页验证码
        - 手动输入验证号码
    - 简单图片
        - 使用图像识别软件或者文字识别软件
        - 可以使用第三方图像验证码破解网站，官网www.chojiying.com
    - 极验
         - 破解比较麻烦
         - 可以模拟鼠标等移动
         - 一直在进化
    - 12306：可以放弃了
    - 语音验证：语音识别

# Tesseract
- 机器视觉领域的基础软件
- OCR：OpticalCharacterRecogniton，光学文字识别
- Tesseract：一个OCR库，有google赞助
- 安装：
    - windows：教程https://www.cnblogs.com/gl1573/p/9876397.html
    - Mac： brew install tesseract
    - Linux：apt-get install tesseract-ocr
    - 安装完成后需要设置环境变量
- 安装完成后还需要pytesseract
    - pip install pytesseract

- 使用方式
    tesseract picture.name filename

- 读取案例
    - basicuse_lxml_32_readverfiedcode.py

## 动态HTML介绍
- JavaScript
- jQuery
- Ajax
- DHTML
- Python采集动态数据
    - 从JavaScript代码入手
    - Python第三方运行JavaScript







