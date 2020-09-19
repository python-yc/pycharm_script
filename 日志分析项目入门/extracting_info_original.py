import datetime
a = [1, 2, 3, 4 , 5 , 6]
print(a[:-2])

logline = '''183.60.212.153 - - [19/Feb/2013:10:23:29 +0800] \
"GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-" \
"Mozilla/5.0 (compatible; +http://www.easou.com.serach/spider.html)"'''

def convert_time(timestr):
    fmstr = "%d/%b/%Y:%H:%M:%S %z"
    dt = datetime.datetime.strptime(timestr, fmstr)
    # print(dt)
    return dt

def convert_request(request):
    return dict(zip(('method','url','protocal'),request.split()))

#与logline内容对应，添加别名
names = ['remote','','','datetime',
         'request','status','size','',
         'useragent']
ops = [None,None,None,convert_time,
       convert_request,int,int,None,
       None]

fields = []

flag = False
tmp = ""

for word in logline.split():
    if not flag:
        if (word.startswith('[') or word.startswith('"')):
            tmp = word[1:]
            if word.endswith(']') or word.endswith('"'):
                tmp = word.strip('[]"')
                fields.append(tmp)
            else:
                flag = True
        else:
            fields.append(word)
        continue
    if flag:
        if word.endswith(']') or word.endswith('"'):
            tmp += " " + word[:-1]  #  word.strip(']"')这样去除结尾多余的也可以
            fields.append(tmp)
            tmp = ""
            flag = False
        else:
            tmp += " " + word
        continue
    # lst.append(word)    # []"

# print(fields)
d = {}
for i,field in enumerate(fields):
    key = names[i]
    # print(ops[i],field)   #定位结果不一致时使用了打印过程
    if ops[i]:
        d[key] = ops[i](field)
    else:
        d[key]  = field

print(d)
