# -*- coding: utf-8 -*-
'''
Created on 2018年12月20日

@author: uidq1501
'''
import time
import os
import serial
from common.create_log_folder import Create_folder
import cv2
from skimage.measure import compare_ssim
import subprocess
from appium import webdriver
import threading

ser = serial.Serial("COM4",115200,bytesize=8)

class Factory_reset():
    def __init__(self):
        self.load_PIC = Create_folder().Create('match')
#         self.ser = serial.Serial("COM3",115200,bytesize=8)
        self.PIC = cv2.imread(r"../main_word/except1.png")
        self.desired_caps = {
          "platformName": "Android",
          "platformVersion": "8.1.0",
          "deviceName": "android",
          "udid": '00001234',
          "noReset": 'true',#不重复安装APP
    #           'app':r'D:\qqmusic.apk',
    #           "appWaitActivity": "com.tencent.qqmusic.activity.baseactivity.PermissionActivity",     
    #           "appActivity": ".activity.AppStarterActivity",
    #           "appPackage": "com.tencent.qqmusic",
        "appActivity": ".MainActivity",
        "appPackage": "com.desaysv.dlnadmr",
          'newCommandTimeout': '300',
        }

    def test_case(self):
        n=0
        Start_Thread(log)
        while (n<1000):
            n+=1
            print('第'+str(n)+'次测试')
            Start_Thread(appium_init)
            print('666')
            time.sleep(10)
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",self.desired_caps)
            self.driver.keyevent(3)
            time.sleep(2)
            subprocess.call('adb -s 00001234 shell input swipe 955 665 396 649 1000')
            subprocess.call('adb -s 00001234 shell input swipe 955 665 396 649 1000')
            time.sleep(1)
            subprocess.call('adb -s 00001234 shell input tap 504 655')
            time.sleep(1)
            self.driver.find_element_by_id('com.android.settings:id/sv_tab_system_id').click()
            time.sleep(2)
            self.driver.find_element_by_id('com.android.settings:id/layout_restore_factory').click()
            time.sleep(2)
            self.driver.find_element_by_id('com.android.settings:id/dialog_confirm').click()
            time.sleep(25)
            appium_stop()
            start_time = time.time()
            while (1):
                ser.write('setprop persist.sv.debug.adb_enable 1\r\n')
                time.sleep(1)
                ser.write('adbdctl start\r\n')
                time.sleep(1)
                result = os.popen('adb devices').readlines()
                print(result)
                print('2')
                end_time = time.time()
                total_time = int(end_time) - int(start_time)
                if '00001234\tdevice\n' in result :
#                 if len(result) >= 3 :
#                     self.ser
                    ser.write('setprop persist.sv.debug_logcat 2\r\n')
                    ser.write('setprop persist.sv.debug_sysinfo 1\r\n')
                    ser.write('setprop persist.sys.sv.debug_service 1\r\n')
#                     time.sleep(1)
#                     self.ser.close()
                    print('车机已经重启')
                    time.sleep(300)
                    print('开始拍照截图')
                    canara_picture()                 
                    time.sleep(2)
                    self.match_PIC = cv2.imread(os.getcwd()+"/match.png")
                    time.sleep(1)
                    m = compare_image(self.PIC,self.match_PIC)
                    print(m)
                    if m > 0.8:
                        appium_stop()
                        exit()

                    else:
                        os.system("cd D:/BT_auto_test/report/G5_android/match && del screenshot.png")
                        while (1):
                            ser.write('setprop persist.sv.debug.adb_enable 1\r\n')
                            time.sleep(1)
                            ser.write('adbdctl start\r\n')
                            time.sleep(1)
                            result = os.popen('adb devices').readlines()
                            print(result)
                            print('2')
                            end_time = time.time()
                            total_time = int(end_time) - int(start_time)
                            if '00001234\tdevice\n' in result:
                                break
                        break
                elif total_time > 600:
                    print('死机')
#                     appium_stop()
#                     exit()
                    
def appium_init():
    appium_stop()
    os.system('appium -p 4723 -bp 4724 -U 00001234 --no-reset --session-override')

#     webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
#     print '777'
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

def canara_picture():
    time.sleep(2)
    cap = cv2.VideoCapture(0) 
    n = 0 
    while(1):#连续捕捉
        n+=1
        print('第'+str(n)+'次拍照')
        ret,frame = cap.read()#cap.read()会返回一个结果
        if not ret: 
            continue#解决官方程序报错的关键，因为很多摄像头返回的第一帧都无效

        time.sleep(1)
        cv2.imwrite(os.getcwd()+"/match.png",frame)
        a = os.path.getsize(os.getcwd()+"/match.png")
        b = 200000
        if int(a) < b:
            pass
        else:
            break
    cap.release()#释放摄像头 
    cv2.destroyAllWindows()
    
def compare_image(imageA, imageB):
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    (score, diff) = compare_ssim(grayA, grayB, full=True)
    print("SSIM: {}".format(score))
    return score

def Start_Thread(t):
    thread = threading.Thread(target = t)
    thread.setDaemon(True)
    thread.start()
    
def savelog(log):
    with open('D:/logtime.txt','a+')as f:
        f.write(log)
        f.write('\n')   

def log():
    if ser.isOpen():
        a = time.asctime()
        while (1):
            if ser.inWaiting() > 0:
                data = ser.readline().decode("utf-8", "ignore").strip()
                Start_Thread(savelog(a+data))
                print(data)
    
if __name__ == '__main__' :
    desired_caps = {
      "platformName": "Android",
      "platformVersion": "8.1.0",
      "deviceName": "android",
      "udid": '00001234',
      "noReset": 'true',#不重复安装APP
#           'app':r'D:\qqmusic.apk',
#           "appWaitActivity": "com.tencent.qqmusic.activity.baseactivity.PermissionActivity",     
#           "appActivity": ".activity.AppStarterActivity",
#           "appPackage": "com.tencent.qqmusic",
        "appActivity": ".MainActivity",
        "appPackage": "com.desaysv.dlnadmr",
      'newCommandTimeout': '300',
    }
#     ser = serial.Serial("COM3",115200,bytesize=8)
    Factory_reset().test_case()


