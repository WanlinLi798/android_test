# -*- coding: utf-8 -*-
'''
Created on 2018年11月20日

@author: uidq1501
'''
# import re
# import os
# import time
# import cv2
# # from util.create_log_folder import Create_folder
# # create_log_folder = Create_folder()
# # save_log = create_log_folder.Create('source_switch')
# # path =os.path.abspath(os.path.dirname(os.getcwd()))+'\error_screenshot'
# # path1 = save_log+'1.png' 
# # print path1
# # # def __generateTestCases():
# # #     arg = []
# # #     with open('result.txt') as f:
# # #         data = f.readlines()
# # #         print data
# # #         arg = re.findall(r"\d+\.?\d*",str(data[0]))
# # #         print arg
# # #         
# # # #         for i in data:
# # # #             print i
# # # #             n = re.sub("\D"," ",i)
# # # #             print n
# # # #         arg.append(n)
# # # # #         args = arg.extend(str(arg[0]))
# # # #         print arg
# # # # #         print args
# # # 
# # #     arglists = [('arg11','0'),('arg21','1'),('arg31','2')]
# # #     
# # # __generateTestCases()
# pic = 'BT'
# tm = time.strftime("%Y%m%d_%H%M%S")
# image_path = os.getcwd()+"/"+pic+".png"
# print image_path
# srcImg  = cv2.imread('D:\\Users\\uidq1501\\eclipse-workspace\\android_test\\src\\main_word\\BT.png')
# cv2.imshow('a',srcImg)
# cv2.waitKey(0)
# from Tkinter import *
# from tkinter.scrolledtext import ScrolledText
# 
# class App():
#     def __init__(self,master):
#     
# #     master = Tk()
#     # var = IntVar()
#         Label(master,text='一键自动化',font=('宋体',36,"bold"),fg = 'blue',bg='white').grid(row=0,column=0,rowspan=2,columnspan=5)
#         Button(master, height=4,width=12,text="编辑case").grid(row=2,column=0,rowspan=2)
#         Button(master, height=4,width=12,text="选择case").grid(row=4,column=0,rowspan=2)
#         Button(master, height=4,width=12,text="开始测试").grid(row=6,column=0,rowspan=2)
#         Button(master, height=4,width=12,text="停止当前case").grid(row=8,column=0,rowspan=2)
#         Button(master, height=1,width=24,text="设置对比图片").grid(row=2,column=1,columnspan=2)
#         Button(master, height=1,width=24,text="查看问题截图").grid(row=2,column=3,columnspan=2)
#         Button(master, text="全屏图片名称确认").grid(row=3,column=2)
#         Button(master, text="ROI图片名称确认").grid(row=3,column=4)
#         Entry(master).grid(row=3,column=1)
#         Entry(master).grid(row=3,column=3)
#         self.logshow = ScrolledText(master)
#         self.logshow.grid(row=4, column=1, columnspan=4, rowspan=6, sticky=W+E+N+S, padx=5, pady=5)
#         with open(r'D:\BT_auto_test\report\test_log.txt') as f:
#             while True:
#                 line = f.readline()
#                 self.logshow.insert(END, line)
#                 self.logshow.see(END)
#                 self.logshow.update()        
# class App2():
#     def __init__(self,master):
#         self.master = master
#         self.gui = App(master)
#         
# if __name__ =='__main__':   
#     root =Tk()
#     root.title('厉害')
#     display = App2(root)
#     root.mainloop()
#     
# #     mainloop()
import time
import chardet

def sound_check(n):
#     creat_filename = open(self.read.get_value('key','write_labview_log'),'w')
#     creat_filename.write(str(n))
#     creat_filename.flush()
#     time.sleep(2)
#     creat_filename.close()
#     p = subprocess.Popen(r'sound_check.exe')
#     p.wait()
        with open('Soundresult.txt','r') as f:
            lines = f.readlines()
            n=0
            while(1):
                n+=1
                a_str = "".join(lines[-n:])
                if a_str.strip()!='':
                    print a_str
                    break
            if 'OK' in a_str:
                print a_str
            else:
                print '77777'
            
sound_check(10)
