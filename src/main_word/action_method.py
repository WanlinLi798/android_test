# -*- coding: utf-8 -*-
'''
Update on 2020年02月25日

@author: uidp4235
'''
from driver.desired_setting import BaseDriver
from driver.use_driver import GetByLocal
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By   # By类：定位元素
import os
from common.write_user_command import WriteUserCommand
import yaml
import cv2
import common.log_confige as log
import subprocess
from common.read_config import ReadIni
from skimage.measure import compare_ssim
from common.common_param import InitParam

path = InitParam()._errorshotpath

# path = os.path.abspath(os.path.dirname(os.getcwd()))+'\error_screenshot'

class ActionMethod():
    
    def __init__(self):
        base_driver = BaseDriver()
        self.driver = base_driver.desired_setting(0)
        self.WebDriverWait = WebDriverWait
        self.EC = EC
        self.By = By
        self.get = GetByLocal(self.driver, self.WebDriverWait, self.EC, self.By)
        self.WF = WriteUserCommand()
        self.read = ReadIni()
              
    def click(self, *args):
        try:
            log.logging.info('开始点击'+str(args[0]))
            element = self.get.get_element(args[0])
            element.click()
        except Exception:
          # if element == None:
            log.logging.info(str('Fail:  '+args[0])+'元素没有找到......')
            tm = time.strftime("%Y%m%d_%H%M%S")
            path1 = os.path.join(path, tm+args[0]+'.png')
            self.driver.get_screenshot_as_file(path1)
            quit()
