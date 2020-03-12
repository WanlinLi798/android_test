# -*- coding: utf-8 -*-
'''
Update on 2020年2月18日

@author: uidp4235
'''
import time
import os.path
from common.read_config import ReadIni

timeinfo=time.strftime('%y%m%d_%H_%M')
path =r'D:\BT_auto_test\report'

class Create_folder:
    def Create(self, parameter):
        try:
            project_name = ReadIni().get_value('key', 'get_name')
            # 获取项目名
            make_path = path+"\\"+project_name+"\\"+parameter+"\\"+timeinfo
            os.makedirs(make_path)
            # 一次建立多层目录
            ImagePath = os.path.join(make_path+'\\')
            # print"test"
            return ImagePath
        except:
            #traceback.print_exc()
            ImagePath = os.path.join(path+"\\"+parameter+'\\')
            # print ImagePath
            return ImagePath
            pass

