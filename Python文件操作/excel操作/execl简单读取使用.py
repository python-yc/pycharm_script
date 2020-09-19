# -*- coding: utf-8 -*-

import xlrd

workbook = xlrd.open_workbook(r'./excel练习信息.xlsx')

table = workbook.sheets()

print(workbook)
print(table)
print(table[0])
table = workbook.sheet_by_name(r'年龄')
table = workbook.sheet_by_index(0)

names = workbook.sheet_names()
print(names)
print(workbook.sheet_loaded(0))
print(workbook.sheet_loaded(r'年龄'))

# 遍历表格的每一行内容
nrows = table.nrows
ncols = table.ncols
print(nrows, ncols, sep="##")
for i in range(1, nrows + 1):
    # print("第" + str(i) + "行内容为: ", table.row(rowx=i-1))
    print("第 {} 行内容为：{}".format(i, table.row(rowx=i-1)))
    if i < 4:
        print("且第三列的值为：",table.cell_value(i-1, 2))
# row_con = table.row(rowx=2)
# print(row_con)
# print(table.row_slice(1))
# print(table.row_len(3))
