#coding=utf-8
#导入相关包
import re

#查找数字
#r表示字符串不转义
p = re.compile(r'\d+')

# 在字符串one12twothree33456four78中进行查找，按照规则p指定的正则进行查找
# 返回None表示没有找到，否则返回match对象
# match 表示起始位置匹配到正确，否则未找到
m = p.match("one12twothree33456four78")

print(m)

print("====================================")
#导入相关包
import re

#查找数字
#r表示字符串不转义
p = re.compile(r'\d+')

#在字符串one12twothree33456four78中进行查找，按照规则p指定的正则进行查找
#返回None表示没有找到，否则返回match对象,3,6表示查找范围，如果范围内不能匹配到以什么开头则表示未找到
############
#####search是在范围内找, 使用compile编译后，然后参数才可以添加起始和结束位置（即，方法内不传pattern）
m = p.serach("one12twothree33456four78",3,6)

m = p.match("one12twothree33456four78",3,6)
n = p.match("one12twothree33456four78",3,36)

print(m)
#这个是查找范围的开始和结束位置
print(m.start(0))
print(m.end(0))
print(n)

print("#########################")

import re
# l 表示忽略掉大小写，不是l是大写的I,表示ignore
# 使用group进行取值，0表示所有，然后1表示第一个。。。，无负值group(-1)
# 并且字符串的前面要匹配的几处不能多打空格，例如此处不能这样写s =r"IL   am really love you"
s =r"IL am really love you"
p = re.compile(r'([a-z]+) ([a-z]+) ([a-z]+)', re.I)

m = p.match(s)
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(3))
'''
result:
<_sre.SRE_Match object; span=(0, 12), match='IL am really'>
IL am really
IL
really
'''


#查找数字
#r表示字符串不转义
p = re.compile(r'\d+')

m = p.search("one12twothree33456four78")

print(m.group())

rst = p.findall("one12twothree33456four78")
print(type(rst))
print(rst)
print(re.search(r'\d+', "one12twothree33456four78").group())

#两个同时满足，然后替换，剩到单个的则保留不变，遇到分隔符如逗号，则不替换
p = re.compile(r'(\w+) (\w+)')
s = "hello 123 hello 456 xiaohong, i love you "
rst = p.sub('Hello world',s)
print(rst)

"""
# 匹配中文
- 大部分中文内容范围是[u4e00-u9fa5]，但不包括全角标点
"""
import re
title = u'世界 你好，hello moto'

p = re.compile(r'[\u4e00-\u9fa5]+')
rst = p.findall(title)

print(rst)

'''
# 贪婪非贪婪
- 贪婪：尽可能多的匹配，(*)表示贪婪匹配
- 非贪婪：找到符合条件的最小内容即可，(?)表示非贪婪
- 正则默认使用贪婪匹配
- 案例re-eg
'''
import re
title = u'<div>name</div><div>age</div>'

p1 = re.compile(r'<div>.*</div>')
p2 = re.compile(r'<div>.*?</div>')

m1 = p1.search(title)
print(m1.group())

m2 = p2.search(title)
print(m2.group())

print('分组案例,使用小括号表示分组：')
# 忽略某个分组
s = 'age:13,name:Tom'
# 不忽略age分组
p1 = re.compile(r'age:(\d+),name:(\w+)')
print(re.findall(p1, s))    #　[('13', 'Tom')]
# 忽略age分组?:
p2 = re.compile(r'age:(?:\d+),name:(\w+)')
print(p2.findall(s))        # ['Tom'] 查找语法与上面一个都可以

# 自定义名称分组
ret = re.search('(?P<id>.+\d{3})/(?P<name>\w{3})','www122/ooo')
print(ret.group('id'))  # www12
print(ret.group('name'))    # ooo
print(ret.group(1))  # www12

'''
括号() 的分组在正则匹配是可以引用的，那么如果这种() 非常多，都写 \1 \2 \3 肯定不是很方便，那么下面有一种命名的编写方式。

分组别名引用：(?P<name>) (?P=name)

字符	        功能
(?P<name>)	    分组起别名
(?P=name)	    引用别名为name分组匹配到的字符串
 
 特别适合于html中
'''
s = 'hello blue go go hello'
p = re.compile(r'\b(?P<my_group1>\w+)\b\s+(?P=my_group1)\b')
print(re.findall(p, s))     # ['go']

# 向后引用
# 所谓后向引用，就是对前面出现过的分组再一次引用，使用默认的分组名称进行后向引用：\1,\2,\3...（注：从1开始）
# 匹配字符串中连续出现的两个相同的单词
s = 'hello blue blue blue go go hello'
p = re.compile(r'\b(\w+)\b\s+\1\b')  # 这里的'\1'就对应前面的(\w+)
print(re.findall(p, s)) # ['blue', 'go']

# 嵌套分组
s  = '2017-07-10 20:00'
# 从结果看出，分组的序号是以左小括号(从左到右的顺序为准的
p = re.compile(r'(((\d{4})-\d{2})-\d{2}) (\d{2}):(\d{2})')
print(re.findall(p, s)) # [('2017-07-10', '2017-07', '2017', '20', '00')]
