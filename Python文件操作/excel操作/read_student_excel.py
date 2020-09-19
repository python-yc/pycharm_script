# -*- coding: utf-8 -*-

## 学习自 https://www.cnblogs.com/linyfeng/p/7123423.html
## 表格元素类型说明：ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
# 1、打开excel文件并获取所有sheet
import xlrd
workbook = xlrd.open_workbook(r'D:\pycharm_script\Python文件操作\excel操作\Student.xlsx')
print(workbook.sheet_names())   # ['Sheet1', 'Sheet2', 'Sheet3']

# 2、根据下标获取sheet名称
sheet2_name = workbook.sheet_names()[1]
print(sheet2_name)  # Sheet2

# 3、根据sheet索引或者名称获取sheet内容，同时获取sheet名称、行数、列数
sheet2 = workbook.sheet_by_index(1)
print(sheet2.name, sheet2.nrows, sheet2.ncols)  # Sheet2 6 5

# 4、根据sheet名称获取整行和整列的值
sheet2 = workbook.sheet_by_name('Sheet2')
# print(sheet2.name, sheet2.nrows, sheet2.ncols)
rows = sheet2.row_values(3)
cols = sheet2.col_values(2)
print(rows, cols, sep='\n')
# 41462.0为日期2013/7/7，实际却显示为浮点数。后面有描述如何纠正
# ['lisi', 19.0, 41462.0, 'bashketball', 'friend2']
# ['出生日期', 42129.0, 42161.0, 41462.0, 40941.0, '']

# 5、获取指定单元格内容
print(sheet2.cell(1,0))   # text:'xiaoming'
print(sheet2.cell(1,0).value)   # xiaoming
print(sheet2.cell(1,0).value.encode('utf-8'))   # b'xiaoming'

print(sheet2.cell_value(1,0))   # xiaoming
print(sheet2.row(1)[0].value)   # xiaoming

# 6、获取单元格内容的数据类型
print(sheet2.cell(1,0).ctype)   # 第2行第1列:xiaoming2 为string类型
print(sheet2.cell(1,1).ctype)   # 第2行第2列:12  为number类型
print(sheet2.cell(1,2).ctype)   # 第2行第3列:2015/5/5 为date类型

## 说明：ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error

# 7、获取单元内容为日期类型的方式
# 使用xlrd的xldate_as_tuple处理date格式，先判断表格的ctype=3时，xlrd才能执行操作，如下：
from datetime import datetime, date
print(sheet2.cell(1,2).ctype)
print(sheet2.cell(1,2).value)   # 42129.0
if sheet2.cell(1,2).ctype == 3:  # 3
    date_value = xlrd.xldate_as_tuple(sheet2.cell_value(1,2), workbook.datemode)
    print(date_value)   # (2015, 5, 5, 0, 0, 0)
    print(date(*date_value[:3]))    # 2015-05-05
    print(date(*date_value[:3]).strftime('%Y/%m/%d'))   # 2015/05/05

# 8、获取合并单元格的内容
print(sheet2.cell(1,4).value)   #　friend
print(sheet2.cell(2,4).ctype)   #　0 表示空
print(sheet2.cell_value(5,1))   #　None
print(sheet2.cell_type(5,2))   #　0 表示空
print(sheet2.cell_type(5,3))   #　0 表示空
"""
从实验结果可以看出来，第6行的第2和第3第4列是合并单元格，但这里我们只获取到第6行第2列的值
而第3列第4列获取的内容为空，理论上来说合并的；

单元格内容应该是一样的，但是现在只有合并的第一个单元格可以获取到值，
其他为空，如何处理? 再用一种更直观的方式显示；
"""
print(sheet2.row_values(5))
# ['zhaoliu', 'None', '', '', ''] 空值部分表示为合并单元格
print(sheet2.col_values(4))
#　['关系', 'friend', '', 'friend2', '', '']　空值部分为合并单元格，注意这里是两个合并单元格，最后一个空值为行上的合并结果；
"""
可以利用merged_cells方法进行处理，处理的方法是只能获取合并单元格的第一个cell的行列索引，才能读到值，读错了就是空值。
即合并行单元格读取;行的第一个索引，合并列单元格读取列的第一个索引。
这里，需要在读取文件的时候添加个参数，将formatting_info参数设置为True，默认是False，否
则可能调用merged_cells方法获取到的是空值。
"""
# 报错处理方案 https://www.cnblogs.com/Detector/p/8709362.html

# 如果workbook实例不报错，可以以下方式执行，输出合并单元格的内容
# workbook = xlrd.open_workbook(r'D:\pycharm_script\Python文件操作\excel操作\Student.xlsx', formatting_info=True)
# sheet2 = workbook.sheet_by_name('Sheet2')
# print(sheet2.merged_cells)    # 此处报错：NotImplementedError: formatting_info=True not yet implemented
# 案例结果：[(1, 3, 4, 5), (3, 5, 4, 5), (5, 6, 1, 5)]
"""
merged_cells返回的这四个参数的含义是：(row,row_range,col,col_range),其中[row,row_range)包括row,不包括row_range,col也是一样，下标从0开

始。即(1, 3, 4, 5)的含义是：第2到3行（不包括第4行）合并，(5, 6, 1, 5)的含义是：第2到5列合并。利用这个，可以分别获取合并的三个单元格的内容：
"""
print(sheet2.cell_value(1, 4)) # #(1, 3, 4, 5)  #结果friend
"""发现规律了没？是的，获取merge_cells返回的row和col低位的索引即可！ 于是可以这样一劳永逸："""
# merge = []
# for (rlow,rhigh,clow,chigh) in sheet2.merged_cells:
#     merge.append([rlow, clow])
#
# # merge = [[1, 4], [3, 4], [5, 1]]
#
# for index in merge:
#     print(sheet2.cell_value(index[0], index[1]))
