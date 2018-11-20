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
from main_word.Runmain import Runmain


class MyTestCase(unittest.TestCase):
    
    def setup(self):
        print 'this is setup'

    def clear(self):
        print 'this is clear'

    def action(self,arg1,arg2):
        run = Runmain()
        run.runmain(int(arg2))
#     def action(self,arg1,arg2):
#         pass
    @staticmethod
    def getTestFunc(arg1,arg2):
        def func(self):
            self.action(arg1,arg2)
        return func

def __generateTestCases():
    arglists = [('arg11','0'),('arg21','1'),('arg31','2')]
    for args in arglists:
        setattr(MyTestCase, 'test_func_%s_%s'%(args[0],args[1]),MyTestCase.getTestFunc(*args))
__generateTestCases()

if __name__ =='__main__': 
    unittest.main()     
