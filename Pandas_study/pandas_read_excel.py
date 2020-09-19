# -*- coding: utf-8 -*-
# 虽然没导入，但是要安装xlrd库
import pandas as pd, numpy as np

# 读取Excel，如果表格前面有多余行，使用skiprows跳过，如果第一行有脏数据，header=1跳过
people = pd.read_excel('./excel/people.xlsx', skiprows=None, header=0)
print(people.shape)
# 如果没有columns的名字，主动设定一个即可
# people.columns = ['ID', 'Type', 'Title', 'FirstName', 'MiddleName', 'LastName']
print(people.columns)
print(people.head())
# print(people)     # 打印整个sheet
# 读取后进行保存
# people.to_excel('xxx.xlsx')
