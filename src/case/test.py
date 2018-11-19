# -*- coding: utf-8 -*-
'''
Created on 2018年10月31日

@author: uidq1501
'''
import os
import time
from util.create_log_folder import Create_folder
import math  #对比图片使用
import operator
from PIL import Image
import subprocess
import serial

# 
# subprocess.call('adb shell /system/bin/screencap -p /storage/usb1/screenshot.png')
# time.sleep(1)
# cmd1 = "cd D:/BT_auto_test/report/G5_android/match"
# cmd2 = "adb pull /storage/usb1/screenshot.png"
# cmd = cmd1 + " && " + cmd2
# subprocess.call(cmd,shell=True)
# time.sleep(1)
# subprocess.call("adb shell rm /storage/usb1/screenshot.png")    

import serial
import threading
import time

ser = serial.Serial("COM4",115200,bytesize=8)
ser.write("setprop persist.sv.debug.adb_enable 1\r\n")
print(ser.readline())
ser.close()


