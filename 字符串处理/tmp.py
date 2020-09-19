import datetime
import re

# logline = '''183.60.212.153 - - [19/Feb/2013:10:23:29 +0800] \
# "GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-" \
# "Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com.serach/spider.html)"'''
#
# def extract(line):
#     pattern = '''(?P<remote>[\d\.]{7,}) - - \[(?P<datetime>[^\[\]]+)\] "(?P<requeset>[^"]+)" (?P<status>\d+) (?P<size>\d+) "([^"]+)" "(?P<useragent>[^"]+)"'''
#     regex = re.compile(pattern)
#     matcher = regex.match(line)
#     return matcher.groupdict()
#
#
# print(extract(logline))

lst = {
    "name": "xiaoming",
    "phone": "1565598",
    "sex": "man",
    "age": "18",
    "height": "173"
}

def convert_height(height):
    height = float(height)
    ht = height / 100
    return ht

ops = {
    "age": int,
    "height": convert_height
}

d = {}
for k, v in lst.items():
    if ops.get(k):
        d[k] = ops.get(k)(v)
    else:
        d[k] = v
    #这个表达式的意思：如果在ops字典中找不到对应lst中的key，
    # 则使用lambda表达式处理传进来的v值，与上面判断等效
    # d[k] = ops.get(k, lambda x:x)(v)
    print(d[k])

print(d)
# print(ops.get("age",))

func = lambda x:x
print(func("xiao ming"))

