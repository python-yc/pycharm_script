# -*- coding: utf-8 -*-
import pandas as pd

students = pd.read_excel('./excel/Students-019.xlsx', index_col='ID')

temp = students[['Test_1', 'Test_2', 'Test_3']]

# 从左到右进行统计；默认为axis=0，从上到下
# result = temp.sum()
row_sum = temp.sum(axis=1)
row_mean = temp.mean(axis=1)
students['Total'] = row_sum
students['Average'] = row_mean

col_mean = students[['Test_1', 'Test_2', 'Test_3', 'Total', 'Average']].mean()

# print(col_mean)
# 将新增的一行命名
col_mean['Name'] = 'Summary'

# 使用append方法，这样默认追加到dataframe的末行
students = students.append(col_mean, ignore_index=True)

print(students)
