# -*- coding: utf-8 -*-
import pandas as pd
from datetime import date, timedelta

books = pd.read_excel('./excel/Books.xlsx', skiprows=3,
                      usecols='C,D,E,F', index_col=None,
                      dtype={'ID': str, 'InStore': str, 'Date': str})
# books['ID'].at[0] = 100

# 由于月份在excel中递增填充比较麻烦，因此给个单独函数
def add_month(d, md):
    yd = md // 12
    m = d.month + md % 12
    if m != 12:
        yd += m // 12
        m = m % 12
    return date(d.year + yd, m, d.day)


start = date(2018, 1, 20)
# 此方式时先拿到series值，再进行修改，还有一种方式直接拿到单元格去修改，dataframe的方式
# for i in books.index:
#     books['ID'].at[i] = i + 1
#     books['InStore'].at[i] = 'YES' if i % 2 == 0 else 'NO'
#     # books['Date'].at[i] = start + timedelta(days=i) # 日增
#     # books['Date'].at[i] = date(start.year + i, start.month, start.day)  # 年增
#     books['Date'].at[i] = add_month(start, i)   # 月增

# dataframe的方式
for i in books.index:
    books.at[i, 'ID'] = i + 1
    books.at[i, 'InStore'] = 'YES' if i % 2 == 0 else 'NO'
    # books['Date'].at[i] = start + timedelta(days=i) # 日增
    # books['Date'].at[i] = date(start.year + i, start.month, start.day)  # 年增
    books.at[i, 'Date'] = add_month(start, i)   # 月增

# 不生成额外的index列
books.set_index('ID', inplace=True)
print(books)
print(books['Name'].at[1])
# 保存表格
# books.to_excel('./excel/auto_fill.xlsx')
