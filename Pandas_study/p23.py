# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

pd.options.display.max_columns = 666
orders = pd.read_excel('./excel/Orders-23.xlsx')

# print(orders.head())
# print(orders.Date.dtype)

orders['Year'] = pd.DatetimeIndex(orders['Date']).year
# print(orders.head())

pt1 = orders.pivot_table(index='Category', columns='Year', values='Total', aggfunc=np.sum)

print(pt1)

print("second method")
# second method

pd.options.display.max_columns = 666
orders = pd.read_excel('./excel/Orders-23.xlsx')

orders['Year'] = pd.DatetimeIndex(orders['Date']).year
groups = orders.groupby(['Category', 'Year'])
s = groups['Total'].sum()
c = groups['ID'].count()

pt2 = pd.DataFrame({'Sum': s, 'Count': c})
print(pt2)

