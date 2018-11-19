# -*- coding: utf-8 -*-
'''
Created on 2018.10.22

@author: uidq1501
'''
from appium import webdriver
import time
from util.write_user_command import WriteUserCommand
 
class BaseDriver:
    def desired_setting(self,i):
        self.WF = WriteUserCommand()
        udid = self.WF.get_value('user_info_'+str(i),'deviceName')
        port = self.WF.get_value('user_info_'+str(i),'port')
        desired_caps = {
            #udid adb devices
          "platformName": "Android",
          "platformVersion": "8.1.0",
          "deviceName": "android",
          "udid": udid,
          "noReset": 'true',#不重复安装APP
          'app':r'D:\qqmusic.apk',
          "appWaitActivity": "com.tencent.qqmusic.activity.baseactivity.PermissionActivity",     
#           "appActivity": ".activity.AppStarterActivity",
#           "appPackage": "com.tencent.qqmusic",
          # "appActivity": "com.desaysv.hmi.SvSettings",
          # "appPackage": "com.android.settings",
          'newCommandTimeout': '300',
    #       "automationName":"UIAutomator2"
        }
        driver = webdriver.Remote("http://127.0.0.1:"+port+"/wd/hub",desired_caps)
        time.sleep(10)
        return driver
    
if __name__ == '__main__' :
    BaseDriver().desired_setting(0)