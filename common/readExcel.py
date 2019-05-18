#coding=utf-8
#__author__= 'jws'

#导入包
import xlrd

# #找到excel文件，并打开，判断文件是否存在，捕获异常
# readbook = xlrd.open_workbook(r"C:\D\interfaceTest\testData\data.xls")
#
# #定位sheet页
# sheet = readbook.sheet_by_index(0)
# print(sheet)
#
# #获取
#
# #定位行和列
# rowvalue = sheet.row_values(1)
# colvalue = sheet.col_values(0)
# print(rowvalue)
# print(colvalue)
# #读取excel数据
#
# #组装测试数据为一条正确匹配的接口测试数据


class readExcel:
    readbook = xlrd.open_workbook(r'C:\D\interfaceTest\testData\data.xls')
    #获取所有sheet页
    sheetall = readbook.sheet_names()
    print(type(sheetall))
    #存sheet里的数据
    sheetData = []
    sheetData1 = []
    sheetData2 = []
    sheetRest = []
    def getData(self):
        for i in self.sheetall:
            sheet = self.readbook.sheet_by_name(i)
            # print(sheet)
            #获取sheet页最大行数和列数
            sheet_nrows = sheet.nrows
            # sheet_ncols = sheet.ncols
            # print(sheet_nrows,sheet_ncols)

            for j in range(1,sheet_nrows):
                #获取sheet1的第一行
                sheet_row = sheet.row_values(j)#获取行
                #print(sheet_row)
                if self.sheetall.index(i) == 0:
                    self.sheetData.append(sheet_row)
                elif self.sheetall.index(i) == 1:
                    self.sheetData1.append(sheet_row)
                elif self.sheetall.index(i) == 2:
                    self.sheetData2.append(sheet_row)
        print(self.sheetData)
        print(type(self.sheetData))
        print(self.sheetData1)
        print(self.sheetData2)

    def addDate(self):
        data = self.sheetData[0] + self.sheetData1[0][1:]
        print('#######',data)
        pass

read = readExcel()
read.getData()
read.addDate()