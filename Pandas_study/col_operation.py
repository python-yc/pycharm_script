# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

"""
# 删除空列
# df.dropna(axis=1, how='any')  # axis = [0, 1], how = ['any', 'all']
# 填空值
# df.fillna(value=0)
# 判断是否有空
# np.any(df.isnull()) == True     # 返回值单个结果：bool，不采用np判断，将返回所有单元格bool
"""

page_001 = pd.read_excel('./excel/Students-27.xlsx', sheet_name='Page_001')
page_002 = pd.read_excel('./excel/Students-27.xlsx', sheet_name='Page_002')


# 行方向连接，左右连接
students = pd.concat([page_001, page_002], axis=1)

# 列方向连接，上下连接
students = pd.concat([page_001, page_002]).reset_index(drop=True)
# 末尾添加一列,默认会给你按等长度复制出所有行的值
# students['Age'] = 25

# 当然你也可以填写等长度的值
students['Age'] = np.arange(0, len(students))

# 删除列
# students = students.drop(columns=['Age', 'Score'])
students = students.drop(columns=['Score'])

# 插入列
students.insert(1, column='Foo', value=np.repeat('foo', len(students)))

# 修改列名
students.rename(columns={'Foo': 'FOO', 'Name': 'NAME'}, inplace=True)

# 重新设置索引
# students = students.set_index('ID')

# 去空值操作
# 制造空值，首先需要转换字符类型
students['ID'] = students['ID'].astype(float)
for i in range(5,15):
    students['ID'].at[i] = np.nan

# row操作中有说到去空值，那种方式是采用定位到空值的inde，然后进行drop；这个更简单
students.dropna(inplace=True)

print(students)
