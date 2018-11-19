# -*- coding: utf-8 -*-
'''
Created on 2018年10月22日

@author: uidq1501
'''
from page.source_switch_page import Source_Page

class SourceHandle:
    def __init__(self,i):
            self.page = Source_Page(i)
        
    def menu(self):
        '''
     进入menu界面
        '''
        self.page.get_menu_element.click()
        
    def player(self):
        '''
     进入player界面
        '''
        self.page.get_player_element().click()

    def music_hall(self):
        '''
     进入music_hall界面
        '''
        
        self.page.get_music_hall_element().click()
        
    
    def BT(self):
        '''
     进入BT界面
        '''
        self.page.get_BT_element().click()
        
    def USB_audio(self):
        '''
     进入USB_audio界面
        '''
        self.page.get_USB_audio_element().click()
        
    def home(self):
        self.page.home()

    def local_music(self):
        self.page.local_music().click()

    def my_icon(self):
        self.page.get_my_icon().click()

    def back(self):
        self.page.get_back().click()

    def find(self):
        self.page.get_find().click()

    def setting(self):
        self.page.get_setting().click()

    def system(self):
        self.page.get_system().click()

    def factory_reset(self):
        self.page.get_factory_reset().click()

    def confirm(self):
        self.page.get_confirm().click()

    def quit(self):
        self.page.quit()

if __name__ == '__main__' :
    SourceHandle(0).menu()

        
    
    