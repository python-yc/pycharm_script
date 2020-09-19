# -*- coding: utf-8 -*-
# 虽然没导入，但是要安装openpyxl库
import pandas as pd
import os

# 没有任何参数直接创建一个空的Excel
# df = pd.DataFrame()
# if not os.path.isfile('./excel/output.xlsx'):
#     df.to_excel('./excel/output.xlsx')
# else:
#     print('./excel/output.xlsx exist!')
# print("Done!")

# 创建Excel并添加内容
df = pd.DataFrame({'ID': [1, 2, 3], 'Name':['Tim', 'Victor', 'Nick']})
# 不设置索引，默认有数字索引
df = df.set_index('ID')
df.to_excel('./excel/output.xlsx')
print("Done!")

