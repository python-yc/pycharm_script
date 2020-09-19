# -*- coding: utf-8 -*-
import requests
"""
源自：http://xiaorui.cc/archives/2786
"""

# 对于requests中文乱码解决方法有这么几种.

"""#################方法一、#####################"""
# 由于content是HTTP相应的原始字节串，可以根据headers头部的charset
# 把content decode为unicode，前提不是ISO-8859-1编码.
# r.encoding 如：'gbk' 'utf-8'

url = 'http://xiaorui.cc/archives/2786'
r = requests.get(url)
# print(r.encoding)
# print(r.content.decode(r.encoding))

"""另一种粗暴方式，直接根据chardet的结果来encode成utf-8"""

"""
In [22]: r  = requests.get('http://item.jd.com/1012551875.html')

In [23]: print r.content
KeyboardInterrupt

In [23]: r.apparent_encoding
Out[23]: 'GB2312'

In [24]: r.encoding
Out[24]: 'gbk'

In [25]: r.content.decode(r.encoding).encode('utf-8')
---------------------------------------------------------------------------
UnicodeDecodeError                        Traceback (most recent call last)
<ipython-input-25-918324cdc053> in <module>()
----> 1 r.content.decode(r.apparent_encoding).encode('utf-8')

UnicodeDecodeError: 'gb2312' codec can't decode bytes in position 49882-49883: illegal multibyte sequence

In [27]: r.content.decode(r.apparent_encoding,'replace').encode('utf-8')
"""

# 如果在确定使用text，并已经得知该站的字符集编码时，可以使用 r.encoding = ‘xxx’ 模式，
# 当你指定编码后，requests在text时会根据你设定的字符集编码进行转换
"""
>>> import requests
>>> r = requests.get('https://up.xiaorui.cc')
>>> r.text
>>> r.encoding
'gbk'
>>> r.encoding = 'utf-8'
"""

"""#################方法二、#####################"""
# 大多数网站还是很规范的，如果headers头部没有charset，那么就从html的meta中抽取.
# python requests的utils.py里已经有个完善的从html中获取meta charset的函数. 说白了还是一对的正则表达式.
# =================
# In [32]: requests.utils.get_encodings_from_content(r.content)
# Out[32]: ['gbk']
import re
def get_encodings_from_content(content):
    charset_re = re.compile(r'<meta.*?charset=["\']*(.+?)["\'>]', flags=re.I)
    pragma_re = re.compile(r'<meta.*?content=["\']*;?charset=(.+?)["\'>]', flags=re.I)
    xml_re = re.compile(r'^<\?xml.*?encoding=["\']*(.+?)["\'>]')

    return (charset_re.findall(content) +
            pragma_re.findall(content) +
            xml_re.findall(content))


"""
最后，针对requests中文乱码的问题总结:
1/统一编码，要不都成utf-8, 要不就用unicode做中间码 !
2/国内的站点一般是utf-8、gbk、gb2312  , 当requests的encoding是这些字符集编码后，是可以直接decode成unicode.
3/但当你判断出encoding是 ISO-8859-1 时，可以结合re正则和chardet判断出他的真实编码. 可以把这逻辑封装补丁引入进来
"""
import requests
def monkey_patch():
    prop = requests.models.Response.content
    def content(self):
        _content = prop.fget(self)
        if self.encoding == 'ISO-8859-1':
            encodings = requests.utils.get_encodings_from_content(_content)
            if encodings:
                self.encoding = encodings[0]
            else:
                self.encoding = self.apparent_encoding
            _content = _content.decode(self.encoding, 'replace').encode('utf8', 'replace')
            self._content = _content
        return _content
    requests.models.Response.content = property(content)
# monkey_patch()


prop = requests.models.Response.content
'''Python3.x解决了这编码问题，如果你还是python2.6 2.7，那么还需要用上面的方法解决中文乱码的问题'''
