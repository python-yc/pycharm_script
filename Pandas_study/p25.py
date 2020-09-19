# -*- coding: utf-8 -*-
"""
pycharm无法显示条件格式的情况，jupyter是可以的，这里只写代码
"""
import pandas as pd

def low_score_red(s):
    color = 'red' if s < 20 else 'black'
    return f'color:{color}'



def highest_score_green(col):
    return ['background-color:lime' if s == col.max()
            else 'backgroud-color:white' for s in col]

students = pd.read_excel('./excel/Students-25-26.xlsx')
# print(students)

students.style.applymap(low_score_red, subset=['Test_1', 'Test_2', 'Test_3'])
students.style.applymap(low_score_red, subset=['Test_1', 'Test_2', 'Test_3'])\
    .apply(highest_score_green, subset=['Test_1', 'Test_2', 'Test_3'])
