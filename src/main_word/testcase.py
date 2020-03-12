# -*- coding: utf-8 -*-
'''
Update on 2020年2月25日

@author: uidp4235
'''

# from test import test_support
import unittest
from Runmain import Runmain
import re
import common.log_confige as log
import os


class MyTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # print('***************请注意，测试开始***************')
        log.logging.info('***************请注意，测试开始***************')
        
    @classmethod
    def tearDownClass(cls):
        # print('这是所有case的后置条件01')
        log.logging.info('***************请开心，所有case测试结束***************')
        
    def setUp(self):
        # print('这是每条case的前置条件01')
        pass
    
    def clear(self):
        print('this is clear')
        
    def tearDown(self):
        # print('这是每条case的后置条件01')
        log.logging.info('******本条case测试结束******')

    @staticmethod
    def action(arg1):
        run = Runmain()
        run.runmain(int(arg1)-1)

    def test_logoutcase2(self):
        print('')
        self.assertEqual('1', '1')

class GenerateTestCases:
    def __init__(self):
        arglists = []
        with open(os.path.abspath(os.path.dirname(os.getcwd())) + '\\report\\result.txt') as f:
            data = f.readlines()
            arglists = re.findall(r"\d+\.?\d*", str(data[0]))

        for args in arglists:
            setattr(MyTestCase, 'test_func_%s'%(args), MyTestCase.action(*args))


if __name__ == '__main__':
    # unittest.main()
    GenerateTestCases()
