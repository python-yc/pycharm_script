# -*- coding: utf-8 -*-
import pandas as pd
import seaborn as sns

# 颜色深浅来表示数据的大小
color_map = sns.light_palette('green', as_cmap=True)

students = pd.read_excel('./excel/Students-25-26.xlsx')
students.style.background_gradient(color_map, subset=['Test_1', 'Test_2', 'Test_3'])

# 使用数据bar(矩形长度)来表示数据大小
students = pd.read_excel('./excel/Students-25-26.xlsx', index_col='ID')
students.style.bar(color='orange', subset=['Test_1', 'Test_2', 'Test_3'])
