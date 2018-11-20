# -*- coding: utf-8 -*-
'''
Created on 2018年11月2日

@author: uidq1501
'''
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


class Android_test(unittest.TestCase):
    def setup(self):
        print 'this is setup'
    
    def testcase1(self):
        run = Runmain()
        run.runmain(0)
                 
    def teardown(self):
        print 'this is teardown'
     
                                   
def get_count():
    write_user_file = WriteUserCommand()
    count = write_user_file.get_file_lines()
    return count

def get_suite(i):
    print 'get_suite里面的'
    suite = unittest.TestSuite()
    suite.addTest(Android_test("testcase1"))
#     suite.addTest(Android_test("test_case_02", parame=i))
    unittest.TextTestRunner().run(suite)
    html_file = r"D:\Users\uidq1501\eclipse-workspace\android_test\src\report\report"+str(i)+".html"
    fp = file(html_file,'wb')
    HTMLTestRunner.HTMLTestRunner(fp).run(suite)
    
         
       
if __name__ =='__main__':
    threads = []
    for i in range(get_count()):
        print i
    t = threading.Thread(target=get_suite,args=(i,))
    threads.append(t)
    for t in threads:
        t.start()