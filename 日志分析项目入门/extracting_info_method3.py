import datetime
import re
a = [1, 2, 3, 4 , 5 , 6]
print(a[:-2])

logline = '''183.60.212.153 - - [19/Feb/2013:10:23:29 +0800] \
"GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-" \
"Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com.serach/spider.html)"'''

def extract(line):
    pattern = '''(?P<remote>[\d\.]{7,}) - - \[(?P<datetime>[^\[\]]+)\] "(?P<requeset>[^"]+)" (?P<status>\d+) (?P<size>\d+) "([^"]+)" "(?P<useragent>[^"]+)"'''
    regex = re.compile(pattern)
    matcher = regex.match(line)
    return matcher.groupdict()

"""
这样可以把上面的两个函数简化进这个ops字典中，看着更清爽
ops = {
    'datetime':lambda timestr: datetime.datetime.strptime(timestr, "%d/%b/%Y:%H:%M:%S %z"),
    'status':int,
    'size':int,
    'request':lambda request:dict(zip(('method','url','protocal'),request.split()))
}
"""

def convert_time(timestr):
    fmstr = "%d/%b/%Y:%H:%M:%S %z"
    dt = datetime.datetime.strptime(timestr, fmstr)
    # print(dt)
    return dt

def convert_request(request:str):
    return dict(zip(('method','url','protocal'),request.split()))

ops = {
    'datetime':convert_time,
    'status':int,
    'size':int,
    'request':convert_request
}


# d = {}
# for k, v in extract(logline).items():
#     d[k] = ops.get(k, lambda x:x)(v)
#这句等于上面三行
# d = {k:ops.get(k, lambda x:x)(v) for k, v in extract(logline).items()}

def load(path:str):
    with open(path) as f:
        for line in f:
            d = extract(line)
            if d:
                yield d
            else:
                #  TODO 不合格数据有多少（TODO表示以后要做的事）
                continue