#         element.click()

    def sound_check(self, n):
        creat_filename = open(self.read.get_value('key', 'write_labview_log'), 'w')
        creat_filename.write(str(n))
        creat_filename.flush()
        time.sleep(2)
        creat_filename.close()
        p = subprocess.Popen(r'sound_check.exe')
        p.wait()
        with open('Soundresult.txt', 'r') as f:
            lines = f.readlines()
            n = 0
            while(1):
                n += 1
                a_str = "".join(lines[-n:])
                if a_str.strip() != '':
                    break
            if 'OK' in a_str:
                print('666')
                return a_str
            else:
                print('777')
                return None

    def click_home(self):
        self.driver.keyevent(3)
        
    def click_menu(self):
        udid = self.WF.get_value('user_info_'+str(0), 'deviceName')
        os.system('adb -s '+udid+' shell input tap 640 563')
        
    def swipe_to_setting(self):
        udid = self.WF.get_value('user_info_'+str(0), 'deviceName')
        os.system('adb -s '+udid+' shell input swipe 931 669 400 669 1000')
        time.sleep(2)
        os.system('adb -s '+udid+' shell input swipe 931 669 400 669 1000')
        time.sleep(2)
        os.system('adb -s '+udid+' shell input tap 334 663')
        
    def repeat_ab(self, a, b):
        pass
        
    def sleep(self, *args):
        time.sleep(int(args[0]))
        
    def click_player(self):
        udid = self.WF.get_value('user_info_'+str(0), 'deviceName')
        os.system('adb -s '+udid+' shell input tap 404 648')
        # os.system('adb -s 00001234 shell input tap 404 648')

    def get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    def swipe_down(self):
        udid = self.WF.get_value('user_info_'+str(0), 'deviceName')
        # x1 = self.get_size()[0]/2
        # y1 = self.get_size()[1]/10
        # y = self.get_size()[1]/10*9
        os.system('adb -s '+udid+' shell input swipe 612 180 612 481 100')
        # self.driver.swipe(x1,y1,x1,y,int(s))
        
    def swipe_up(self, s1):
        x1 = self.get_size()[0]/2
        y = self.get_size()[1]/10
        y1 = self.get_size()[1]/10*7
        self.driver.swipe(x1, y1, x1, y, int(s1))

    def get_element(self, *args):
        return self.get.get_element(args[0])
    
    def check(self, *args):
        try:
            element = self.get.get_element(args[0])   # 获取界面元素ID
            return element
        except :
            # if element == None:
            print('元素没有找到......')
            tm = time.strftime("%Y%m%d_%H%M%S")
            path1 = os.path.join(path, tm+args[0]+'.png')

            self.driver.get_screenshot_as_file(path1)
            # quit()    # Mei Xiu 20200225注释，不注释会导致后面Case不执行

    def picture_match(self, pic, row):
        tm = time.strftime("%Y%m%d_%H%M%S")
        PIC = cv2.imread(path + pic +".png")
        self.driver.get_screenshot_as_file('file.png')
        match = cv2.imread('file.png')
        
        grayA = cv2.cvtColor(PIC, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(match, cv2.COLOR_BGR2GRAY)
    
        (score, diff) = compare_ssim(grayA, grayB, full=True)
        print("SSIM: {}".format(score))
        if score < 0.95:
            os.rename(os.path.join(os.getcwd(), 'file.png'), os.path.join(path, tm+str(row)+".png"))
            return None
        return score

#         h1 = PIC.histogram()
#         h2 = match.histogram()
#         differ = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1))
#         if differ > 1000:
#             os.rename(os.path.join(os.getcwd(),'file.png'),os.path.join(path,tm+str(row)+".png"))
#             return None
#         return differ
        
    def ROI_picture_match(self, pic, row):
        tm = time.strftime("%Y%m%d_%H%M%S")
        image_path = path + "/screenshot/" + pic + ".png"
        srcImg = cv2.imread(image_path)
        self.driver.get_screenshot_as_file('filename.png')
        match = cv2.imread('filename.png')
        
        with open(InitParam().roi_yaml_filepath) as f:
            data = yaml.load(f) 
            roi = data['key'+pic]
        img_roi = srcImg[roi['iy']:(roi['iy']+roi['y']), roi['ix']:(roi['ix']+roi['x'])]
        match_roi = match[roi['iy']:(roi['iy']+roi['y']), roi['ix']:(roi['ix']+roi['x'])]
        cv2.imwrite(os.getcwd()+"/img_roi.png", img_roi)
        cv2.imwrite(os.getcwd()+"/match_roi.png", match_roi)
        PIC_roi = cv2.imread(os.getcwd()+"/img_roi.png")
        match_roi = cv2.imread(os.getcwd()+"/match_roi.png")
        grayA = cv2.cvtColor(PIC_roi, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(match_roi, cv2.COLOR_BGR2GRAY)
    
        (score, diff) = compare_ssim(grayA, grayB, full=True)
        print("SSIM: {}".format(score))
        if score < 0.95:
            os.rename(os.path.join(os.getcwd(),'filename.png'),os.path.join(path,tm+str(row)+".png"))
            return None
        return score
#         h1 = PIC_roi.histogram()
#         h2 = match_roi.histogram()
#         differ = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1))
#         print differ
#         if differ > 0.1:
#             os.rename(os.path.join(os.getcwd(),'filename.png'),os.path.join(path,tm+str(row)+".png"))
#             print differ
#             quit()
#             return None
#         return h2            
    
    def camara_macth(self, pic, row):
        tm = time.strftime("%Y%m%d_%H%M%S")
        PIC = cv2.imread(os.getcwd()+"/"+pic+".png")
        self.driver.get_screenshot_as_file('file.png')
        match =  cv2.imread('file.png')
        grayA = cv2.cvtColor(PIC, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(match, cv2.COLOR_BGR2GRAY)
    
        (score, diff) = compare_ssim(grayA, grayB, full=True)
        print("SSIM: {}".format(score))
        if score < 0.95:
            os.rename(os.path.join(os.getcwd(), 'file.png'), os.path.join(path, tm+str(row)+".png"))
            return None
        return score

        
if __name__ =='__main__':      
    action = ActionMethod()
    action.sound_check(10)
#     action.ROI_picture_match('BT',1)