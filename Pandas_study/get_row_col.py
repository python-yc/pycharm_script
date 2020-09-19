# -*- coding: utf-8 -*-
import pandas as pd, numpy as np

df = pd.DataFrame(np.arange(12).reshape(3,4), index=list(range(3)),
                  columns=list('abcd'))

print(df)

"""
   a  b   c   d
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
"""


"""
总结每个方式首先记住一个：
row: df.loc[row_index]      df.loc[1]
col: df[['a', 'b']]
val: df['b'][1]
"""

print('获取列内容===============')
"""获取列内容"""
# 获取列内容两种方式；获取多列时会显示列名，单列不显示，,但是有name属性输出
print("df[['a', 'b']] a,b 两列内容")
print(df[['a', 'b']])    # 获取多列要以列表传入

print("\ndf['b'] b一列内容")
print(df['b'])

print('\ndf.a方式一列')
print(df.a)     # 获取第a 列

print("\ndf.loc[:, ['a', 'b']]")
print(df.loc[:, ['a', 'b']])

print("\ndf.loc[:, ['a']]")
print(df.loc[:, ['a']])

# print("\ndf.loc[['a', 'b']]")  这个不支持
# print(df.loc[['a', 'b']])

'''获取行内容'''
# 获取行内容,使用loc :(select by lable)定位索引获取，
# 同列一样，当行不显示行索引，而且是竖向输出,但是有name属性输出
# 也可以这样使用切片 df = df[0:1] 但是不能df = df[0]
print('获取行内容================')
print('df[0:1]')
print(df[0:1])

# 获取指定行
print("df.loc[[0, 2]] 获取指定行")
print(df.loc[[0, 2]])

print('\ndf.loc[1]一行')
print(df.loc[1])
print("\ndf.loc[1:2]两行")
print(df.loc[1:2])

print("\ndf[0:2] 的行")
print(df[0:2])
# 获取行内容,使用iloc :(select by position)定位非索引获取，
print("\ndf.iloc[2] 第三3行")
print(df.iloc[2])

print("\ndf.iloc[0::2, 1:3] step为2的表示")
print(df.iloc[0::2, 1:3])

print("\ndf.iloc[0:2, 1:3] ,注意与上面一个对比，少个冒号，不同表示")
print(df.iloc[0:2, 1:3])

print("\ndf.iloc[[0, 2], 1:3] 第一行和第三行")
print(df.iloc[[0, 2], 1:3])


"""# 取单元格的值"""
print("取单元格的值===============")
print("\ndf['a'][1] 先列后行取值法")
print(df['a'][1])

print("\ndf.loc[1, 'a'] 行列式取值法")
print(df.loc[1, 'a'])

print("\ndf['a'][0:2][1]")
print(df['a'][0:2][1])

print("\ndf['a'][0:2]")
print(df['a'][0:2])

print(type(df['a'][0:2]))

print("\ndf.loc[1, ['a', 'b']] 第2行ab列的值")
print(df.loc[1, ['a', 'b']])

print("\ndf.a > 5 筛选，结果为bool")
print(df.a > 5)

print("\ndf.at[1, 'a'] = 99")
df.at[1, 'a'] = 99
print(df)

print("\ndf['a'].at[2] = 100")
df['a'].at[2] = 100
print(df)
