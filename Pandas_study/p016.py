# -*- coding: utf-8 -*-
import pandas as pd

students = pd.read_excel('./excel/Student_Score-16.xlsx', sheet_name='Students')
scores = pd.read_excel('./excel/Student_Score-16.xlsx', sheet_name='Scores')

# print(students)
# print(scores)

'''merge 进行联立'''
# 将上面两个表联合起来,此以students表为主、并且以ID列 进行合并
# 如果一个为ID，另一个不叫ID，这是可以使用right_on/left_on；此参数不加，默认也会自动找
# how不加时，默认将对不上的数据丢弃；空数据为NaN，调用fillna函数将其变为0
# 另外一个注意项，如果ID被设为索引项，ID也就从列中"消失"了，此时再merge就会报错；这是就必须使用on、left_on/right_on
table = students.merge(scores, how='left', on='ID').fillna(0)
# 数变为分数，进行调整为int
table.Score = table.Score.astype(int)

# print(table)


'''join 方式进行联合，join中是去除了left_on和right_on的'''

students = pd.read_excel('./excel/Student_Score-16.xlsx',
                         sheet_name='Students',
                         index_col='ID')
scores = pd.read_excel('./excel/Student_Score-16.xlsx',
                       sheet_name='Scores',
                       index_col='ID')

"""这里使用join可以，但是直接替换merge就会报错，就是上述15行中所说"""
table = students.join(scores, how='left').fillna(0)
table.Score = table.Score.astype(int)

print(table)
