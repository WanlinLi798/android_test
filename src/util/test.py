# -*- coding: utf-8 -*-
'''
@author: uidq1501
'''
from page.source_switch_page import Source_Page
from util.create_log_folder import Create_folder

save_PIC = Create_folder().Create('factory_reset')
load_PIC = Create_folder().Create('match')
Source_Page(0).get_screenshot(save_PIC)
Source_Page(0).get_screenshot(load_PIC+str(1)+'.png')

