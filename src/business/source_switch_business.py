# -*- coding: utf-8 -*-
'''
Created on 2018年10月22日

@author: uidq1501
'''
import os
import time
from handle.source_switch_handle import SourceHandle
from util.write_user_command import WriteUserCommand

class SourceBusiness:
    def __init__(self,i):
        self.handle = SourceHandle(i)
        self.WF = WriteUserCommand()
        
    def BT_switch(self):
        try:
            self.handle.home()
            time.sleep(1)
            udid = self.WF.get_value('user_info_'+str(0),'deviceName')
            os.system('adb -s '+udid+' shell input tap 404 648')
#             os.system('adb -s 00001234 shell input tap 404 648')
            print 11111
            self.handle.music_hall()
            self.handle.BT()
            time.sleep(5)
        except Exception:
            return False
            pass
    def USB_audio_switch(self):
        try:
#             self.handle.home()
#             os.system('adb -s 00001234 shell input tap 640 563')
# #             self.handle.menu()
#             self.handle.player()
            udid = self.WF.get_value('user_info_'+str(0),'deviceName')
            os.system('adb -s '+udid+' shell input tap 404 648')
#             os.system('adb -s 00001234 shell input tap 404 648')
            self.handle.music_hall()
            self.handle.USB_audio()
        except Exception:
            return False
            pass

    def local_music(self):
        self.handle.my_icon()
        self.handle.local_music()

    def go_find(self):
        self.handle.back()
        self.handle.find()

    def factory_reset(self):
        self.handle.home()
        time.sleep(5)
        udid = self.WF.get_value('user_info_'+str(0),'deviceName')
        os.system('adb -s '+udid+' shell input tap 640 563')
        print '进入设置界面'
        time.sleep(1)
        self.handle.setting()
        print '恢复出厂设置'
        self.handle.system()
        self.handle.factory_reset()
        self.handle.confirm()
        time.sleep(30)


if __name__ == '__main__' :
    SourceBusiness(0).factory_reset()
    # while(1):
    #   Server().kill_server()
    #   Server().start_server(0)
    #   time.sleep(10)
    #   print '444'
    #   SourceBusiness(0).factory_reset()
    #   start_time = time.time()
    #   print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    #   while(1):
    #       result = os.popen('adb devices').readlines()
    #       print result
    #       end_time = time.time()
    #       total_time = int(end_time) - int(start_time)
    #       # print total_time
    #       if len(result) >= 3:
    #           break
    #
    #       elif total_time > 20:
    #           print '死机'
    #           exit()




