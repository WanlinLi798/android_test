# -*- coding: utf-8 -*-
'''
@author: uidq1501
'''
import threading

def sum(a):
    print a+6
threads = []
for i in range(3):
    # print i
    t = threading.Thread(target=sum,args=(i,))
    threads.append(t)
for j in threads:
    j.start()