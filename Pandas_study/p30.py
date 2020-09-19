# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


def get_circumcirecle_area(l, h):
    r = np.sqrt(l**2+h**2)/2
    return r**2*np.pi


def wrapper(row):
    return get_circumcirecle_area(row['Length'], row['Height'])

rects = pd.read_excel('./excel/Rectangles-30.xlsx', index_col='ID')


# 使用两个函数去返回或者后面直接使用lambda表达式
# rects['CA'] = rects.apply(wrapper, axis=1)
rects['CA'] = rects.apply(lambda row: get_circumcirecle_area(row['Length'], row['Height']), axis=1)

print(rects)

# print(any(rects['Length'] == 8))
# print(all(rects['Length'] == 8))
# print(rects.loc[rects['Length'] >= 8])
# print(rects[rects['Length'] >= 8].index)
