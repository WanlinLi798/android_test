# -*- coding: utf-8 -*-
'''
Created on 2018年11月16日

@author: uidq1501
'''
import time
from Tkinter import *
import threading

class MyThread(threading.Thread):
 
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)
 
 
def write(file1,file2):
    with open(file1, 'r+') as f1:
        for line in f1:
             # print line
           f2 = open(file2, 'a+')
           f2.write(line)
           time.sleep(0.00001)


def windows1(file2):
    root = Tk()
    root.title("serial log")
    s1 = Scrollbar(root)
    s1.pack(side=RIGHT, fill=Y)
    s2 = Scrollbar(root, orient=HORIZONTAL)
    s2.pack(side=BOTTOM, fill=X)
    textpad = Text(root, yscrollcommand=s1.set, xscrollcommand=s2.set, wrap='none')
    textpad.pack(expand=YES, fill=BOTH)
    s1.config(command=textpad.yview)
    s2.config(command=textpad.xview)
    with open(file2) as f:
        while True:
            line = f.readline()
            textpad.pack()
            textpad.insert(END, line)
            textpad.see(END)
            root.update()


if __name__ =='__main__':
    file1 = 'log.txt'
    file2 = r'D:\BT_auto_test\report\test_log.txt'
    threads = []
    t1 = MyThread(write, (file1,file2))
    threads.append(t1)
    t2 = MyThread(windows1,(file2,))
    threads.append(t2)
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()