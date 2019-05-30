#coding=utf-8
#__author__= 'jws'

'''
1，创建新建空白表方法，使用os模块获取当前路径的父路经，
2，创建追加方法，一行一行追加数据

'''


# from xlutils.copy import copy
# import xlrd
import xlwt
import os

class WriteExcel():

    def writeData(self):
        path = os.path.dirname(os.getcwd()) + '\\' + 'report\\jws.xls'
        workbook = xlwt.Workbook()               # 新建一个工作簿
        sheet = workbook.add_sheet('test1')      #创建工作表
        value = [[1,2,3],[4,5,6],[7,8,9]]
        #写入
        for i in range(len(value)):            #让i遍历value列表的长度 （以列表的长度迭代）相当于sheet行
            for j in range(len(value[i])):     #让j遍历value中的列表的长度（）相当与sheet列
                sheet.write(i, j, value[i][j])   #写入value中的值
        workbook.save(path)  # 保存工作簿

a = WriteExcel()
a.writeData()


