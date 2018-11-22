# -*- coding: utf-8 -*-
'''
Created on 2018年11月2日

@author: uidq1501
'''
from util.desired_setting import BaseDriver
from util.use_driver import GetByLocal
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os
from util.write_user_command import WriteUserCommand
import math
from PIL import Image
import operator
import yaml
import cv2
import util.log_save as log

path =os.path.abspath(os.path.dirname(os.getcwd()))+'\error_screenshot'


class ActionMethod():
    
    def __init__(self):
        base_driver = BaseDriver()
        self.driver = base_driver.desired_setting(0)
        self.WebDriverWait = WebDriverWait
        self.EC = EC
        self.By = By
        self.get = GetByLocal(self.driver,self.WebDriverWait,self.EC,self.By)
        self.WF = WriteUserCommand()
              
    def click(self,*args):
        try:
            log.logging.info('开始点击'+str(args[0]))
            element = self.get.get_element(args[0])
            element.click()
        except Exception:
#         if element == None:
            log.logging.info(str('Fail:  '+args[0])+'元素没有找到......')
            tm = time.strftime("%Y%m%d_%H%M%S")
            path1 = os.path.join(path,tm+args[0]+'.png')
 
            self.driver.get_screenshot_as_file(path1)
            quit()
#         element.click()
        
    def click_home(self):
        self.driver.keyevent(3)
        
    def click_menu(self):
        udid = self.WF.get_value('user_info_'+str(0),'deviceName')
        os.system('adb -s '+udid+' shell input tap 640 563')
        
    def sleep(self,*args):
        time.sleep(int(args[0]))
        
    def click_player(self):
        udid = self.WF.get_value('user_info_'+str(0),'deviceName')
        os.system('adb -s '+udid+' shell input tap 404 648')
#         os.system('adb -s 00001234 shell input tap 404 648')
            
    
    def get_element(self,*args):
        return self.get.get_element(args[0])
    
    def check(self,*args):
        try:
            element = self.get.get_element(args[0])
            return element
        except :
#             if element == None:
            print '元素没有找到......'
            tm = time.strftime("%Y%m%d_%H%M%S")
            path1 = os.path.join(path,tm+args[0]+'.png')

            self.driver.get_screenshot_as_file(path1)

    
    def picture_match(self,pic,row):
        tm = time.strftime("%Y%m%d_%H%M%S")
        PIC = Image.open(os.getcwd()+"/"+pic+".png")
        self.driver.get_screenshot_as_file('file.png')
        match =  Image.open('file.png')
        h1 = PIC.histogram()
        h2 = match.histogram()
        differ = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1))
        if differ > 1000:
            os.rename(os.path.join(os.getcwd(),'file.png'),os.path.join(path,tm+str(row)+".png"))
            return None
        return differ
        
    def ROI_picture_match(self,pic,row):
        tm = time.strftime("%Y%m%d_%H%M%S")
        image_path = os.getcwd()+"/"+pic+".png"
        srcImg  = cv2.imread(image_path)
        self.driver.get_screenshot_as_file('filename.png')
        match =  cv2.imread('filename.png')
        
        with open(os.getcwd()+'/ROI.yaml') as f:
            data = yaml.load(f) 
            roi = data['key'+pic]
        img_roi  = srcImg[roi['iy']:(roi['iy']+roi['y']),roi['ix']:(roi['ix']+roi['x'])]  
        match_roi = match[roi['iy']:(roi['iy']+roi['y']),roi['ix']:(roi['ix']+roi['x'])]
        cv2.imwrite(os.getcwd()+"/img_roi.png",img_roi) 
        cv2.imwrite(os.getcwd()+"/match_roi.png",match_roi)  
        PIC_roi = Image.open(os.getcwd()+"/img_roi.png")
        match_roi =  Image.open(os.getcwd()+"/match_roi.png") 
        h1 = PIC_roi.histogram()
        h2 = match_roi.histogram()
        differ = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1))
        if differ > 10:
            os.rename(os.path.join(os.getcwd(),'filename.png'),os.path.join(path,tm+str(row)+".png"))
            print differ
            return None
        return h2            

if __name__ =='__main__':      
    action = ActionMethod()
    action.ROI_picture_match('BT',1)
    

            
             
        
        