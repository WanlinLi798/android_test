# -*- coding: utf-8 -*-
'''
Created on 2018年11月16日

@author: uidq1501
'''
from Tkinter import *
import Tkinter
import tkMessageBox
import os
from Runmain import Runmain
import threading
import time
from tkinter.scrolledtext import ScrolledText
import yaml
from tkinter import filedialog
import cv2
from tkinter import colorchooser


class MyThread(threading.Thread):
   
    def __init__(self, func):
        threading.Thread.__init__(self)
        self.func = func
#         self.args = args
  
    def run(self):
        self.func()
#         self.func(*self.args)


class Application():     
    def __init__(self,master,fuc,fuc1):
        Label(master,text='一键自动化',font=('宋体',36,"bold"),fg = 'blue',bg='white').grid(row=0,column=0,rowspan=2,columnspan=6)
        Button(master, height=4,width=12,text="编辑case",command=fuc1).grid(row=2,column=0,rowspan=2)
        Button(master, height=4,width=12,text="选择case",command=self.choosecase).grid(row=4,column=0,rowspan=2)
        Button(master, height=4,width=12,text="开始测试",command=fuc).grid(row=6,column=0,rowspan=2)
        Button(master, height=4,width=12,text="停止当前case",command=self.stop).grid(row=8,column=0,rowspan=2)
        Button(master, height=1,width=70,text="设置对比图片",command=self.PIC).grid(row=2,column=1,columnspan=3,sticky=E,padx=10)
        Button(master, height=1,width=16,text="查看测试报告").grid(row=2,column=4,sticky=W,padx=5)
        Button(master, height=1,width=16,text="查看问题截图",command = self.openerror).grid(row=2,column=5)
        Button(master, height=1,width=16,text="清空截图信息",command = self.clearPIC).grid(row=3,column=5)
        Button(master, text="全屏图片名称确认",command=self.queding).grid(row=3,column=2,sticky=W,padx=5)
        Button(master, text="ROI图片名称确认", height=1,width=16,command=self.ROIqueding).grid(row=3,column=4,sticky=W,padx=5)
        self.nameinput1 = Entry(master)
        self.nameinput1.grid(row=3,column=1,sticky=E,padx=5)
        self.nameinput2 = Entry(master)
        self.nameinput2.grid(row=3,column=3,sticky=E,padx=5)
        self.logshow = ScrolledText(master,font=('宋体',16,"bold"),fg='red')
        self.logshow.grid(row=4, column=1, columnspan=5, rowspan=6, sticky=W+E+N+S, padx=5, pady=5)
        with open(r'..\report\report.txt') as f:
            while True:
                line = f.readline()
                self.logshow.grid()
                self.logshow.insert(END, line)
                self.logshow.see(END)
                self.logshow.update()
        
    def PIC(self):
        tkMessageBox.showinfo('Message', '如果要对比多个图片，请在标记图片后，在右边的方框命名，并在Excel中填上对应的名称，图片加载需要几秒钟，不要走开！' )
        os.system("python drow_ROI.py")
                
    def queding(self):
        name1 = self.nameinput1.get()
        print name1
        os.rename(os.path.join(os.getcwd(),"screenshot.png"),os.path.join(os.getcwd(),name1+".png"))
        
    def ROIqueding(self):
        name2 = self.nameinput2.get()
        print name2
        with open("ROI.yaml",'r+') as fr:
            data = yaml.load(fr)
            y1 = data['key']['iy']
            x1 = data['key']['ix']
            y = data['key']['y']
            x = data['key']['x']
            data1 = {
                'key'+name2:{
                    "ix":x1,
                    "iy":y1,
                    "x":x,
                    "y":y,
                    }  
                }
            yaml.dump(data1,fr)
        os.rename(os.path.join(os.getcwd(),"screenshot.png"),os.path.join(os.getcwd(),name2+".png"))
            
    def openerror(self):
        filename = filedialog.askopenfilename(title='打开问题图片',initialdir = '../error_screenshot',filetypes=[('png', '*.png'), ('All Files', '*')] )
        print(filename)
        image = cv2.imread(filename)
        cv2.imshow('image',image)
        
#     def setlog(self):
# #         return 'red'
#         C = colorchooser.askcolor()
#         return str(C[1])

    def del_files(self,path):
        for root , dirs, files in os.walk(path):
            for name in files:
                if name.endswith(".png"):   #指定要删除的格式，这里是png 可以换成其他格式
                    os.remove(os.path.join(root, name))

    def clearPIC(self):
        with open("ROI.yaml",'w') as fr:
            fr.truncate()    
        fr.close()
        self.del_files('../main_word')
        
    def choosecase(self):
        os.system("python GUI_V04.py")

    def stop(self):
        os.system('taskkill -F -PID node.exe')  
        sys.exit(1)     
    
class ThreadClient():
    
    def __init__(self, master):
        self.master = master 
        self.gui = Application(master, self.start,self.openfile) #将我们定义的GUI类赋给服务类的属性，将执行的功能函数作为参数传入


    def starting(self):
        os.system("python test4.py")
#         run = Runmain()
#         run.runmain()
    def openexcel(self):
        os.system(r'..\config\case.xls')  
        
    def openfile(self):
        b = MyThread(self.openexcel)
        b.start()
        
        
    def start(self):
        with open(r'D:\BT_auto_test\report\test_log.txt','w') as f:
            f.truncate()
        threads = []
        t = MyThread(self.starting)
        threads.append(t)
        for t in threads:
            t.setDaemon(True)
            t.start()
               
if __name__ =='__main__':              
    root =Tk()
    root.title('厉害')
    display = ThreadClient(root)
    root.mainloop()
