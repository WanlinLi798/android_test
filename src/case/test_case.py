# -*- coding: utf-8 -*-
'''
@author: uidq1501
'''

import unittest
import HTMLTestRunner
import time
import multiprocessing
from util.server import Server
from util.write_user_command import WriteUserCommand
from business.source_switch_business import SourceBusiness

class parameTestcase(unittest.TestCase):
    def __init__(self,methodName='runTest',parame=None):
        super(parameTestcase,self).__init__(methodName)
        global parames
        parames = parame

class CaseTest(parameTestcase):
    @classmethod
    def setUpClass(cls):
        print 'this is setUpClass---->',parames
        cls.SourceBusiness = SourceBusiness(parames)

    def setUp(self):
        print 'this is setup\n'

    def test_case_1(self):
        print 'test case1'
       # flag = True
       # self.assertEquals("1","1",'数据错误')
       # self.assertTrue(flag)
       # @unittest.skip("CaseTest")
       #  self.SourceBusiness.local_music()
        self.SourceBusiness.BT_switch()
        self.SourceBusiness.USB_audio_switch()

    def test_case_2(self):
        n = 0
        # print 'this is case2'
        # self.assertNotEquals("1","2",'fei数据错误')
        while(n<10):
            n+=1
            self.SourceBusiness.USB_audio_switch()


    def tearDown(self):
        time.sleep(1)
        print 'this is teardown\n'

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        print 'this is class teardown\n'


def get_suite(i):
    print 'get_suite里面的',i
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_case_1",parame=i))
    suite.addTest(CaseTest("test_case_2",parame=i))
    html_file = r"D:\Users\uidq1501\eclipse-workspace\android_test\src\report\report"+str(i)+".html"
    fp = file(html_file,'wb')
    HTMLTestRunner.HTMLTestRunner(fp).run(suite)

def get_count():
    write_user_file = WriteUserCommand()
    count = write_user_file.get_file_lines()
    return count

def appium_init():
    server = Server()
    server.main()

if __name__ == '__main__':
    appium_init()
    threads = []
    for i in range(get_count()):
        print i
        t = multiprocessing.Process(target=get_suite,args=(i,))
        threads.append(t)
    for j in threads:
        j.start()
