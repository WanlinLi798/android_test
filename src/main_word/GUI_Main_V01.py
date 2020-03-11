# -*- coding: utf-8 -*-
'''
Update on 2020年2月19日

@author: uidp4235
'''
from tkinter import *
from tkinter import ttk
# import ttk
import tkinter
import tkinter.messagebox
import os
from tkinter.scrolledtext import ScrolledText
import threading
# from ScrolledText import ScrolledText  Mei Xiu20200108
import yaml
import tkinter.filedialog as filedialog
import cv2
from driver.server import Server
from testcase import GenerateTestCases
from common.drow_ROI import DrawROI
from common.common_param import InitParam

class Application:
    def __init__(self, master, starttest, editcase):
        self.CheckVar1 = IntVar()
        self.CheckVar2 = IntVar()
        self.CheckVar3 = IntVar()
        Label(master, text='安卓自动化测试系统', font=('宋体', 20, "bold"), fg='blue').grid(row=0, column=0, rowspan=2, columnspan=8)
        Button(master, height=4, width=12, text="编辑case", command=editcase).grid(row=2, column=0, rowspan=2)
        Button(master, height=4, width=12, text="选择case", command=self.choosecase).grid(row=4, column=0, rowspan=2)
        Button(master, height=4, width=12, text="开始测试", command=starttest).grid(row=6, column=0, rowspan=2)
        Button(master, height=4, width=12, text="停止当前case", command=self.stop).grid(row=8, column=0, rowspan=2)
        Button(master, height=1, width=30, text="设置对比图片", command=self.PIC).grid(row=2, column=1, columnspan=2, padx=10)
        Button(master, height=1, width=12, text='摄像头截图', command=self.CAM).grid(row=2, column=4, sticky=W, padx=10)
        Button(master, height=1, width=16, text="查看问题截图", command=self.openerror).grid(row=2, column=6)
        Button(master, height=1, width=16, text="清空截图信息", command=self.clearPIC).grid(row=2, column=7)
        Button(master, text="全屏图片名称确认", command=self.queding).grid(row=3, column=2, sticky=W, padx=5)
        Button(master, text="ROI图片名称确认", height=1, width=16, command=self.ROIqueding).grid(row=3, column=4, sticky=W, padx=5)
        
        number1 = tkinter.StringVar()
        self.numberChosen1 = ttk.Combobox(master, width=12, textvariable=number1, state='readonly')
        self.numberChosen1['values'] = self.devices_list()  # 设置下拉列表的值
        self.numberChosen1.grid(column=7, row=3)  # 设置其在界面中出现的位置 column代表列 row 代表行
#         self.numberChosen1.current(0) # 设置下拉列表默认显示的值，0为numberChosen['values'] 的下标值
        
        number2 = tkinter.StringVar()
        self.numberChosen2 = ttk.Combobox(master, width=12, textvariable=number2, state='readonly')
        self.numberChosen2['values'] = (0, 1, 2, 3)  # 设置下拉列表的值
        self.numberChosen2.grid(column=3, row=2, sticky=E)  # 设置其在界面中出现的位置 column代表列 row 代表行
        self.numberChosen2.current(0)  # 设置下拉列表默认显示的值，0为numberChosen['values'] 的下标值

        self.nameinput1 = Entry(master)
        self.nameinput1.grid(row=3, column=1, sticky=E, padx=5)
        self.nameinput2 = Entry(master)
        self.nameinput2.grid(row=3, column=3, sticky=E, padx=5)
        self.logshow = ScrolledText(master, font=('宋体', 16, "bold"), fg='red')
        self.logshow.grid(row=4, column=1, columnspan=7, rowspan=6, sticky=W+E+N+S, padx=5, pady=5)
        
#     def ReceiveData(self):
        with open(r'..\report\report.txt') as f:
            while True:
                line = f.readline()
