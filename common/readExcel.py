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
        print('sheetData:',self.sheetData)
        print(type(self.sheetData))
        print(self.sheetData1)
        print('sheetData1是个DATA1:',self.sheetData1)
        print('DATA2:',self.sheetData2)

    def addDate(self):
        dat = []
        sheet3 = []
        #将sheet3中的第二列存入列表
        for a in self.sheetData2:
            sheet3.append(a[1])
        print('sheet3[1]:',sheet3)

        for i in range(3):
            #将sheet1列表中的元素（也是个列表）和sheet2的中的元素（也是个列表）相加
            data = self.sheetData[i] + self.sheetData1[i][1:]
            #将sheet3的数据追加到列表后
            data.append(sheet3[i])

            #追加到大列表中
            dat.append(data)
        print('#######',dat)

        pass

read = readExcel()
read.getData()
read.addDate()


# #列表方法zip
# a = [1,2,3]
# b = ['a','b','c']
# c = [4,5,6]
#
# x = list(zip(a,b,c))
# print(x)
# # m = []
# # for a,b,c in x:
# #     print(a,c)
# #     m.append((a,c))
# #     print(m)
# a = []
# for i in x:
#     print('i----',i)
#     a.append((i[0],i[-1]))
#     print('---',a)