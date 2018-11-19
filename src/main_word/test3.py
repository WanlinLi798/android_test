# -*- coding: utf-8 -*-
'''
Created on 2018年11月17日

@author: uidq1501
'''
import time
def windows1():
    with open(r'D:\BT_auto_test\report\test_log.txt') as f:
        while True:
            time.sleep(1)
            line = f.readline()
            print line

windows1()
