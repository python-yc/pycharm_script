# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('./excel/Students-012.xlsx', index_col='From')
print(students)

# lable = students['From']
# print(lable)
# 由于数字比较特殊，此处只能使用方括号(虽然在表格中类型为字符串)，字符则用students.Field
students['2017'].plot.pie(fontsize=8)
# plt.pie(students['2017'], labels=students['From'])    # 使用这个时需要去掉读表时的索引

# 方法一、使用排序再startangle进行按顺时针旋转
# students['2017'].sort_values(ascending=True).plot.pie(fontsize=8, startangle=-270)

# 方法二、不排序，调整一个counterclock参数
# students['2017'].plot.pie(fontsize=8, counterclock=False, startangle=-270)

# 优化饼图
# plt.title('Source of International Students', fontsize=16, fontweight='bold')
plt.title('Source of International Students', fontsize=16)
# plt.ylabel('2017', fontsize=12, fontweight='bold')
plt.ylabel('2017', fontsize=12)
plt.show()
