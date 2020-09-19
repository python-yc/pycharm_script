# -*- coding: utf-8 -*-
import pandas as pd


'''一、assert 方式校验'''
# def score_validation(row):
#     try:
#         assert 0 <= row.Score <= 100
#     except:
#         print(f'#{row.ID}\tstudent {row.Name} has an invalid score {row.Score}.')

'''二、if 判断校验'''
def score_validation(row):
    if not 0 <= row.Score <= 100:
        print(f'#{row.ID}\tstudent {row.Name} has an invalid score {row.Score}.')
        # print(row)



# 一般默认不要设置列索引，让其自动生成索引
students = pd.read_excel('./excel/Students-17.xlsx')

# print(students)
students.apply(score_validation, axis=1)
print(students.head(3))
print(students[0:1])
