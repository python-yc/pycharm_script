# -*- coding: utf-8 -*-
import pandas as pd

"""csv/tsv/txt都是一种纯本文文件，所以读取方法一样read_csv"""
# 读取csv文件
students1 = pd.read_csv('./excel/Students-22.csv', index_col='ID')
print(students1)

students2 = pd.read_csv('./excel/Students-22.tsv', sep='\t', index_col='ID')
print(students2)

students3 = pd.read_csv('./excel/Students-22.txt', sep='|', index_col='ID')
print(students3)
