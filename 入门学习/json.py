# coding: utf-8

"""JSON 的标准：双引号而非单引号！  并且最后一个值末尾不能有逗号"""

# {'name':'Eric', 'age':23,}
# 如果这个代表 json 数据，则有两处错误；1：应该双引号而非单引号；2：末尾有逗号
# 正确的写法： {"name":"Eric", "age":23}

import json

# 此时student是一个dict格式内容，不是json
student={
            "name":"xiaoming",
            "age":18,
            "mobile":"15655984653"
        }

print(type(student))
print(student)

stu_json = json.dumps(student)
print(type(stu_json),"这是json的格式")
print("JSON对象：{0}".format(stu_json))

stu_dict = json.loads(stu_json)
print(type(stu_dict),"这又对json进行解码，变成了python格式")
print(stu_dict)

print("#############################################")

# json文件的读写

import json

data = {"name":"haha","age":12}

with open("C:\\t.json",'w') as f:
    json.dump(data,f)

with open("C:\\t.json",'r') as f:
    d = json.load(f)
    print(d)
