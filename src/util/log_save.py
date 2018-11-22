# -*- coding: utf-8 -*-
'''
Created on 2018年10月22日

@author: uidq1501
'''
import time
import logging

path =r'..\report'

now = time.strftime('%Y-%m-%M-%H_%S',time.localtime(time.time()))
logging.basicConfig(level=logging.INFO,
#                 format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                format='%(asctime)s %(levelname)s %(message)s',
                datefmt='%y%m%d_%H:%M:%S',
                filename= path+'\\report.txt',
                filemode='w')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)