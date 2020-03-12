# -*- coding: utf-8 -*-
'''
Update on 2020年02月25日

@author: uidp4235
'''
from appium import webdriver
import time
from common.write_user_command import WriteUserCommand
import common.log_confige as log
 
class BaseDriver:
    def desired_setting(self, i):
        self.WF = WriteUserCommand()
        udid = self.WF.get_value('user_info_'+str(i), 'deviceName')
        port = self.WF.get_value('user_info_'+str(i), 'port')
        desired_caps = {
                        # udid adb devices
                        "platformName": "Android",
                        "platformVersion": "8.1.0",
                        "deviceName": "android",
                        "udid": udid,
                        "noReset": 'true',  # 不重复安装APP
                        "appActivity": "com.desaysv.dsvsettings.MainActivity",   # 20200224 Mei Xiu，设置app activity名称
                        "appPackage": "com.desaysv.dsvsettings",    # 20200224 Mei Xiu 设置app包名
                        'newCommandTimeout': '300',
                        # "automationName":"UIAutomator2"
        }
        driver = webdriver.Remote("http://127.0.0.1:"+port+"/wd/hub", desired_caps)   # python运行时会跳转到app界面
        log.logging.info('APP界面初始化成功！')
        time.sleep(10)
        return driver


if __name__ == '__main__':
    BaseDriver().desired_setting(0)