# -*- coding: utf-8 -*-
import pandas as pd

"""
如果是统一处理的话，加判断处理即可
"""

students = pd.read_excel('./excel/Students-after-study.xlsx', sheet_name='Sheet1')

# 根据实际再进行处理
# print(students)
# 去除Page_001中的空白
# 删除空白行
students.dropna(how='all', inplace=True)

# 删除空白列
students.dropna(axis=1, how='all', inplace=True)

# 重排索引
students = students.reset_index(drop=True)

# 重设列名,可用循环得到内容进行设置
# students.columns = ['ID', 'Name', 'Score']
# 直接将第一行内容设为列标签,使用position定位比较保险，防止表格无0索引
# students.columns = students.loc[0]
students.columns = students.iloc[0]

# 有不确定空行数时，导致数据无列名，重设列名时有第一列与列名重复，删除第一行
students.drop(index=0, inplace=True)

# 重设索引
students = students.reset_index(drop=True)

# 设置已知列为索引
students = students.set_index('ID')

print(students)

# 打印列标签，由于ID被设为索引，因此不会被当成普通列名打印
print(students.columns)
# print(students.shape)

# 而且显示的开头有个0，但是不会保存在excel中

# 保存excel
# students.to_excel('./excel/Students-after-study11.xlsx')
