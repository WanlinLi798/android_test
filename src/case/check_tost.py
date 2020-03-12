# -*- coding: utf-8 -*-
'''
Update on 2020年2月18日

@author: uidp4235
'''
from appium import webdriver
import cv2
from skimage.measure import compare_ssim
import time
import os
import threading

class Check_pw():
 
    def check_pw(self):
        desired_caps = {
          "platformName": "Android",
          "platformVersion": "8.1.0",
          "deviceName": "android",
          "udid": '00001234',
          "noReset": 'true',#不重复安装APP
        "appActivity": ".MainActivity",
        "appPackage": "com.desaysv.dlnadmr",
          'newCommandTimeout': '300',
        }
        PIC = cv2.imread(r"../main_word/expect2.png")
        time.sleep(2)
        cap = cv2.VideoCapture(1) 
        n = 0
        Start_Thread(appium_init)
        time.sleep(5)
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        print(2)
        self.driver.keyevent(3)
        while(1):#连续捕捉
            
            time.sleep(2)
            n+=1
            print('第'+str(n)+'次拍照')
            ret,frame = cap.read()#cap.read()会返回一个结果
            if not ret: 
                continue#解决官方程序报错的关键，因为很多摄像头返回的第一帧都无效
            time.sleep(1)
            cv2.imwrite(os.getcwd()+"/match.png",frame)
            time.sleep(0.5)

            
            match_PIC = cv2.imread(os.getcwd()+"/match.png")
            b = compare_image(PIC,match_PIC)
            print(b)
            if b < 0.8:
                pass
            else:
                if (n % 2) == 0:
                    self.driver.find_element_by_id('com.android.settings:id/wifi_con_dialog_password').send_keys('12345678')
                    self.driver.find_element_by_id('com.android.settings:id/wifi_con_dialog_confirm').click()                            
                    print('密码已输入')
                    time.sleep(5)
                else:
                    pass
        cap.release()  # 释放摄像头
        cv2.destroyAllWindows()


def compare_image(imageA, imageB):
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    (score, diff) = compare_ssim(grayA, grayB, full=True)
    print("SSIM: {}".format(score))
    return score

def appium_init():
    appium_stop()
    os.system('appium -p 4723 -bp 4724 -U 00001234 --no-reset --session-override')


def appium_stop():
        command = 'tasklist | find "node.exe"'
        server_list = excute_cmd_result(command)
        if len(server_list)>0:
            excute_cmd('taskkill -F -PID node.exe')

def excute_cmd_result(command):
        result_list = []
        result = os.popen(command).readlines()
        for i in result:
            if i =='\n':
                continue
            result_list.append(i.strip('\n'))
        return result_list
    
def excute_cmd(command):
        os.system(command)

def Start_Thread(t):
    thread = threading.Thread(target=t)
    thread.setDaemon(True)
    thread.start()


if __name__ == '__main__' :
    check = Check_pw()
    check.check_pw()
