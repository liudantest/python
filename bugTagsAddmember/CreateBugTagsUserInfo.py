# -*- coding:utf-8 -*-
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy


excel1_name='test.xls'
excel1_sheet1_name='Sheet1'

excel2_name='test2.xls'
excel2_sheet1_name='Sheet1'


def read_excel():
    rexcel=open_workbook(excel1_name)
    sheet1_content=rexcel.sheet_by_name(excel1_sheet1_name)
    sheet1_col = sheet1_content.ncols
    sheet1_row=sheet1_content.nrows
    print("sheet1的 rows,col:%d %d" % (sheet1_row,sheet1_col))
    excel=copy(rexcel)
    sheet1=excel.get_sheet(0)

    workbook2=open_workbook(excel2_name)
    sheet2_content = workbook2.sheet_by_name(excel2_sheet1_name)
    #获取列数
    sheet2_col=sheet2_content.ncols
    sheet2_row=sheet2_content.nrows
    print("sheet2的 rows,col:%d %d" % (sheet2_row,sheet2_col))

    #获取sheet表的内容
    sheet2_content = workbook2.sheet_by_name(excel2_sheet1_name)

    for i  in range(1,sheet1_row):
        for j in range(1,sheet2_row):
            #sheet1的第i行，第二列的内容
            print('sheet1',int(sheet1_content.cell(i,1).value))
            #sheet2的第j行，第二列的内容
            print('sheet2',int(sheet2_content.cell(j,1).value))
            #比较sheet1和sheet2同列同行的内容，如果相等则将sheet2的内容写入到sheet1中，追加一列
            if int(sheet1_content.cell(i,1).value)==int(sheet2_content.cell(j,1).value):
                # 将user_id写入excel
                sheet1.write(i,sheet1_col,int(sheet2_content.cell(j,1).value))
                sheet1.write(i, sheet1_col+1,sheet2_content.cell(j, 0).value)
                print("ok")

    sheet1.write(0,sheet1_col,'mobile_2')
    sheet1.write(0, sheet1_col+1, 'name')
    excel.save(excel1_name)


if __name__=='__main__':
    read_excel()
