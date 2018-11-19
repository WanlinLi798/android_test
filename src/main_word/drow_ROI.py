# -*- coding: utf-8 -*-
'''
Created on 2018年11月12日

@author: uidq1501
'''
import cv2
import numpy as np
import subprocess
import time
import os
import yaml

drawing = False # true if mouse is pressed
mode = True # 如果是True, 就画矩形. 键盘按 'm' 键就切换到曲线
ix,iy = -1,-1

# 鼠标回调函数
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode#指定这些变量为全局变量

    if event == cv2.EVENT_LBUTTONDOWN:#鼠标左键按下事件
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:#鼠标移动事件
        if drawing == True:
            if mode == True:
                pass
                #cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),1)#z注释后为不填充的矩形，不注释就是填充的
            else:
                cv2.circle(img,(x,y),5,(130,66,130),-1)

    elif event == cv2.EVENT_LBUTTONUP:#鼠标左键松开事件
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),3)
            with open(os.getcwd()+'/ROI.yaml','a') as f:
                data = {
                    "key":{
                    "ix":ix,
                    "iy":iy,
                    "x":x,
                    "y":y,
                    }
                    }
                yaml.dump(data,f)               
                f.close()
            print (ix,iy),(x,y)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)
# Next we have to bind this mouse callback function to OpenCV # # window. In the main loop, we should set a keyboard binding for 
# key ‘m’ to toggle between rectangle and circle.
def nothing(x):
    pass


subprocess.call('adb shell /system/bin/screencap -p /data/local/tmp/screenshot.png')
time.sleep(1)
cmd1 = "cd "+os.getcwd()
cmd2 = "adb pull /data/local/tmp/screenshot.png"
cmd = cmd1 + " && " + cmd2
subprocess.call(cmd,shell=True)
time.sleep(3)
img = cv2.imread(os.getcwd()+"/screenshot.png")
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
subprocess.call("adb shell rm /data/local/tmp/screenshot.png")  
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'): # 切换模式
        mode = not mode
    elif k == 27:
        break
cv2.destroyAllWindows()


