# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('./excel/Students-010.xlsx')
students.sort_values(by='2017', inplace=True, ascending=False)
print(students)
# 直接在这里改字号时不支持的，可以使用plt进行添加并修改;此处title='International'可省略
plt.figure(3)
students.plot.bar(x='Field', y=['2016', '2017'], color=['purple', 'red'],
                  title='International')


# 直接使用plt的方式，由于x都用的students.Field，结果会重叠起来，但是有颜色区分
plt.figure(5)
plt.bar(students.Field, students['2017'], label='2017')
plt.bar(students.Field, students['2016'], label='2016')


plt.title('International Students', fontsize=16, fontweight='bold')
plt.xlabel('Field')
plt.ylabel('Sale')

# 获取轴
ax = plt.gca()  # get current axis
# ha 控制字体旋转的固定点
ax.set_xticklabels(students['Field'], rotation='45', ha='right')

# 获取图形
f = plt.gcf()   # get current figure
f.subplots_adjust(left=0.2, bottom=0.42)

plt.tight_layout()
plt.show()
print('over!')
