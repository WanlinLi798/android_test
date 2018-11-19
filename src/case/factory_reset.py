# -*- coding: utf-8 -*-
'''
@author: uidq1501
'''
from business.source_switch_business import SourceBusiness
from page.source_switch_page import Source_Page
import time
import os
import serial
from util.create_log_folder import Create_folder
from PIL import Image
from util.server import Server
import math  #对比图片使用
import operator
import subprocess


class Factory_reset():
    def __init__(self,n):
        self.load_PIC = Create_folder().Create('match')
        self.ser = serial.Serial("COM4",115200,bytesize=8)
        self.PIC = Image.open(r"D:\BT_auto_test\report\G5_android\factory_reset\except.png")
#         self.match_PIC = Source_Page(0).get_screenshot(load_PIC+str(n)+'.png')
#         self.match = Source_Page(0).same_as(self.PIC,self.match_PIC)

    def test_case(self):
        n=0
        while (n<1000):
            n+=1
            print '第'+str(n)+'次测试'
            appium_init()
            SourceBusiness(0).factory_reset()
            appium_stop()
            start_time = time.time()
            while (1):
                self.ser.write('setprop persist.sv.debug.adb_enable 1\r\n')
                time.sleep(1)
                self.ser.write('adbdctl start\r\n')
                time.sleep(1)
                result = os.popen('adb devices').readlines()
                print '2'
                end_time = time.time()
                total_time = int(end_time) - int(start_time)
                if len(result) >= 3:
#                     self.ser
                    self.ser.write('setprop persist.sv.debug_logcat 2\r\n')
                    self.ser.write('setprop persist.sv.debug_sysinfo 1\r\n')
                    self.ser.write('setprop persist.sys.sv.debug_service 1\r\n')
#                     time.sleep(1)
#                     self.ser.close()
                    appium_init()
                    subprocess.call('adb kill-server') 
                    time.sleep(5)       
                    subprocess.call('adb start-server')            
                    time.sleep(60)
                    subprocess.call('adb shell /system/bin/screencap -p /storage/usb1/screenshot.png')
                    time.sleep(1)
                    cmd1 = "cd D:/BT_auto_test/report/G5_android/match"
                    cmd2 = "adb pull /storage/usb1/screenshot.png"
                    cmd = cmd1 + " && " + cmd2
                    subprocess.call(cmd,shell=True)
                    time.sleep(3)
                    subprocess.call("adb shell rm /storage/usb1/screenshot.png")                   
                    self.match_PIC = Image.open(r"D:/BT_auto_test/report/G5_android/match/screenshot.png")
                    time.sleep(1)
                    M = same_as(self.PIC,self.match_PIC)
                    print M
                    if M >1000:
                        exit()
                    else:
                        os.system("cd D:/BT_auto_test/report/G5_android/match && del screenshot.png")
                        break
                elif total_time > 120:
                    print '死机'
                    exit()
                    
def appium_init():
    server = Server()
    server.main()
    
def appium_stop():
    server = Server()
    server.kill_server()

def same_as(image1,image2):
    h1 = image1.histogram()
    h2 = image2.histogram()

    differ = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1))
    return differ


if __name__ == '__main__' :
    appium_init()
    Factory_reset(0).test_case()

