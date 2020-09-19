# -*- coding: utf-8 -*-
import pandas as pd

students = pd.read_excel('./excel/Students_Duplicates-20.xlsx')

# 多列去重
# students.drop_duplicates(subset=['Name', 'ID'], inplace=True)

# 此处为单列;keep重复值保留前面的还是后面的，默认first
# # students.drop_duplicates(subset='Name', inplace=True, keep='first')
# students.drop_duplicates(subset=['Name'], inplace=True, keep='last')
#
# print(students)

"""上面去除重复内容的代码，后面为找出重复的内容"""

dupe = students.duplicated(subset='Name')
print(dupe)
print(type(dupe))

print("\ndupe[0]: ", end=' ')
print(dupe[0])
print()

# 再进行过滤
# dupe = dupe[dupe == True]

# 因为dupe本身就是bool，所以可以简写为
dupe = dupe[dupe]

# 获取过滤的重复值的索引
dupe_inx = dupe.index       # Int64Index([20, 21, 22, 23, 24], dtype='int64')

# 定位重复数据
data = students.loc[dupe_inx]
print(data)
