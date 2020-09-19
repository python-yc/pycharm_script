# -*- coding: utf-8 -*-
import pandas as pd

employees = pd.read_excel('./excel/Employees-018.xlsx', index_col='ID')

# 添加一个参数，直接将一个列表分成两列，expand=True
df = employees['Full Name'].str.split(expand=True)

# print(df)
employees['First Name'] = df[0]
employees['Last Name'] = df[1]
print(employees)
# employees.to_excel('./excel/Employees-01888.xlsx')
