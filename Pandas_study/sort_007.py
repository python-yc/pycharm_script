# -*- coding: utf-8 -*-
import pandas as pd

'''排序
ID	Name	    Price	Worthy
1	Product_001	9.69	YES
2	Product_002	11.6	NO
3	Product_003	25	    YES
4	Product_004	36	    NO
5	Product_005	20	    YES
'''
# products = pd.read_excel('./excel/Books-007.xlsx', index_col='ID', usecols='A:D')
# # 价格按从高到低排序，注意多项排序不能写多个sort_values函数，那样就相当于排了多次这个表
# # products.sort_values(by='Price', inplace=True, ascending=False)
# # 多重排序给个列表即可
# products.sort_values(by=['Worthy', 'Price'], inplace=True, ascending=False)
# print(products)


'''筛选过滤部分
表格前几行内容
ID	Name	Age	Score
1	Student_001	16	87
2	Student_002	26	96
3	Student_003	22	66
4	Student_004	18	59
5	Student_005	30	57
'''

# 以函数形式表达刷选的条件，年龄筛选
def age_18_to_30(a):
    return 18 <= a < 30


# 分数筛选
def level_a(s):
    return 85 <= s <= 100
    # return s == 96


# 同一个表不可以有两个相同的列，这样在读取时会有点问题
# 虽然使用了usercols参数，单表格的整体有效性不变，即：行数不同时空值为NaN
students = pd.read_excel('./excel/Books-007.xlsx', usecols='G:J',
                         index_col='ID1',
                         dtype={'ID1': str})

# 条件过滤
students = students.loc[students['Age'].apply(age_18_to_30)].\
        loc[students['Score'].apply(level_a)]

# 不使用students['Age']，使用students.Age也是可以的
students = students.loc[students.Age.apply(age_18_to_30)].\
        loc[students.Score.apply(level_a)]

# 由于有两行空的，执行时ValueError: cannot reindex from a duplicate axis
# 使用次函数查询重复轴索引，进行删除或修改即可
# print(students.index.duplicated())

print(type(students))
print(students)
