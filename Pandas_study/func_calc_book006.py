# -*- coding: utf-8 -*-
import pandas as pd

books = pd.read_excel('./excel/Books-006.xlsx', index_col='ID')

print('Book_001 原本价格：', books['ListPrice'].at[1])

# 给每本书涨价两元,下面也有使用apply函数修改
books['ListPrice'] = books['ListPrice'] + 2
print('Book_001 涨2元价格：', books['ListPrice'].at[1])

# 使用series的另外一种重要函数apply
def add_2(x):
    return x + 2


# 也可以直接使用lambda表达式 lambda x: x + 2
books['ListPrice'] = books['ListPrice'].apply(add_2)
# books['ListPrice'] = books['ListPrice'].apply(lambda x: x + 2)
print('Book_001 再涨2元价格：', books['ListPrice'].at[1])

# 此方式比较常用的计算，下面循环的单元格方式
books['Price'] = books['ListPrice'] * books['Discount']

#循环的单元格方式
# for i in books.index:
#     # series 类型方式
#     # books['Price'].at[i] = books['ListPrice'].at[i] * books['Discount'].at[i]
#     # dataframe 类型方式
#     books.at[i, 'Price'] = books.at[i, 'ListPrice'] * books.at[i, 'Discount']

print(books)
# 保存
# books.to_excel('./excel/Books-006.xlsx')
