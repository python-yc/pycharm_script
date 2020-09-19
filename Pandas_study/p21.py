# -*- coding: utf-8 -*-
import pandas as pd

pd.options.display.max_columns = 666

# 为避免行列互换后自动有行索引，首先打开时添加列索引
videos = pd.read_excel('./excel/Videos-21.xlsx', index_col='Month')

# 旋转
table = videos.transpose()

print(table)
