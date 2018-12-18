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
import threading

drawing = False # true if mouse is pressed
mode = True # 如果是True, 就画矩形. 键盘按 'm' 键就切换到曲线
ix,iy = -1,-1
class Use_camana():
# 鼠标回调函数
    def draw_circle(self,event,x,y,flags,param):
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
                    cv2.circle(self.img,(x,y),5,(130,66,130),1)
    
        elif event == cv2.EVENT_LBUTTONUP:#鼠标左键松开事件
            drawing = False
            if mode == True:
                cv2.rectangle(self.img,(ix,iy),(x,y),(0,255,0),1)
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
                cv2.circle(self.img,(x,y),5,(0,0,255),-1)
    # Next we have to bind this mouse callback function to OpenCV # # window. In the main loop, we should set a keyboard binding for 
    # key ‘m’ to toggle between rectangle and circle.
    def nothing(self,x):
        pass
    
    
    
    def DrowROI(self):
        time.sleep(1)
        self.img = cv2.imread(os.getcwd()+"/screenshot.png")
        cv2.namedWindow('a')
        cv2.setMouseCallback('a',self.draw_circle)
        while(1):
            cv2.imshow('a',self.img)
            k = cv2.waitKey(1) & 0xFF
            if k == ord('m'): # 切换模式
                mode = not mode
            elif k == 27:
                break
        cv2.destroyAllWindows()
        
    def vedio(self):
        cap = cv2.VideoCapture(1)  
        while(1):#连续捕捉
            ret,frame = cap.read()#cap.read()会返回一个结果
            #第一个参数ret的值为TRUE/FALSE，代表没有读到图片
            #第二个参数是frame，是当前截取一帧的图片
            if not ret: continue#解决官方程序报错的关键，因为很多摄像头返回的第一帧都无效
        #     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#转换成灰度图
            cv2.imshow('cap',frame)
            if cv2.waitKey(1)&0xFF == 32:
                cv2.imwrite(os.getcwd()+"/screenshot.png",frame)
                Start_Thread(self.DrowROI)
            if cv2.waitKey(1)&0xFF == 27:
                cv2.imwrite(os.getcwd()+"/screenshot.png",frame)
                break
        cap.release()#释放摄像头 
        cv2.destroyAllWindows()
        
def Start_Thread(t):
    thread = threading.Thread(target = t)
    thread.setDaemon(True)
    thread.start()
if __name__=='__main__':
    use = Use_camana()
    use.vedio()

    