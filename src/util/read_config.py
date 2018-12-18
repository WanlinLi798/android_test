# -*- coding: utf-8 -*-
'''
Created on 2018年10月22日

@author: uidq1501
'''
import ConfigParser
configpath = r'D:\Users\uidq1501\eclipse-workspace\android_test\src\config\config.ini'

class ReadIni:
    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path = configpath
        else:
            self.file_path = file_path
        self.data = self.read_ini()
 
    def read_ini(self):
        read_ini = ConfigParser.ConfigParser()
        read_ini.read(self.file_path)
        return read_ini
 
    #通过key获取对应的value
    def get_value(self,key,section=None):
        if section == None:
            section = 'G6S_common_element'
        try:
            value = self.data.get(section,key)  
                  
        except:
            value = None
        return value
 
if __name__ == '__main__':
    read_ini = ReadIni()
    print read_ini.get_value("key","write_labview_log")