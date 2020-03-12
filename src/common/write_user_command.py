# -*- coding: utf-8 -*-
'''
Created on 2018年10月25日

@author: uidq1501
'''
import yaml

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
        
    def write_data(self, i, device, bp, port):
        data = self.join_data(i, device, bp, port)
        with open("../config/userconfig.yaml", 'a') as fr:
            yaml.dump(data,fr)
        fr.close()
            
    def join_data(self, i, device, bp, port):
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
        with open("../config/userconfig.yaml", 'w') as fr:
            fr.truncate()    
        fr.close()

    def get_file_lines(self):
        data = self.read_data()
        return len(data)

    def change_key(self, name):
        with open(InitParam().roi_yaml_filepath, 'r+') as fr:
            data = yaml.load(fr)
            y1 = data['key']['iy']
            x1 = data['key']['ix']
            y = data['key']['y']
            x = data['key']['x']
            data1 = {
                'key'+name:{
                    "ix":x1,
                    "iy":y1,
                    "x":x,
                    "y":y,
                    }  
                }
            yaml.dump(data1,fr)
            return data1
           

if __name__ == '__main__' :
    YQ = WriteUserCommand()
    print(YQ.change_key('BT'))
#     print YQ.get_value('user_info_'+str(0),'port')
#     print YQ.read_data()[key]['port']