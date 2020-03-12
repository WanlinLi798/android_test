# -*- coding: utf-8 -*-
'''
Created on 2018年11月2日

@author: uidq1501
'''
from common.opera_excel import OperaExcel

class GetExcel:
    def __init__(self, i=None):
        if i == None:
            i = 0
        self.opera = OperaExcel(i)
        
    def get_case_lines(self):
        lines = self.opera.get_lines()
        if lines == "":
            return None
        else:
            return lines
    
    def get_method(self, row):
        method = self.opera.get_value(row, 3)
        if method == "":
            return None
        else:
            return method

    def get_element(self, row):
        element = self.opera.get_value(row, 4)
        if element == '':
            return None
        else:
            return element
        
    def get_handle_value(self, row):
        handle_value = self.opera.get_value(row, 5)
        if handle_value == "":
            return None
        else:
            return handle_value
        
    def get_except(self, row):
        value = self.opera.get_value(row, 6)
        if value == "":
            return None
        else:
            print(value)
            return value
        
    def get_except_handle(self, row):
        value = self.opera.get_value(row, 7)
        if value == "":
            return None
        else:
            return value   
        
    def write_value(self, i, row, line, value):
        self.opera.read_excel()
        self.opera.write_value(i, row, line, value)
        
    
if __name__ =='__main__':
    get = GetExcel(8)
    print(get.get_element(3))
    print(get.get_except_handle(3))