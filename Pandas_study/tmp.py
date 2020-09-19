import pandas as pd, numpy as np

books = pd.read_excel('./excel/Books.xlsx', skiprows=3,
                      usecols='C,D,E,F', index_col=None,
                      dtype={'ID': str, 'InStore': str, 'Date': str})

print(books.columns)

df = pd.DataFrame([[1, 2, 3, 4]])

print(df)

df = pd.DataFrame({'a': [1, 2, 3, 4]})

print(df)

dic2 = {'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8], 'c': [9, 10, 11, 12],
        'd': [13, 14, 15, 16]}
df2 = pd.DataFrame(dic2)
print(df2.loc[0])
print(type(df2.loc[0]))
print(df2.loc[0].values)

print((df2.loc[0].values)[0])

print(df2.index.any())
print(df.index)
print(df.index.values)
