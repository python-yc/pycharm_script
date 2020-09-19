# -*- coding: utf-8 -*-
from urllib import request, parse
import json

"""
任务要求和内容与simple_urllib_5_post1.py一样
不同：使用request.Request类来实现

利用parse模块模拟post请求
分析百度词典，步骤如下：
1、打开F12
2、尝试输入girl，发现没敲一个字符都有请求
3、请求地址是 https://fanyi.baidu.com/sug
4、利用NetWork-All-Headers查看，发现FormData的值是kw:girl
5、检查返回内容格式，格式为json给事内容==》需要用到json包
"""


'''
post方法获取网页
大致流程：
1、利用data构造内容，然后urlopen打开
2、返回一个json格式的结果
3、结果就应该是girl的释义（此处只是练习，固定参数，方式称为硬编码）
'''

baseurl = 'https://fanyi.baidu.com/sug'

# 存放用来授权form的数据，一定是###dict###格式
data = {
    # girl是翻译输入的内容，应该是由用户输入，此处使用硬编码
    "kw": "girl"
}

# 需要使用parse模块对data进行编码
# POST data should be bytes or an iterable of bytes. It cannot be of type str
# data = parse.urlencode(data)

# 由于data数据需要是bytes或者iterable bytes
# 原本urlencode编码后是个字符串，在进行编码成bytes格式
data = parse.urlencode(data).encode('utf-8')
print(type(data))

# 我们需要构造一个请求头，请求头部应该至少包含传入的数据的长度
# request要求传入的请求头是一个dict格式

# simple_urllib_5_post1.py未使用到header，此代码会使用
headers = {
    'Content-Length': len(data)
}

# 构造一个Request实例
req = request.Request(url=baseurl, data=data, headers=headers)

# 有了data 、 url 、 headers 就可以发出请求了
# 因为已经构造了一个Request的请求实例，则所有的请求信息都可以封装在Request实例中
# 因此此处只需要把Request实例传进来打开即可,其他信息无需改动，结果与simple_urllib_5_post1.py结果一致
rsp = request.urlopen(req)

json_data = rsp.read().decode('utf-8') # 只这样解码不能解决,此处不解码是bytes类型，应需要str
print(type(json_data))

# json格式，使用json进行解码,同时还是需要先使用decode解码
# 把json字符串格式转化成python字典
json_data = json.loads(json_data)
print(type(json_data))

print(json_data)

# 把里面的值取出来
'''
{'data': [{'k': 'girl', 'v': 'n. 女孩; 姑娘; 女儿; 年轻女子; 女郎;'}, 
{'k': 'girls', 'v': 'n. 女孩; 姑娘; 女儿; 年轻女子; 女郎;  girl的复数;'}, 
{'k': 'girlfriend', 'v': 'n. 女朋友; 女情人; (女子的)女伴，女友;'}, 
{'k': 'girl friend', 'v': ' 未婚妻; 女性朋友;'}, 
{'k': "Girls' Generation", 'v': ' 少女时代（韩国SM娱乐有限公司于2007年推出的九名女子少女组合）;'}],
 'errno': 0}
'''


for item in json_data['data']:
    print(item['k'],"---",item['v'])

# 上面也是直接取字典内的值
print("==========取data值列表内的字典============")
# for item,v in json_data['data'][0].items():
#     print(item,"###",v)

