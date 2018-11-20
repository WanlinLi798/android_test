# -*- coding: utf-8 -*-
'''
Created on 2018年11月12日

@author: uidq1501
'''
import sys
import tkinter.ttk
from tkinter import scrolledtext
import time
import queue
import serial 
import threading
import tkinter as tk
from tkinter import *
 
isOpened = threading.Event()
RQueue = queue.Queue(maxsize=1024)
TQueue = queue.Queue(maxsize=1024)
 
root = tk.Tk()
ComX = tk.StringVar(root,'COM5')
Baud = tk.StringVar(root,"115200")
Dbit = tk.StringVar(root,'8')
Sbit = tk.StringVar(root,'1')
Chck = tk.StringVar(root,'None')
Enty = tk.StringVar(root,'root')
HexD = tk.BooleanVar(root,False)
HexO = tk.BooleanVar(root,False)
Open = tk.StringVar(root,u'打开串口')
Policy =tk.StringVar()

# iptables 策略列表，可进行修改
Policy=('root',
'iptables -nvL',
'iptables -F;iptables -X;iptables -L'
'iptables -P INPUT DROP;iptables -N SECURITY_CHECK;iptables -A INPUT -j SECURITY_CHECK;iptables -L',
'iptables -P INPUT ACCEPT;iptables -N SECURITY_CHECK;iptables -A INPUT -j SECURITY_CHECK;iptables -L',
'iptables -A SECURITY_CHECK -i lo -s 127.0.0.1 -d 127.0.0.1 -j ACCEPT',
'iptables -A SECURITY_CHECK -i lo -j ACCEPT',
'iptables -A SECURITY_CHECK -m state --state INVALID -j DROP',
'iptables -A SECURITY_CHECK -m state --state ESTABLISHED,RELATED -j ACCEPT',
'iptables -A SECURITY_CHECK -p icmp -j DROP',
'QQMusic_Car_TCPPort=43997;QQMusic_Car_ReqPort=43955;QQMusic_Car_ResPort=43959',
'iptables -A SECURITY_CHECK -p tcp --syn \! --dport $QQMusic_Car_TCPPort -j DROP',
'iptables -A SECURITY_CHECK -p tcp --syn --dport $QQMusic_Car_TCPPort -m connlimit --connlimit-above 1 --connlimit-mask 0 -j DROP',
'iptables -A SECURITY_CHECK -p tcp --syn --dport $QQMusic_Car_TCPPort -j ACCEPT',
'iptables -A SECURITY_CHECK -p UDP -m state --state NEW --dport $QQMusic_Car_ReqPort -j ACCEPT',
'iptables -A SECURITY_CHECK -p UDP -m state --state NEW --dport $QQMusic_Car_ResPort -j ACCEPT',
'iptables -A SECURITY_CHECK -p all -m state --state NEW -m recent --name port_scan --update --second 60 --hitcount 30 -j DROP',
'iptables -A SECURITY_CHECK -p all -m state --state NEW -m recent --name port_scan --set -j ACCEPT')
 