#                 self.logshow.grid()
                self.logshow.insert(END, line)
                self.logshow.see(END)
                self.logshow.update()
    
    def devices_list(self):
        list = Server().get_device() 
        return list
    
    def PIC(self):
        tkinter.messagebox.showinfo('Message', '如果要对比多个图片，请在标记图片后，在右边的方框命名，并在Excel中填上对应的名称，图片加载需要几秒钟，不要走开！' )
        # os.system("python drow_ROI.py")
        DrawROI()
        
    def CAM(self):
        tkinter.messagebox.showinfo('Message', '如果要对比多个图片，请在标记图片后，在右边的方框命名，并在Excel中填上对应的名称，图片加载需要几秒钟，不要走开！' )
        os.system("python use_camara.py")
                
    def queding(self):
        name1 = self.nameinput1.get()
        print(name1)
        name_list = os.listdir(InitParam()._screenshotpath)
        if name1+'.png' in name_list:
            tkinter.messagebox.showinfo('Error', '图片名字冲突，请重命名')
        else:
            os.rename(os.path.join(os.path.abspath(os.path.dirname(os.getcwd())) + '\screenshot', "screenshot.png"), os.path.join(os.path.abspath(os.path.dirname(os.getcwd())) + '\screenshot', name1+".png"))
                 
    def ROIqueding(self):
        name2 = self.nameinput2.get()
        print(name2)
        with open(InitParam().roi_yaml_filepath, 'r+') as fr:
            data = yaml.load(fr)
            y1 = data['key']['iy']
            x1 = data['key']['ix']
            y = data['key']['y']
            x = data['key']['x']
            data1 = {
                'key'+name2: {
                    "ix": x1,
                    "iy": y1,
                    "x": x,
                    "y": y,
                    }  
                }
            yaml.dump(data1, fr)
        os.rename(os.path.join(InitParam()._screenshotpath, 'screenshot.png'), os.path.join(InitParam()._screenshotpath + '\ROI\\', name2+".png"))
            
    def openerror(self):
        filename = filedialog.askopenfilename(title='打开问题图片', initialdir='../error_screenshot', filetypes=[('png', '*.png'), ('All Files', '*')] )
        print(filename)
        image = cv2.imread(filename)
        cv2.imshow('image', image)
        
    def openreport(self):
        filename = filedialog.askopenfilename(title='打开内存测试报告', initialdir='../report', filetypes=[('csv', '*.csv'), ('All Files', '*')] )
        os.system(filename)


    def del_files(self,path):
        for root, dirs, files in os.walk(path):
            for name in files:
                if name.endswith(".png"):   #指定要删除的格式，这里是png 可以换成其他格式
                    os.remove(os.path.join(root, name))

    def clearPIC(self):
        with open(InitParam().roi_yaml_filepath, 'w') as fr:
            fr.truncate()    
        fr.close()
        self.del_files('../main_word')
        
    def choosecase(self):
        # get = Getcase()
        # get.setcase()
        os.system("python select_testcase.py")

    def stop(self):
        os.system('taskkill -F -PID node.exe')  
        sys.exit(1)     


class ThreadClient:
    
    def __init__(self, master):
        self.gui = Application(master, self.start, self.openfile)  # 将我们定义的GUI类赋给服务类的属性，将执行的功能函数作为参数传入
        self.master = master

    def starting(self):
        GenerateTestCases()
        # os.system("python ../main_word/testcase.py")
        # run = Runmain()
        # run.runmain(1)

    def openexcel(self):
        os.system(r'..\config\case.xls')  
        
    def openfile(self):
        b = threading.Thread(target=self.openexcel)
        b.daemon = True
        # b = myThread(self.openexcel, 'openfile', 2)
        b.start()
    
    def start(self):
        with open(r'..\report\report.txt', 'w') as f:
            f.truncate()
        t = threading.Thread(target=self.starting)
        t.daemon = True
        # t = myThread(self.starting, 'startest', 1)
        t.start()

def MyThread(t):
    thread = threading.Thread(target=t)
    thread.setDaemon(True)
    thread.start()

def callback():
    tkinter.messagebox.showwarning('警告', '确定退出吗？')
    root.destroy()


if __name__ =='__main__':
    root = Tk()
    root.title('安卓自动化测试系统')
    display = ThreadClient(root)
    root.mainloop()
