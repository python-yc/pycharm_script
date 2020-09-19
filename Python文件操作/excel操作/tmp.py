# -*- coding: utf-8 -*-
import pandas as pd, numpy as np

df = pd.DataFrame(columns=['a', 'b', 'c', 'd'])

# stu = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd':4})
# print(df.head())
df = df.append({'a': 1, 'b': 2, 'c': 3, 'd':4}, ignore_index=True)
# df = df.append(stu, ignore_index=True)
df = df.set_index('a')
print(df)
# df.to_excel('D:/ab.xlsx')


df = pd.DataFrame({'ID': [1, 2, 3], 'Name':['Tim', 'Victor', 'Nick']})
df = df.set_index('ID')

df = pd.DataFrame({'ID': [1, 2, 3], 'Name':['Tim', 'Victor', 'Nick']})
# df = df.set_index('ID')
# df = df.append(['6', 'denny'])
print('======')
print(df)

df = pd.DataFrame({'ID': [1, 2, 3], 'Name':['Tim', 'Victor', 'Nick']})

df = df.append({'ID': 6, 'Name':'denny'}, ignore_index=True)
print('===')
print(df)