class test:
    def main(self):
        root.title("iptables 策略测试")
        root.geometry('1500x930+50+50')
        
        self.txt1 = tk.scrolledtext.ScrolledText(root,width=200,height=50,border=5,font =18)
        self.txt1.pack(side='top',padx=3,pady=1,anchor='w')
        
        cnv1 = tk.Canvas(root,height=30,width=1200)
        cnv1.pack(side='top',padx=0,pady=0,anchor='w')
        cnv1.create_window(40,15,window=tkinter.ttk.Label(root,text=u'输入框：'))
        cnv1.create_window(500,15,window=tkinter.ttk.Combobox(root,textvariable=Enty,values = Policy,width=120))
        cnv1.create_window(1000,15,window=tkinter.ttk.Button(root,text=u'发送',width=9,command=lambda:TQueue.put(Enty.get())))
        cnv1.create_window(1100,15,window=tkinter.ttk.Button(root,text=u'清除',width= 9,command=lambda:self.txt1.delete('1.0','end')))
        # cnv1.create_window(547,15,window=tkinter.ttk.Checkbutton(root,text=u'HEX显示',variable=HexD,onvalue=True,offvalue=False,command=lambda:HEXDProc(txt1)))
        
        cnv2 = tk.Canvas(root,height=30,width=580)
        cnv2.pack(side='top',padx=0,pady=0,anchor='w')
        cnv2.create_window( 40,15,window=tkinter.ttk.Label(root,text=u'串口号：'))
        cnv2.create_window(120,15,window=tkinter.ttk.Combobox(root,textvariable=ComX,values=['COM1', 'COM2', 'COM3','COM4','COM5','COM6','COM7','COM8'],width=12))
        cnv2.create_window(202,15,window=tkinter.ttk.Label(root,text=u'波特率：'))
        cnv2.create_window(277,15,window=tkinter.ttk.Combobox(root,textvariable=Baud,values=['4800','9600','115200'],width=12))
        cnv2.create_window(398,15,window=tkinter.ttk.Button(root,textvariable=Open,width=16,command=lambda:COMOpen(cnv2)))
        cnv2.create_oval(470,7,486,23,fill='black',tag='led')
        # cnv2.create_window(547,15,window=tkinter.ttk.Checkbutton(root,text=u'HEX发送',variable=HexO,onvalue=True,offvalue=False,command=lambda:Enty.set(''.join('%02X' %i for i in [ord(c) for c in Enty.get()])) if HexO.get() else Enty.set(''.join([chr(int(i,16)) for i in [Enty.get()[i*2:i*2+2] for i in range(0,len(Enty.get())/2)]]))))
        
        cnv3 = tk.Canvas(root,height=10,width=580)
        cnv3.pack(side='top',padx=0,pady=0,anchor='w')
        cnv3.create_window( 40,15,window=tkinter.ttk.Label(root,text=u'数据位：'))
        cnv3.create_window(120,15,window=tkinter.ttk.Combobox(root,textvariable=Dbit,values=['9','8','7','6','5'],width=12))
        cnv3.create_window(202,15,window=tkinter.ttk.Label(root,text=u'停止位：'))
        cnv3.create_window(277,15,window=tkinter.ttk.Combobox(root,textvariable=Sbit,values=['1','2'],width=12))
        cnv3.create_window(370,15,window=tkinter.ttk.Label(root,text=u'校验位：'))
        cnv3.create_window(445,15,window=tkinter.ttk.Combobox(root,textvariable=Chck,values=['None','Odd','Even','Mark','Space'],width=12))
        cnv3.create_window(547,15,window=tkinter.ttk.Button(root,text=u'扩展',width=9))
    
        com_thread = threading.Thread(target=COMTrce)
        com_thread.setDaemon(True)
        com_thread.start()

        root.bind("<<COMRxRdy>>",lambda e:self.txt1.insert("insert", ''.join('%02X' %i for i in [ord(c) for c in RQueue.get()]) if HexD.get() else RQueue.get()))
        self.txt1.bind('<<modified>>',modified)   
        root.mainloop()
    
    # def HEXDProc(txt1):
    #     if HexD.get():
    #         s = txt1.get('1.0','end')
    #         s = ''.join('%02X' %i for i in [ord(c) for c in s])
    #         txt1.delete('1.0','end')
    #         txt1.insert("insert",s)
    #     else:
    #         s = txt1.get('1.0','end')
    #         s = ''.join([chr(int(i,16)) for i in [s[i*2:i*2+2] for i in range(0,len(s)/2)]])
    #         txt1.delete('1.0','end')
    #         txt1.insert("insert",s)
        
                
    self.COM = serial.Serial()
    def COMOpen(self,cnv2):
        if not isOpened.isSet():
            try:
                self.COM.timeout = 1
                self.COM.xonxoff = 0   
                self.COM.port = ComX.get()
                self.COM.parity = Chck.get()[0]
                self.COM.baudrate = int(Baud.get())
                self.COM.bytesize = int(Dbit.get())
                self.COM.stopbits = int(Sbit.get())
                COM.open()
            except Exception:
                print ('COM Open Error!')
            else:
                isOpened.set()
                Open.set(u'关闭串口')
                cnv2.itemconfig('led',fill='green')
        else:
            COM.close()
            isOpened.clear()
            Open.set(u'打开串口')
            cnv2.itemconfig('led',fill='black')
    
    def COMTrce(self):
        while True:
            if isOpened.isSet():
                rbuf = COM.read(1)          #read one, with timout
                if rbuf:
                    n = COM.inWaiting()
                    if n:
                        rbuf = rbuf+COM.read(n)
                        RQueue.put(rbuf)
                        root.event_generate("<<COMRxRdy>>")
                        
                if not TQueue.empty():
                    command = str(TQueue.get()).encode('utf-8') + b"\r\n"
                    COM.write(command)

    def modified(self):
        self.txt1.see(END)

if __name__=='__main__':
    isOpened.clear()
    main()

