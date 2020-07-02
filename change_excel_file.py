import xlrd
import xlwt
file_name = 'result.xls'
rdata = xlrd.open_workbook(file_name)
print(type(rdata))
sheet1 = rdata.sheet_by_index(0)
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('my_sheet')
worksheet.write(0,0,'学校名称')
worksheet.write(0,1,'2019年最低分数')
worksheet.write(0,2,'2018年最低分数')
worksheet.write(0,3,'2017年最低分数')
row_count = 1
row_total = sheet1.nrows
def getMin(max , min):
    print(type(max))
    if str(max) == '999.0':
        return min
    else:
        return max
for i in range(1,row_total):
    name = sheet1.row(i)[0]
    max_2019 = sheet1.row_values(i)[1]
    min_2019 = sheet1.row_values(i)[2]
    max_2018 = sheet1.row_values(i)[3]
    min_2018 = sheet1.row_values(i)[4]
    max_2017 = sheet1.row_values(i)[5]
    min_2017 = sheet1.row_values(i)[6]
    unit_2019 = getMin(max_2019,min_2019)
    unit_2018 = getMin(max_2018,min_2018)
    unit_2017 = getMin(max_2017,min_2017)
    worksheet.write(i,0,str(name))
    worksheet.write(i,1,str(unit_2019))
    worksheet.write(i,2,str(unit_2018))
    worksheet.write(i,3,str(unit_2017))

workbook.save('changed_file.xls')