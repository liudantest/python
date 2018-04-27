# -*- coding:utf-8 -*-
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy


def read_excel():
    rexcel=open_workbook('test.xls')
  #  xlrd.open_workbook('test.xls').sheet_by_name('sheet0').ncols
    sheet1_content=rexcel.sheet_by_name('sheet1')
    sheet1_col = sheet1_content.ncols
    print(sheet1_col)
    excel=copy(rexcel)
    sheet1=excel.get_sheet(0)





    workbook2=open_workbook('test2.xls')
    sheet2_col=workbook2.sheet_by_name('sheet1').ncols
    print(sheet2_col)
    sheet2_content = rexcel.sheet_by_name('sheet1')




    for i  in range(1,sheet1_col+1):
        for j in range(1,sheet2_col+1):
            #sheet1的第一列的内容
            print(sheet1_content.cell(i,1).value)
            #sheet1第二列的内容
            if int(sheet1_content.cell(i,1).value)==int(sheet2_content.cell(j,1).value):
                # 将user_id写入excel
                sheet1.write(i,sheet1_col,int(sheet2_content.cell(j,1).value))
                print("ok")




    sheet1.write(0,sheet1_col,'mobile_2')
    excel.save('test.xls')










if __name__=='__main__':
    read_excel()
