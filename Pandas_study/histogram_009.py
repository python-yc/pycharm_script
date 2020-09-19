# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('./excel/Students-009.xlsx')
students.sort_values(by=['Number'], inplace=True, ascending=False)

print(students)
# pandas 绘图
students.plot.bar(x='Field', y='Number', color='purple', title='International')

# 使用plt绘图
# plt.bar(students.Field, students.Number, color='purple')
# 将标签旋转90度,原因标签叠在一起
# plt.xticks(students.Field, rotation='90')
# 添加坐标轴名
# plt.xlabel('Field')
# plt.ylabel('Number')
plt.title('International Students by Field', fontsize=16)

# 变迁完全显示，紧凑型布局(如果太长，标签会被阶段)
plt.tight_layout()
plt.show()
print('over!')
