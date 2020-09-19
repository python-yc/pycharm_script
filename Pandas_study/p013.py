# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

weeks = pd.read_excel('./excel/Orders-013.xlsx', index_col='Week')
print(weeks)
print(weeks.columns)
# weeks.plot(y=['Accessories', 'Bikes', 'Clothing', 'Components', 'Grand Total'])

# 使用叠加折线图绘制
weeks.plot.area(y=['Accessories', 'Bikes', 'Clothing', 'Components', 'Grand Total'])

plt.title('Sales Weekly Trend', fontsize=16, fontweight='bold')
plt.ylabel('Total', fontsize=12, fontweight='bold')
plt.xticks(weeks.index, fontsize=8)
plt.show()
