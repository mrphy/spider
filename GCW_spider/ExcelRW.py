import xlwt
import xlrd

wb = xlwt.Workbook()
ws = wb.add_sheet('mysheet')
ws.write(0, 0, 1.01)  #把表格想象成二维表，前2各参数是行列
ws.write(0, 1, 'haha')
ws.write(1,0,'A')
ws.write(1,1,'B')
ws.write(1,2,'SUM')
ws.write(2, 0, 123)
ws.write(2, 1, 456)
ws.write(2,2,110)
ws.write(2, 3, xlwt.Formula("A3+B3"))
wb.save('example.xls')

wb = xlrd.open_workbook('example.xls')
sn = wb.sheet_names()  #获得工作所有表名
print('sheet names :'+str(sn))
#wb.sheet_by_name('name')   通过工作表名进入工作表
sh = wb.sheet_by_index(0)    #通过index进入工作表

sheets = wb.sheets()  #获取所有工作表
for sheet in sheets:
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            print(sheet.cell(row,col).value)


