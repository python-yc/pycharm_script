# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

# 列太长，默认输出时部分被隐藏，如果不要隐藏，进行配置
pd.options.display.max_columns = 777

home_data = pd.read_excel('./excel/home_data-14.xlsx')
print(home_data.head())
print(home_data.shape)

'''散点图'''
# home_data.plot.scatter(x='price', y='sqft_living')
# home_data.plot.scatter(y='sqft_living', x='price')

'''房屋面积直方图'''
# home_data.sqft_living.plot.hist(bins=100)
# plt.xticks(range(0, max(home_data.sqft_living), 5000), fontsize=8, rotation=90)

'''密度图'''
# home_data.sqft_living.plot.kde()
# plt.xticks(range(0, max(home_data.sqft_living), 500), fontsize=8, rotation=90)
#
# plt.show()

print(home_data.corr())
