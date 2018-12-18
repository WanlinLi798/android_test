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


class Runmain:

    def runmain(self,i):
        log.logging.info('case'+str(i+1)+'开始测试喽,Appium启动中，请骚等>>>>>>')
        server = Server()
        server.main()
        get = GetExcel(i)
        Action = ActionMethod()
        case_NO = get.get_case_lines()
        cycle = get.get_handle_value(case_NO-1)
        n = 0
        pass_num = 0

        while (n<cycle):
            n+=1
            fail_num = 0
            log.logging.info( '开始第'+str(n)+"次测试")
            case_NO = get.get_case_lines()
            conditon = get.get_method(case_NO-2)
            
            if n==1or conditon.find('repeat_ab') == -1:
                for m in range(1,case_NO-1):
    
                    method = get.get_method(m)
                    element = get.get_element(m)
                    handle_value = get.get_handle_value(m) 
                    expect_element = get.get_except(m)
                    expect_handle = str(get.get_except_handle(m))
    
                    
                    excute_method = getattr(Action,method)
                    if element == None and handle_value ==None:
                        excute_method()            
                    else:
                        if element != None:
                            excute_method(element,handle_value)
                        else:
                            excute_method(handle_value)
                        if expect_element != None:
                            if expect_handle == 'check' or expect_handle == 'sound_check':
                                expect_result = getattr(Action,expect_handle)
                                result = expect_result(expect_element)
                            else:
                                expect_result = getattr(Action,expect_handle)
                                result = expect_result(expect_element,n)                            
                            if result:
    #                             get.write_value(i,m,n+7,"pass")
    
                                log.logging.info('第'+str(n)+"次测试进行中......")
                            else:
    #                             get.write_value(i,m,n+7,"fail") 
                                fail_num+=1
                                log.logging.info('第'+str(n)+"次测试FAIL")
                if fail_num==0:
                    pass_num+=1
    #             time.sleep(2)
                log.logging.info('总共测试了'+str(n)+'次,成功了'+str(pass_num)+"次")
                time.sleep(2)
            else:
                    a =  get.get_element(case_NO-2)    
                    b =  get.get_handle_value(case_NO-2)
                    for m in range(int(a),int(b)):
        
                        method = get.get_method(m)
                        element = get.get_element(m)
                        handle_value = get.get_handle_value(m) 
                        expect_element = get.get_except(m)
                        expect_handle = str(get.get_except_handle(m))
        
                        
                        excute_method = getattr(Action,method)
                        if element == None and handle_value ==None:
                            excute_method()            
                        else:
                            if element != None:
                                excute_method(element,handle_value)
                            else:
                                excute_method(handle_value)
                            if expect_element != None:
                                if expect_handle == 'check' or expect_handle == 'sound_check':
                                    expect_result = getattr(Action,expect_handle)
                                    result = expect_result(expect_element)
                                else:
                                    expect_result = getattr(Action,expect_handle)
                                    result = expect_result(expect_element,n)                            
                                if result:
        #                             get.write_value(i,m,n+7,"pass")
        
                                    log.logging.info('第'+str(n)+"次测试进行中......")
                                else:
        #                             get.write_value(i,m,n+7,"fail") 
                                    fail_num+=1
                                    log.logging.info('第'+str(n)+"次测试FAIL")
                    if fail_num==0:
                        pass_num+=1
        #             time.sleep(2)
                    log.logging.info('总共测试了'+str(n)+'次,成功了'+str(pass_num)+"次")
                    time.sleep(2)                     
                    
        server.kill_server()
        exit                  
                                   
def get_count():
    write_user_file = WriteUserCommand()
    count = write_user_file.get_file_lines()
    return count
    
         
       
if __name__ =='__main__':
    run = Runmain()
    run.runmain(3)
            
            
            