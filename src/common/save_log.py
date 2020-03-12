# -*- coding: utf-8 -*-
'''
Created on 2018年11月21日

@author: uidq1501
'''
import sys
import serial
import time
import util.log_confige as log
import traceback
import threading

ser = serial.Serial("COM4", 115200, bytesize=8)

def ser_write(ser_cmd):
    return ser.write(ser_cmd.encode('utf-8'))

def Start_Thread(t):
    thread = threading.Thread(target=t)
    thread.setDaemon(True)
    thread.start()
    
def savelog(log):
    with open('D:/logtime.txt', 'a+')as f:
        f.write(log)

def rvc_test():
    try:
        time.sleep(20)
        ser_write('\r\n')
        time.sleep(3)
        ser_write('root\r\n')
        log.logging.info('journalctl | grep weston')
        ser_write('root\r\n')        
        log.logging.info('journalctl | grep weston  done')  
    except:
        log.logging.info('Power reboot for only tell you there is an Exception')
        log.logging.info(traceback.format_exc())
        
def input():
    ser_write('ipconfig\r\n')

        
def log():
    if ser.isOpen():
        while (1):
            if ser.inWaiting() > 0:
                data = ser.readline().decode("utf-8", "ignore").strip()
                Start_Thread(savelog(data)) 
                print(data)
                if data.find(r"Normal boot") != -1:
                    Start_Thread(rvc_test)
                elif data.find(r"g6s login:") != -1:
                    ser_write('root\r\n')
                elif data.find(r"Password") != -1:
                    ser_write('root\r\n')    
                elif data.find(r"root@g6s") != -1:
                    Start_Thread(input)                                   
            else:
                time.sleep(0.01)
    else:
        log.logging.info('ser is closed, then opened sucessfully, but now is closed again.')


if __name__ == "__main__":
    log()
#     event = threading.Event()
#     event.set()
        