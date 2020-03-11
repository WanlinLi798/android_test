# -*- coding: utf-8 -*-
'''
@author: uidq1501
'''
from business.source_switch_business import SourceBusiness
import time
import os
import serial
from common.create_log_folder import Create_folder
from driver.server import Server
import subprocess
import cv2
import numpy as np
from skimage.measure import compare_ssim

class Factory_reset():
    def __init__(self,n):
        self.load_PIC = Create_folder().Create('match')
        self.ser = serial.Serial("COM4",115200,bytesize=8)
        self.PIC = cv2.imread(r"../main_word/except1.png")
#         self.match_PIC = Source_Page(0).get_screenshot(load_PIC+str(n)+'.png')
#         self.match = Source_Page(0).same_as(self.PIC,self.match_PIC)

    def test_case(self):
        n=0
        while (n<1000):
            n+=1
            print('第'+str(n)+'次测试')
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
                print(result)
                print('2')
                end_time = time.time()
                total_time = int(end_time) - int(start_time)
                if '00001234\tdevice\n' in result :
#                 if len(result) >= 3 :
#                     self.ser
                    self.ser.write('setprop persist.sv.debug_logcat 2\r\n')
                    self.ser.write('setprop persist.sv.debug_sysinfo 1\r\n')
                    self.ser.write('setprop persist.sys.sv.debug_service 1\r\n')
#                     time.sleep(1)
#                     self.ser.close()
                    print('重启appium')
                    appium_init()
                    subprocess.call('adb kill-server') 
                    time.sleep(5)       
                    subprocess.call('adb start-server')            
                    time.sleep(200)
                    print('开始拍照截图')
                    canara_picture()                 
                    time.sleep(2)
                    self.match_PIC = cv2.imread(os.getcwd()+"/match.png")
                    time.sleep(1)
#                     M = same_as(self.PIC,self.match_PIC)
#                     print M
                    hash1 = pHash(self.PIC)
                    hash2 = pHash(self.match_PIC)
                    m= cmpHash(hash1, hash2)
                    print(m)
                    if m >30:
#                         appium_stop()
                        exit()

                    else:
                        os.system("cd D:/BT_auto_test/report/G5_android/match && del screenshot.png")
                        break
                elif total_time > 180:
                    print('死机')
#                     appium_stop()
                    exit()

                    
def appium_init():
    server = Server()
    server.main()
    
def appium_stop():
    server = Server()
    server.kill_server()

# def same_as(image1,image2):
#     gray1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
#     gray2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
#     h1 = gray1.histogram()
#     h2 = gray2.histogram()
# 
#     differ = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1))
#     return differ

# 感知哈希算法(pHash)
def pHash(img):
    # 缩放32*32
    img = cv2.resize(img, (640, 480))  # , interpolation=cv2.INTER_CUBIC
#     img = cv2.imread(img)
    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 将灰度图转为浮点型，再进行dct变换
    dct = cv2.dct(np.float32(gray))
    # opencv实现的掩码操作
    dct_roi = dct[0:8, 0:8]

    hash = []
    avreage = np.mean(dct_roi)
    for i in range(dct_roi.shape[0]):
        for j in range(dct_roi.shape[1]):
            if dct_roi[i, j] > avreage:
                hash.append(1)
            else:
                hash.append(0)
    return hash

# Hash值对比
def cmpHash(hash1, hash2):
    n = 0
    # hash长度不同则返回-1代表传参出错
    if len(hash1)!=len(hash2):
        return -1
    # 遍历判断
    for i in range(len(hash1)):
        # 不相等则n计数+1，n最终为相似度
        if hash1[i] != hash2[i]:
            n = n + 1
    return n

# 通过得到RGB每个通道的直方图来计算相似度
def classify_hist_with_split(image1, image2, size=(256, 256)):
    # 将图像resize后，分离为RGB三个通道，再计算每个通道的相似值
    image1 = cv2.resize(image1, size)
    image2 = cv2.resize(image2, size)
    sub_image1 = cv2.split(image1)
    sub_image2 = cv2.split(image2)
    sub_data = 0
    for im1, im2 in zip(sub_image1, sub_image2):
        sub_data += calculate(im1, im2)
    sub_data = sub_data / 3
    return sub_data

# 计算单通道的直方图的相似值
def calculate(image1, image2):
    hist1 = cv2.calcHist([image1], [0], None, [256], [0.0, 255.0])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0.0, 255.0])
    # 计算直方图的重合度
    degree = 0
    for i in range(len(hist1)):
        if hist1[i] != hist2[i]:
            degree = degree + (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
        else:
            degree = degree + 1
    degree = degree / len(hist1)
    return degree


def canara_picture():
    time.sleep(2)
    cap = cv2.VideoCapture(1)  
    while(1):#连续捕捉
        ret, frame = cap.read()#cap.read()会返回一个结果
        if not ret: 
            continue#解决官方程序报错的关键，因为很多摄像头返回的第一帧都无效

        time.sleep(1)
        cv2.imwrite(os.getcwd()+"/match.png", frame)
        a = os.path.getsize(os.getcwd()+"/match.png")
        b = 200000
        if int(a) < b:
            pass
        else:
            break
    cap.release()#释放摄像头 
    cv2.destroyAllWindows()
    
def compare_image(imageA, imageB):
# 
#     imageA = cv2.imread(path_image1)
#     imageB = cv2.imread(path_image2)
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    (score, diff) = compare_ssim(grayA, grayB, full=True)
    print("SSIM: {}".format(score))
    return score


if __name__ == '__main__' :
#     appium_init()
#     Factory_reset(0).test_case()
#     canara_picture()
    print(os.getcwd()+"\test3.png")
    img1 = cv2.imread(r"../main_word/test2.png")
    img2 = cv2.imread("test3.png")
    compare_image(img1,img2)
#     hash1 = pHash(img1)
#     hash2 = pHash(img2)
#     n = cmpHash(hash1, hash2)
#     print n
#     a = os.path.getsize(os.getcwd()+"/match.png")
#     print a
