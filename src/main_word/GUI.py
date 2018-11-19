# -*- coding: utf-8 -*-
'''
Created on 2018年11月14日

@author: uidq1501
'''
from Tkinter import *
import tkMessageBox
import os
from Runmain import Runmain
import threading
import time

# class MyThread(threading.Thread):
#  
#     def __init__(self, func, args):
#         threading.Thread.__init__(self)
#         self.func = func
#         self.args = args
# 
#     def run(self):
#         self.func(*self.args)

class Application():
#     def __init__(self,master=None):
#         Frame.__init__(self, master)
#         self.pack() 
#         self.creatWidgets()
        
    def __init__(self,master):
        fm1 = Frame(master,bg='white')
        self.helloLable = Label(fm1, text='简易自动化工具',font=('宋体',36,"bold"),fg = 'blue',bg='white' )
        self.helloLable.pack()
        fm1.pack(side=TOP,fill=BOTH,pady=2,padx=2)
        
        fm2 = Frame(master)
        self.openButton = Button(fm2, text='打开case',height=3,width=12,command=self.openexcel)  
        self.openButton.pack(pady=22)
        self.startButton = Button(fm2, text='开始测试',fg = 'green',height=3,width=12,command=self.start)  
        self.startButton.pack(pady=42)
        self.quitButton = Button(fm2, text='停止并退出',fg = 'red',height=3,width=12,command=self.stop)  
        self.quitButton.pack(pady=30)
        fm2.pack(side=LEFT,fill=BOTH,pady=2,padx=2)
        
        fm3 = Frame(master)
        self.setButton = Button(fm3, text='设置对比图片',height=1,width=16,command=self.PIC)  
        self.setButton.place(x=50)       
        self.nameinput = Entry(fm3)
        self.nameinput.pack() 
        self.commitButton = Button(fm3, text='确定',height=1,width=4,command=self.queding)  
        self.commitButton.place(x=360)  
#         self.scroll = Scrollbar(fm3)
#         self.scroll.pack(side=RIGHT,fill=Y)
#         self.logshow = Text(fm3)
#         self.logshow.pack(pady=10)
#         self.scroll.config(command=self.logshow.yview)
#         self.logshow.config(yscrollcommand=self.scroll.set)
        self.scroll = Scrollbar(fm3)
        self.scroll.pack(side=RIGHT, fill=Y)
#         s2 = Scrollbar(fm3, orient=HORIZONTAL)
#         s2.pack(side=BOTTOM, fill=X)
        self.logshow = Text(fm3, yscrollcommand=self.scroll.set,wrap='none')
        self.logshow.pack(expand=YES,pady=10)
        self.scroll.config(command=self.logshow.yview)
#         s2.config(command=textpad.xview)
        fm3.pack(side=BOTTOM,fill=BOTH,pady=2,padx=2)
                        
    def openexcel(self):
        os.system(r'..\config\case.xls')
        
    def starting(self):
        run = Runmain()
        run.runmain()
        
    def start(self):
        threads=[]
        f = threading.Thread(target=self.logo)
        threads.append(f)        
        t = threading.Thread(target=self.starting)
        threads.append(t)
        for t in threads:
            t.setDaemon(True)
            t.start()
        for t in threads:
            t.join()
#             self.threads = []
#             t = threading.Thread(target=self.starting)
#             f = threading.Thread(target=self.readfile)
#             self.threads.append(t)
#             self.threads.append(f)
#             for j in self.threads:
#                 j.start()
    
    def stop(self):
        os.system('taskkill -F -PID node.exe')  
        sys.exit(1)    
        
    def logo(self):
        os.system("python test1.py")
        
        
    def PIC(self):
        tkMessageBox.showinfo('Message', '如果要对比多个图片，请在标记图片后，在右边的方框命名，并在Excel中填上对应的名称，图片加载需要几秒钟，不要走开！' )
        os.system("python drow_ROI.py")
                
    def queding(self):
        name = self.nameinput.get()
        os.rename(os.path.join(os.getcwd(),'screenshot.png'),os.path.join(r'D:\BT_auto_test\report\G5_android',name+".jpg"))
#     def hello(self):
#         name = self.nameinput.get() or 'pengfy'
#         tkMessageBox.showinfo('Message', 'Hello,%s' %name)
        

root =Tk()
root.title('厉害')
display = Application(root)
root.mainloop()



