# -*- coding: utf-8 -*-
'''
Created on 2018年11月19日

@author: uidq1501
'''
from tkinter import *
from common.opera_excel import OperaExcel
import tkinter.messagebox

class Getcase():
    def __init__(self):
        self.opera = OperaExcel()
        self.check_buttons = list()

    def setcase(self):
        self.sheet_name = self.opera.get_sheetname()
        self.sheet_num = len(self.sheet_name)
        print(self.sheet_name)
        print(self.sheet_num)
        self.root = Tk()
        self.root.title('case选项')
        self.root.geometry("500x"+str(self.sheet_num*4)+'0')
        for i in range(self.sheet_num):
            v = IntVar()
            txt = "case" + str(i+1)
            Checkbutton(self.root,text = "".join(self.sheet_name[i]),variable=v).pack(anchor='w')
            # 设置选项默认不选中
            v.set(1)
            # 将每个选项的对象信息存放在一个列表中
            self.check_buttons.append([v, txt])
        Button(self.root, text="选好了", command=self.get_checked_buttons).pack()      
        self.root.mainloop()

        return self.sheet_num

    def get_checked_buttons(self):
        checked = ""
        for each in self.check_buttons:
            if each[0].get() == 1:
                checked += each[1] + "  "
                tkinter.messagebox.showinfo(title="选中项为", message=checked)
        with open('result.txt', 'w') as f:
            f.write(checked)    
        self.root.quit()


if __name__ == '__main__':
    get = Getcase()
    get.setcase()