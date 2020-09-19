# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

users = pd.read_excel('./excel/Users-011.xlsx')
users['Total'] = users['Oct'] + users['Nov'] + users['Dec']
users.sort_values(by='Total', inplace=True)
print(users)

# 多个柱状图进行叠加成一个
# users.plot.bar(x='Name', y=['Oct', 'Nov', 'Dec'], stacked=True, title='User Behavior')

# barh 表示水平方向展示
users.plot.barh(x='Name', y=['Oct', 'Nov', 'Dec'], stacked=True, title='User Behavior')
plt.tight_layout()
plt.show()
