#!/usr/bin/env python
# encoding: utf-8
import linecache
import xlwt
import os

new_book = xlwt.Workbook()
new_sheet = new_book.add_sheet("sheet1")
new_sheet.write(0,0,"name")
new_sheet.write(0,1,"thread")
new_sheet.write(0,2,"tps")
new_sheet.write(0,3,"avg")
new_sheet.write(0,4,"min")
new_sheet.write(0,5,"max")
new_sheet.write(0,6,"err")

#获取txt文件的行数
def get_line_count2(filename):
    count=0
    with open(filename,'r',encoding='utf-8') as f:
        for file_line in f.readlines():
            file_line=file_line.strip()
            count+=1
    print(count)
    return count
#获取指定行中的指定内容
def insert_result(content,row,file):

    str=content.split('=')[2].strip(" ")

    print("str:",str)

    tps = str.split('/s')[0]
    print("tps:", tps)

    avg = str.split(' ')[3]
    print("avg:", avg)

    min = str.split(' ')[7]
    print("min:", min)

    max = str.split(' ')[10]
    print("max:", max)

    err = str.split('Err:     ')[1]
    print("err:", err)

    name=file.split('.')[0]
    print(name)

    thread=file.split('.')[1]
    print(thread)
    new_sheet.write(row, 0, name)
    new_sheet.write(row, 1, thread)
    new_sheet.write(row, 2, tps)
    new_sheet.write(row, 3, avg)
    new_sheet.write(row, 4, min)
    new_sheet.write(row, 5, max)
    new_sheet.write(row, 6, err)

    return tps,avg,min,max,err

def creat_excel():
    new_book=xlwt.Workbook()
    new_sheet=new_book.add_sheet("sheet1")
    new_book.save('jmeterresult.xls')
    return new_book



#获取倒数第三行的数据
def get_rowdata(line_number,file):
    the_line=linecache.getline(file,222)
    print(the_line)
    if line_number<1:
        return ''
    for cur_line_number,line in enumerate(open(file,'rU')):
        if cur_line_number==line_number-1:
            return line
    return ''


# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    path=set()
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        #print(child) # .decode('gbk')是解决中文显示乱码问题
        path.add(child)
    return path


if __name__ == '__main__':
    child=eachFile('E:\PythonTools\CollectDataFromJtl\data\\')

    a=1
    for file in child:
        print("test>>>",file)
        line_number=get_line_count2(file)
        the_line=get_rowdata(line_number-2,file)
        insert_result(the_line,a,file)
        a+=1
        new_book.save("NewCreateWorkbook.xls")







