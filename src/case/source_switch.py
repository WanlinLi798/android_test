# coding=utf-8
'''
Created on 2018.10.22
@author: uidq1501
'''
# from business.source_switch_business import SourceBusiness
import unittest
import HTMLTestRunner
import time
import multiprocessing
from driver.server import Server
from common.write_user_command import WriteUserCommand
from business.source_switch_business import SourceBusiness
class ParameTestcase(unittest.TestCase):
    def __init__(self,methodName='runTest',parame=None):
        super(ParameTestcase, self).__init__(methodName)
        global parames
        parames = parame

class source(ParameTestcase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass---->', parames)
        cls.SourceBusiness = SourceBusiness(parames)

    def setUp(self):
        print('this is setup\n')

    def test_case_01(self):
        print('test case1里面的参数', parames)
        self.SourceBusiness.BT_switch()

    def test_case_02(self):
        print('this is case2')

    def tearDown(self):
        time.sleep(1)
        print('this is teardown\n')

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        print('this is class teardown\n')

def appium_init():
    server = Server()
    server.main()

def get_suite(i):
    print('get_suite里面的',i)
    suite = unittest.TestSuite()
    suite.addTest(source("test_case_01", parame=i))
    suite.addTest(source("test_case_02", parame=i))
    unittest.TextTestRunner().run(suite)
    html_file = r"D:\Users\uidq1501\eclipse-workspace\android_test\src\report\report"+str(i)+".html"
    fp = file(html_file, 'wb')
    HTMLTestRunner.HTMLTestRunner(fp).run(suite)

def get_count():
    write_user_file = WriteUserCommand()
    count = write_user_file.get_file_lines()
    return count

if __name__ == '__main__':
    appium_init()
    threads = []
    for i in range(get_count()):
        print(i)
        t = multiprocessing.Process(target=get_suite, args=(i,))
        threads.append(t)
    for j in threads:
        j.start()