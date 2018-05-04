import linecache
import xlwt

new_book = xlwt.Workbook()
new_sheet = new_book.add_sheet("sheet1")
new_sheet.write(0,0,"tps")
new_sheet.write(0,1,"avg")
new_sheet.write(0,2,"min")
new_sheet.write(0,3,"max")
new_sheet.write(0,4,"err")

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
def get_result(content):

    str=content.split('=')[2].strip(" ")

    print("str:",str)

    tps=str.split('/s')[0]
    print("tps:",tps)

    avg=str.split(' ')[5]
    print("avg:",avg)

    min=str.split(' ')[11]
    print("min:",min)

    max =str.split(' ')[14]
    print("max:",max)

    err =str.split(' ')[18]
    print("err:",err)

    new_sheet.write(1, 0, tps)
    new_sheet.write(1, 1, avg)
    new_sheet.write(1, 2, min)
    new_sheet.write(1, 3, max)
    new_sheet.write(1, 4, err)

    return tps,avg,min,max,err

def creat_excel():
    new_book=xlwt.Workbook()
    new_sheet=new_book.add_sheet("sheet1")
    new_book.save('jmeterresult.xls')
    return new_book



#获取倒数第三行的数据
def get_tps(line_number):
    the_line=linecache.getline('test.txt',222)
    print(the_line)
    if line_number<1:
        return ''
    for cur_line_number,line in enumerate(open('test.txt','rU')):
        if cur_line_number==line_number-1:
            return line
    return ''



if __name__ == '__main__':
    line_number=get_line_count2('test.txt')
    the_line=get_tps(line_number-2)
    get_result(the_line)
    new_book.save("NewCreateWorkbook.xls")


