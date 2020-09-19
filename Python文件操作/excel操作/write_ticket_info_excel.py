# -*- coding: utf-8 -*-
import xlwt

"""
需要稍作解释的就是write_merge方法：

write_merge(x, x + m, y, w + n, string, sytle)
x表示行，y表示列，m表示跨行个数，n表示跨列个数，string表示要写入的单元格内容，style表示单元格样式。其中，x，y，w，h，
都是以0开始计算的。
这个和xlrd中的读合并单元格的不太一样。
如下述：sheet1.write_merge(21,21,0,1,u'合计',set_style('Times New Roman',220,True))
即在22行合并第1,2列，合并后的单元格内容为"合计"，并设置了style。
如果需要创建多个sheet，则只要f.add_sheet即可。
"""

def set_style(name, height, bold=False):
    """
    设置单元格样式
    :param name: 表头名
    :param height: 单元格高度
    :param bold: 单元格宽度
    :return: 单元格样式
    """
    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体
    font.name = name    # 'Times New Roman'
    font.bold = bold
    font.colour_index = 4
    font.height = height

    # borders = xlwt.Borders()
    # borders.left = 6
    # borders.right = 6
    # borders.top = 6
    # borders.bottom = 6

    style.font = font
    # style.borders = borders

    return style


# 写excel
def write_excel():
    f = xlwt.Workbook() # 创建工作簿

    """创建一个sheet：sheet1"""
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True) # 创建sheet
    row0 = [u'业务', u'状态', u'北京', u'上海', u'广州', u'深圳', u'状态小计', u'合计']
    column0 = [u'机票', u'船票', u'火车票', u'汽车票', u'其它']
    status = [u'预定', u'出票', u'退票', u'业务小计']

    # 生成第一行
    for i in range(len(row0)):
        sheet1.write(0,i,row0[i],set_style('Times New Roman',220,True))

    # 生成第一列和最后一列(合并4行)
    i, j = 1, 0
    while i < 4*len(column0) and j < len(column0):
        sheet1.write_merge(i,i+3,0,0,column0[j],set_style('Arial',220,True))    # 第一列
        sheet1.write_merge(i,i+3,7,7)   # 最后一列"合计"
        i += 4
        j += 1

    sheet1.write_merge(21,21,0,1,u'合计',set_style('Times New Roman',220,True))

    # 生成第二列
    i = 0
    while i < 4*len(column0):
        for j in range(0,len(status)):
            sheet1.write(j+i+1,1,status[j])
        i += 4

    f.save('ticket_info.xlsx')  # 保存文件

if __name__ == '__main__':
    # generate_workbook()
    # read_excel()
    write_excel()

