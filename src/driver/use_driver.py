# -*- coding: utf-8 -*-
'''
Created on 2018.10.22

@author: uidq1501
'''
import time
from common.read_config import ReadIni
from common.create_log_folder import Create_folder

save_log = Create_folder().Create('source_switch_01')

class GetByLocal:
    def __init__(self, driver, WebDriverWait, EC, By):
        self.driver = driver
        self.Web = WebDriverWait
        self.EC = EC
        self.By = By
        
    def get_element(self, key):
        idOrXpath = ReadIni().get_value(key)
        if idOrXpath.startswith('/'):
            ret = self.Web(self.driver, 15).until(self.EC.element_to_be_clickable((self.By.XPATH, idOrXpath)))
        else:
            ret = self.Web(self.driver, 5).until(self.EC.element_to_be_clickable((self.By.ID, idOrXpath)))
        return ret 
    
    def PIC(self, name):
        tm = time.strftime("%Y%m%d_%H%M%S")
        save_pic =save_log+tm+name+'.png'
        self.driver.get_screenshot_as_file(save_pic)