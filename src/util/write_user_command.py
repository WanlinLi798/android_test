# -*- coding: utf-8 -*-
'''
Created on 2018年10月25日

@author: uidq1501
'''
import yaml
from port import Port

class WriteUserCommand:
    def read_data(self):
        with open("../config/userconfig.yaml") as fr:
            data = yaml.load(fr)
        return data
            
    def get_value(self,key,port):
        data = self.read_data()
        if data and ('4' in data[key]['port']):
            value = data[key][port]
            return value
        
    def write_data(self,i, device, bp, port):
        data = self.join_data(i, device, bp, port)
        with open("../config/userconfig.yaml",'a') as fr:
            yaml.dump(data,fr)
        fr.close()
            
    def join_data(self,i,device,bp,port):
        '''
        拼接数据
        '''
        data = {
            "user_info_"+str(i):{
            "deviceName":device,
            "bp":bp,
            "port":port
            }
            }
        return data
    
    def clear_data(self):
        with open("../config/userconfig.yaml",'w') as fr:
            fr.truncate()    
        fr.close()

    def get_file_lines(self):
        data = self.read_data()
        return len(data)

            
        
if __name__ == '__main__' :
    YQ = WriteUserCommand()
#     print YQ.get_value('user_info_'+str(0),'port')
#     print YQ.read_data()[key]['port']