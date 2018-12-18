# -*- coding: utf-8 -*-
'''
Created on 2018年11月20日

@author: uidq1501
'''
import unittest
# from test import test_support
from get_excel import GetExcel
from action_method import ActionMethod
from util.server import Server
from util.write_user_command import WriteUserCommand
import util.log_save as log
import time
import unittest
import HTMLTestRunner
import threading
from Runmain import Runmain
import re
import util.log_save as log


class MyTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        log.logging.info('***************请注意，测试开始***************')
        
    @classmethod
    def tearDownClass(cls):
        log.logging.info('***************请开心，所有case测试结束***************')
        
    def setUp(self):
        pass
    
    def clear(self):
        print 'this is clear'
        
    def tearDown(self):
        log.logging.info('******本条case测试结束******')

    def action(self,arg1):
        run = Runmain()
        run.runmain(int(arg1)-1)
#     def action(self,arg1,arg2):
#         pass
    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.action(arg1)
        return func

def __generateTestCases():
    arglists = []
    with open('result.txt') as f:
        data = f.readlines()
        arglists = re.findall(r"\d+\.?\d*",str(data[0]))
        
    for args in arglists:
        setattr(MyTestCase, 'test_func_%s'%(args),MyTestCase.getTestFunc(*args))
__generateTestCases()

if __name__ =='__main__': 
   unittest.main()
