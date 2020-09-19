# -*- coding: utf-8 -*-
import pandas as pd
import  matplotlib.pyplot as plt
from scipy.stats import linregress

sales = pd.read_excel('./excel/Sales-24.xlsx', dtype={'Month': str})
print(sales)

# 斜率、截距
slope, intercept, r, p, std_err = linregress(sales.index, sales.Revenue)
# 期望值
exp = sales.index * slope + intercept

# plt.bar(sales.index, sales.Revenue)
# 散点图
plt.scatter(sales.index, sales.Revenue)
# 执行图
plt.plot(sales.index, exp, color='purple')

# plt.title('Sales')
plt.title(f'y={slope} * x + {intercept}')
plt.xticks(sales.index, sales.Month, rotation=90)
plt.tight_layout()
plt.show()
