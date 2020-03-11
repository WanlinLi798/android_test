# -*- coding: utf-8 -*-
'''
Update on 2020年02月25日

@author: uidp4235
'''
import cv2
import numpy as np
import subprocess
import time
import os
import yaml
from common.common_param import InitParam


class DrawROI:
    def __init__(self):
        self.drawing = False  # true if mouse is pressed
        self.mode = True  # 如果是True, 就画矩形. 键盘按 'm' 键就切换到曲线
        self.ix, self.iy = -1, -1
        subprocess.call('adb shell /system/bin/screencap -p /data/local/tmp/screenshot.png')
        time.sleep(1)
        cmd1 = 'cd ' + InitParam()._screenshotpath
        # cmd1 = "cd "+ os.path.abspath(os.path.dirname(os.getcwd())) + '/screenshot'
        cmd2 = "adb pull /data/local/tmp/screenshot.png"
        cmd = cmd1 + " && " + cmd2
        print(cmd)
        subprocess.call(cmd, shell=True)
        time.sleep(3)
        print(InitParam()._screenshotpath + '\\' + InitParam()._defaultpicname)
        self.img = cv2.imread(InitParam()._screenshotpath + '\\' + InitParam()._defaultpicname)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', self.draw_circle)
        subprocess.call("adb shell rm /data/local/tmp/screenshot.png")
        while(1):
            cv2.imshow('image', self.img)
            k = cv2.waitKey(1) & 0xFF
            if k == ord('m'):  # 切换模式
                self.mode = not self.mode
            elif k == 27:   # Mei Xiu 20200225 esc键ASCII值为27,按ESC键退出
                break
        cv2.destroyAllWindows()

    # 鼠标回调函数
    def draw_circle(self, event, x, y, flags, param):
        # global ix, iy, drawing, mode  # 指定这些变量为全局变量
        if event == cv2.EVENT_LBUTTONDOWN:  # 鼠标左键按下事件
            self.drawing = True
            self.ix, self.iy = x, y

        elif event == cv2.EVENT_MOUSEMOVE:  # 鼠标移动事件
            if self.drawing == True:
                if self.mode == True:
                    pass
                    # cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)#z注释后为不填充的矩形，不注释就是填充的
                else:
                    cv2.circle(self.img, (x, y), 5, (130, 66, 130), 1)

        elif event == cv2.EVENT_LBUTTONUP:  # 鼠标左键松开事件
            self.drawing = False
            if self.mode == True:
                cv2.rectangle(self.img, (self.ix, self.iy), (x, y), (0, 255, 0), 1)
                with open(InitParam().roi_yaml_filepath, 'a') as f:
                    data = {"key": {"ix": self.ix, "iy": self.iy, "x": x, "y": y, }}
                    yaml.dump(data, f)
                    f.close()
                print(self.ix, self.iy), (x, y)
            else:
                cv2.circle(self.img, (x, y), 5, (0, 0, 255), -1)

    def nothing(x):
        pass
