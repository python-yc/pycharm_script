'''
题目：列表转换为字典。

程序分析：无。
'''
list = [1,2,3]
i = ['a','b','c','d']

x = dict.fromkeys(list,i)

print(x)


dict_list = dict(zip(list,i))
print(dict_list)

for k,v in dict_list.items():
    print(v)

