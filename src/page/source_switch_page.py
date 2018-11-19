# -*- coding: utf-8 -*-
'''
Created on 2018年10月22日

@author: uidq1501
'''
from util.use_driver import GetByLocal
from util.desired_setting import BaseDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# import math  #对比图片使用
# import operator
# from PIL import Image
# import os
# import time


class Source_Page:
    # 获取登录页面所有的页面元素信息
    def __init__(self,i):
        base_driver = BaseDriver()
        self.driver = base_driver.desired_setting(i)
        self.WebDriverWait = WebDriverWait
        self.EC = EC
        self.By = By
        self.get_by_local = GetByLocal(self.driver,self.WebDriverWait,self.EC,self.By)

    def get_BT_element(self):
        '''
        获取BT source元素信息
        '''
        try:
            return self.get_by_local.get_element('BT')
        except Exception:
            self.get_by_local.PIC('BT')
            print '没有找到该元素或该元素不可点击'
    def get_menu_element(self):
        '''
        获取menu元素信息
       '''
        # try:
        return self.driver.find_element_by_xpath('//android.widget.TextView[@content-desc="应用"]')
        # except Exception:
        #     self.get_by_local.PIC('menu')
        #     print '没有找到该元素或该元素不可点击'
        
    def get_player_element(self):
        '''
        获取menu元素信息
        '''
        try:
            return self.get_by_local.get_element('player')
        except Exception:
            self.get_by_local.PIC('player')
            print '没有找到该元素或该元素不可点击'
    
    def get_music_hall_element(self):
        '''
        获取music_hall元素信息
        '''
        try:
            return self.get_by_local.get_element('music_hall')
        except Exception:
            self.get_by_local.PIC('music_hall')
            print '没有找到该元素或该元素不可点击'
    
    def get_USB_audio_element(self):
        '''
        获取USB_audio元素信息
        '''
        try:
            return self.get_by_local.get_element('USB_audio')
        except Exception:
            self.get_by_local.PIC('USB_audio')
            print '没有找到该元素或该元素不可点击'
    
    def home(self):
        self.driver.keyevent(3)

    def local_music(self):
        try:
           return self.get_by_local.get_element('local_music')
        except Exception:
            self.get_by_local.PIC('local_music')
            print '没有找到该元素或该元素不可点击'

    def get_my_icon(self):
        try:
           return self.get_by_local.get_element('my_icon')
        except Exception:
            self.get_by_local.PIC('my_icon')
            print '没有找到该元素或该元素不可点击'

    def get_back(self):
        try:
           return self.get_by_local.get_element('back')
        except Exception:
            self.get_by_local.PIC('back')
            print '没有找到该元素或该元素不可点击'

    def get_find(self):
        try:
           return self.get_by_local.get_element('find')
        except Exception:
            self.get_by_local.PIC('find')
            print '没有找到该元素或该元素不可点击'

    def get_setting(self):
        try:
           return self.get_by_local.get_element('setting')
        except Exception:
            self.get_by_local.PIC('setting')
            print '没有找到该元素或该元素不可点击'

    def get_system(self):
        try:
           return self.get_by_local.get_element('system')
        except Exception:
            self.get_by_local.PIC('system')
            print '没有找到该元素或该元素不可点击'

    def get_factory_reset(self):
        try:
           return self.get_by_local.get_element('factory_reset')
        except Exception:
            self.get_by_local.PIC('factory_reset')
            print '没有找到该元素或该元素不可点击'

    def get_confirm(self):
        try:
            return self.get_by_local.get_element('confirm')
        except Exception:
            self.get_by_local.PIC('confirm')
            print '没有找到该元素或该元素不可点击'

#     def get_screenshot(self,path):
#         self.driver.get_screenshot_as_file(path)
# 
#     def same_as(self,image1,image2):
#         # image1 = Image.open(path1)
#         # image2 = Image.open(path2)
# 
#         h1 = image1.histogram()
#         h2 = image2.histogram()
# 
#         differ = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1))
#         return differ

    def quit(self):
        self.driver.quit()


if __name__ == '__main__' :
    page = Source_Page(0)
    print page.get_menu_element()
