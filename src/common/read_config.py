# -*- coding: utf-8 -*-


import configparser
configpath = r'..\config\config.ini'

class ReadIni:
    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = configpath
        else:
            self.file_path = file_path
        self.data = self.read_ini()
 
    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path, encoding='UTF-8')  # 2020-2-18 Mei Xiu Update
        return read_ini
 
    # 通过key获取对应的value
    def get_value(self, key, section=None):
        if section == None:
            section = 'G6S_common_element'
        try:
            value = self.data.get(section, key)
                  
        except:
            value = None
        return value


if __name__ == '__main__':
    read_ini = ReadIni()
    print(read_ini.get_value("key", "write_labview_log"))