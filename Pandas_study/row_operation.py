# -*- coding: utf-8 -*-
import pandas as pd

page_001 = pd.read_excel('./excel/Students-27.xlsx', sheet_name='Page_001')
page_002 = pd.read_excel('./excel/Students-27.xlsx', sheet_name='Page_002')

"""
# 删除空行
# df.dropna(axis=0, how='any')  # axis = [0, 1], how = ['any', 'all']
# 填空值
# df.fillna(value=0)
# 判断是否有空
# np.any(df.isnull()) == True     # 返回值单个结果：bool，不采用np判断，将返回所有单元格bool
"""

# 两种合并和处理index问题,append方式
# 方法一：
# students = page_001.append(page_002, ignore_index=True)

# 方法二：
students = page_001.append(page_002).reset_index(drop=True)


# 追加append
stu = pd.Series({'ID': 41, 'Name': 'Abel', 'Score': 99})
# ignore_index=True 不加报错，Can only append a Series if ignore_index=True or if the Series has a name
students = students.append(stu, ignore_index=True)


# 获取行操作
rows = students.loc[[0, 1]]
# print(rows)

# 直接修改单元格的值
students.at[39, 'Name'] = 'Bailey'
students.at[39, 'Score'] = '120'

# 直接替换整行内容
stu = pd.Series({'ID':38, 'Name': 'kitty', 'Score': 115})
students.iloc[37] = stu


# 在第ID为20和21之间插入一行，danny同学，使用到切片方法
stu = pd.Series({'ID': 101, 'Name': 'Danny', 'Score': 101})
part1 = students[:20]
part2 = students[20:]
students = part1.append(stu, ignore_index=True).append(part2).reset_index(drop=True)
# students = part1.append(stu, ignore_index=True).append(part2, ignore_index=True)


# 删除数据行，索引为0-2的行；参数inplace是为了不生成新的dataframe
students.drop(index=[0, 1, 2], inplace=True)
# 使用切片方式删除
students.drop(index=range(3,10), inplace=True)
students.drop(index=students[1:6].index, inplace=True)

# print(students)

# ===================================
"""按条件处理数据"""
page_001 = pd.read_excel('./excel/Students-27.xlsx', sheet_name='Page_001')
page_002 = pd.read_excel('./excel/Students-27.xlsx', sheet_name='Page_002')

students = page_001.append(page_002).reset_index(drop=True)

# 把一些行名字设为空，进行处理
for i in range(5,15):
    students['Name'].at[i] = ''

missing = students.loc[students['Name'] == '']
students.drop(index=missing.index, inplace=True)
students = students.reset_index(drop=True)

print(students)
print('=====')
print(missing)


