#coding=utf-8
#__author__= 'jws'


import xlrd

class ReadExcel:
    #将打开excel方法赋与变量readbook
    readbook = xlrd.open_workbook(r'C:\D\interfaceTest\testData\data.xls')
    #通过实例化的readbook获取所有sheet页的名称
    sheetall = readbook.sheet_names()
    #创建存放sheet页数据的列表
    urlSheet = []
    paraamSheet = []
    assertSheet =[]

    #创建一个读取sheet页数据的方法
    def getData(self):
        for i in self.sheetall:
            sheet = self.readbook.sheet_by_name(i)
            #获取sheet页最大行数
            sheet_nrow = sheet.nrows

            for j in range(1,sheet_nrow):
                #获取行数据
                sheet_row = sheet.row_values(j)
                if i == 'urlSheet':
                    self.urlSheet.append(sheet_row)
                elif i =='paramSheet':
                    self.paraamSheet.append(sheet_row)
                elif i == 'assertSheet':
                    self.assertSheet.append(sheet_row)

    #创建一个重新构建数据的方法
    def addData(self):
        enData = []
        for i in range(len(self.urlSheet)):
            #将列表中数据读出后按需要拼接
            data = self.urlSheet[i] + self.paraamSheet[i][1:] + list(self.assertSheet[i][1])
            #追加到列表中
            enData.append(data)
        # print(enData)
        return enData

read = ReadExcel()
read.getData()
read.addData()