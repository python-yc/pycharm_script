import os

print(os.getcwd())
print(os.listdir())

if os.path.isfile('a.txt'):
    os.rename('a.txt', 'b.txt')
print(os.listdir())

import pandas as pd

df = pd.DataFrame({'name': 'denny', 'Age': 18, 'addr': ''}, index=[1])
print(df)

df = pd.DataFrame({'ID': [1, 2, 3], 'Name':['Tim', 'Victor', 'Nick']})
print(df)

df = pd.DataFrame({'name': ['denny'], 'Age': [18], 'addr': ['']})
print(df)

if os.path.isfile('b.txt'):
    with open('b.txt', 'rb') as f:
        con = f.readlines()
        print(con)
