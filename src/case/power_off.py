# -*- coding: utf-8 -*-
'''
Created on 2019年3月22日

@author: uidq1501
'''
import serial
import time
import threading
import cv2
from skimage.measure import compare_ssim
import subprocess
import os

ser1 = serial.Serial("COM4",115200,bytesize=8)
ser2 = serial.Serial('COM6',9600,bytesize=8)
PIC1 = cv2.imread(r"../main_word/except6.png")
PIC2 = cv2.imread(r"../main_word/except5.png")
PIC3 = cv2.imread(r"../main_word/except4.png")

setPowerControl = 'AA002001000000000000000000000000000000000000000000CB'#设置电源控制
setPowerON = 'AA002101000000000000000000000000000000000000000000CC'#打开电源
setPowerOFF = 'AA002100000000000000000000000000000000000000000000CB' #关闭电源 
setPower0mV = 'AA002300000000000000000000000000000000000000000000CD' #设置0v电压
setPower6800mV = 'AA00237017000000000000000000000000000000000000000054' #设置6v电压
setPower12000mV = 'AA0023E02E0000000000000000000000000000000000000000DB'#设置12v电压
touch_key = 'input tap 150 600'
power_on_key = 'vndservice call display.qservice 15 i32 0 i32 1 i32 1'
n = 0

def check_ser(ser):
    if ser.isOpen() :
        return ser
    else :
        print("power open failed")
 
def savelog(log):
    with open('D:/logtime.txt','a')as f:
        f.write(log)
     
def Start_Thread(t):
    thread = threading.Thread(target = t)
    thread.setDaemon(True)
    thread.start()  

def power_on():
    print ('准备重启')
    ser2.write(setPowerControl.decode('hex'))
    time.sleep(1)
    ser2.write(setPower6800mV.decode('hex'))
    time.sleep(8)
    ser2.write(setPower12000mV.decode('hex'))
    

def toch(ser1):
    ser1.write('input tap 1200 600\r\n')
    time.sleep(2)
    for i in range(8):
        ser1.write(touch_key+'\r\n')
        time.sleep(0.5)
        
def start_enter():
    print('正在开机')
    time.sleep(70)
    ser1.write('\r\n')
    time.sleep(0.5)
    ser1.write('su\r\n')
    time.sleep(0.5)    
    ser1.write(power_on_key+'\r\n')
    print('发了')
    toch(ser1)
        
    
def canara_picture(): 
    time.sleep(3)
    cap = cv2.VideoCapture(1) 
    n = 0 
    while(1):#连续捕捉
        n+=1
        time.sleep(3)
        ret,frame = cap.read()#cap.read()会返回一个结果
#         if not ret: 
#             continue#解决官方程序报错的关键，因为很多摄像头返回的第一帧都无效
        time.sleep(1)
        cv2.imwrite(os.getcwd()+"/match.png",frame)
        a = os.path.getsize(os.getcwd()+"/match.png")
        print(a)
        b = 300000
        if int(a) < b:
            pass
        else:
            break
#     cap.release()#释放摄像头 
#     cv2.destroyAllWindows()

def compare_image(imageA, imageB):
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    (score, diff) = compare_ssim(grayA, grayB, full=True)
    print("SSIM: {}".format(score))
    return score
        
def ser_write_key():
    print('车机已经重启')
    time.sleep(25)
    print('开始拍照截图')
    canara_picture()                 
    time.sleep(2)
    match_PIC = cv2.imread(os.getcwd()+"/match.png")
    time.sleep(1)
    m = compare_image(PIC1,match_PIC)
#             print m
    k = compare_image(PIC2,match_PIC)
#             print n     
    s = compare_image(PIC3,match_PIC)
#             print s       
    if m > 0.75 or k>0.8 or s>0.8:
        ser1.write('adb devices\r\n')
        ser1.write('adb devices\r\n')

    else:
#                 os.system("cd D:/BT_auto_test/report/G5_android/match && del screenshot.png")
        ser1.write('2>&1 | tee logcat.txt\r\n')
        time.sleep(1)
        ser1.write('dumpsys SurfaceFlinger 2>&1 | tee SurfaceFlinger.txt\r\n')
        time.sleep(1)
        ser1.write('dumpsys display > dumpdisplay.txt\r\n')   


def main():
        n = 0
        if ser1.isOpen():
            while True:
                if ser1.inWaiting() > 0:
                    data = ser1.readline()
                    Start_Thread(savelog(time.asctime()+data)) 
#                     print (data)                    
                    if data.find(r"Jumping to kernel via monitor") != -1:
                        Start_Thread(start_enter)
                    elif data.find(r"Result: Parcel(NULL)") != -1:
                        n+= 1
                        print('第'+str(n)+'次测试') 
                        Start_Thread(ser_write_key)
                    elif data.find(r"adb devices") != -1:
                        Start_Thread(power_on)
                    elif data.find(r"dumpsys display > dumpdisplay.txt") != -1:
                        break            
                else:
                    time.sleep(0.01)
        else:
            print('ser is closed, then opened sucessfully, but now is closed again.')
#     ser2.write(setPower6800mV.decode('hex'))
#     time.sleep(8)
#     n =0
#     while True:
#         power_on(ser2)
#         if ser1.inWaiting() > 0:
#             data = ser1.readline()
#             Start_Thread(savelog(time.asctime()+data)) 
#             n += 1
#             print('第'+str(n)+'次测试')
#             time.sleep(70)
#             ser1.write(power_on_key+'\r\n')
#             toch(ser1)
#             print '车机已经重启'      
#             time.sleep(20)
#             print '开始拍照截图'
#             canara_picture()                 
#             time.sleep(2)
#             match_PIC = cv2.imread(os.getcwd()+"/match.png")
#             time.sleep(1)
#             m = compare_image(PIC1,match_PIC)
# #             print m
#             k = compare_image(PIC2,match_PIC)
# #             print n     
#             s = compare_image(PIC3,match_PIC)
# #             print s       
#             if m > 0.83 or k>0.83 or s>0.83:
#                 ser2.write(setPower6800mV.decode('hex'))
#                 time.sleep(8)
# 
#             else:
# #                 os.system("cd D:/BT_auto_test/report/G5_android/match && del screenshot.png")
#                 ser1.write('2>&1 | tee logcat.txt\r\n')
#                 time.sleep(1)
#                 ser1.write('dumpsys SurfaceFlinger 2>&1 | tee SurfaceFlinger.txt\r\n')
#                 time.sleep(1)
#                 ser1.write('dumpsys display > dumpdisplay.txt\r\n')   
#                 break
                        
if __name__ == "__main__":
#     ser_write_key()
    main()
    
    
    

    







