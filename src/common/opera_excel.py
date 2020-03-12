# -*- coding: utf-8 -*-
'''
Created on 2018年11月2日

@author: uidq1501
'''
import xlrd
from xlutils.copy import copy 
# excel = xlrd.open_workbook(r"D:\Users\uidq1501\eclipse-workspace\android_test\src\config\case.xlsx")
# data = excel.sheets()[0]
# print data.nrows
# print data.cell(2,5).value

class OperaExcel:
    
    def __init__(self, i=None, file_path=None):
        if file_path == None:
            self.file_path = r"..\config\case.xls"
        else:
            self.file_path = file_path
        if i == None:
            i = 0
            
        self.excel = self.read_excel()
        self.data = self.get_sheets(i)
            
    def read_excel(self):
        # 获取Excel文件
        excel = xlrd.open_workbook(self.file_path)
        return excel
    
    def get_sheetname(self):
        name = self.excel.sheet_names()
        return name
    
    def get_sheets(self, i):
        # 获取Excel文件中某个sheet的内容
        data = self.excel.sheets()[i]
        return data
    
    def get_lines(self):
        # 获取sheet的行数
        lines = self.data.nrows
        return lines
    
    def get_value(self, row, line):
        # 获取某个单元个值
        data = self.data.cell(row, line).value
        return data
    
    def write_value(self, i, row, line, value):
        read_value = self.read_excel()
        write_data = copy(read_value)
        write_save = write_data.get_sheet(i)
        write_save.write(row, line, value)
        write_data.save(self.file_path)
        
#     def input_picture(self,pic,row):
#         read_value = self.read_excel()
#         write_data = copy(read_value)
#         write_save = write_data.
#         write_save.insert_image(row,1,pic)
#         write_data.save(self.file_path)
#         
    
if __name__ =='__main__':
    opera = OperaExcel()
    print(opera.get_sheetname())
#     print opera.get_lines()
#     time.sleep(5)
#     opera.write_value(7, 8, 'pass')
#     opera.write_value(7, 9, 'fail')
#     opera.write_value(7, 10, 'pass')
                 
    