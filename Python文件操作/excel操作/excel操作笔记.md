### xlrd： 读取excel文件操作；xlwt：excel的写入

# 1、常用单元格中的数据类型
0 empty（空的）,1 string（text）, 2 number, 3 date, 4 boolean, 5 error， 6 blank（空白表格）

# 2、导入xlrd    import xlrd

# 3、打开Excel文件读取数据
data = xlrd.open_workbook(filename)#文件名以及路径，如果路径或者文件名有中文给前面加一个r拜师原生字符。

# 4、常用的函数
excel中最重要的方法就是book和sheet的操作
1）获取book中一个工作表
table = data.sheets()[0]          #通过索引顺序获取
table = data.sheet_by_index(sheet_indx)) #通过索引顺序获取
table = data.sheet_by_name(sheet_name)#通过名称获取
以上三个函数都会返回一个xlrd.sheet.Sheet()对象
names = data.sheet_names()    #返回book中所有工作表的名字
data.sheet_loaded(sheet_name or indx)   # 检查某个sheet是否导入完毕

2）行的操作
nrows = table.nrows  #获取该sheet中的有效行数
table.row(rowx)  #返回由该行中所有的单元格对象组成的列表
table.row_slice(rowx)  #返回由该列中所有的单元格对象组成的列表
table.row_types(rowx, start_colx=0, end_colx=None)    #返回由该行中所有单元格的数据类型组成的列表
table.row_values(rowx, start_colx=0, end_colx=None)   #返回由该行中所有单元格的数据组成的列表
table.row_len(rowx) #返回该列的有效单元格长度

3）列(colnum)的操作
ncols = table.ncols   #获取列表的有效列数
table.col(colx, start_rowx=0, end_rowx=None)  #返回由该列中所有的单元格对象组成的列表
table.col_slice(colx, start_rowx=0, end_rowx=None)  #返回由该列中所有的单元格对象组成的列表
table.col_types(colx, start_rowx=0, end_rowx=None)    #返回由该列中所有单元格的数据类型组成的列表
table.col_values(colx, start_rowx=0, end_rowx=None)   #返回由该列中所有单元格的数据组成的列表

4）单元格的操作  
table.cell(rowx,colx)   #返回单元格对象
table.cell_type(rowx,colx)    #返回单元格中的数据类型
table.cell_value(rowx,colx)   #返回单元格中的数据
table.cell_xf_index(rowx, colx)   # 暂时还没有搞懂

################################################
### openpyxl 的基本操作：可读可写
openpyxl中有三个不同层次的类，Workbook是对工作簿的抽象，Worksheet是对表格的抽象，Cell是对单元格的抽象，每一个类都包含了许多属性和方法。
## 1 Excel基本操作
操作Excel的一般场景:
a)打开或者创建一个Excel需要创建一个Workbook对象
b)获取一个表则需要先创建一个Workbook对象，然后使用该对象的方法来得到一个Worksheet对象
c)如果要获取表中的数据，那么得到Worksheet对象以后再从中获取代表单元格的Cell对象
创建workbook对象:
import openpyxl
>>> wb = openpyxl.Workbook('hello.xlxs')
>>> wb = openpyxl.load_workbook('file_name.xlxs')
注意：Workbook和load_workbook相同，返回的都是一个Workbook对象。
# 1.1 Workbook提供的部分常用属性如下：
active：获取当前活跃的Worksheet
worksheets：以列表的形式返回所有的Worksheet(表格)
read_only：判断是否以read_only模式打开Excel文档
write_only:判断是否以write_only模式打开Excel文档
encoding：获取文档的字符集编码
properties：获取文档的元数据，如标题，创建者，创建日期等
sheetnames：获取工作簿中的表（列表）
## 1.2 Workbook提供的部分常用方法如下：
get_sheet_names：获取所有表格的名称(新版已经不建议使用，通过Workbook的sheetnames属性即可获取)
get_sheet_by_name：通过表格名称获取Worksheet对象(新版也不建议使用，通过Worksheet['表名']获取)
get_active_sheet：获取活跃的表格(新版建议通过active属性获取)
remove_sheet：删除一个表格
create_sheet：创建一个空的表格
copy_worksheet：在Workbook内拷贝表格
## 1.3 Worksheet提供的部分常用属性如下：
title：表格的标题
dimensions：表格的大小，这里的大小是指含有数据的表格的大小，即：左上角的坐标:右下角的坐标
max_row：表格的最大行
min_row：表格的最小行
max_column：表格的最大列
min_column：表格的最小列
rows：按行获取单元格(Cell对象) - 生成器
columns：按列获取单元格(Cell对象) - 生成器
freeze_panes：冻结窗格
values：按行获取表格的内容(数据)  - 生成器
注意：freeze_panes，参数比较特别，主要用于在表格较大时冻结顶部的行或左边的行。对于冻结的行，在用户滚动时，是始终可见的，可以设置为一个Cell对象或一个端元个坐标的字符串，单元格上面的行和左边的列将会冻结(单元格所在的行和列不会被冻结)。例如我们要冻结第一行那么设置A2为freeze_panes，如果要冻结第一列，freeze_panes取值为B1，如果要同时冻结第一行和第一列，那么需要设置B2为freeze_panes，freeze_panes值为none时 表示 不冻结任何列。
Workbook提供的部分常用方法如下：
iter_rows：按行获取所有单元格，内置属性有(min_row,max_row,min_col,max_col)
iter_columns：按列获取所有的单元格
append：在表格末尾添加数据
merged_cells：合并多个单元格
unmerged_cells：移除合并的单元格
## 1.4 cell对象知识点总结
Cell对象比较简单，常用的属性如下:
row：单元格所在的行
column：单元格坐在的列
value：单元格的值
coordinate：单元格的坐标
