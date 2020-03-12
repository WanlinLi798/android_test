# -*- coding: utf-8 -*-
'''
Creat on 2020年3月03日

@author: uidp4235
'''

import os


class InitParam:

    def __init__(self):
        self._screenshotpath = os.path.abspath(os.path.dirname(os.getcwd()))+'\screenshot'
        self._errorshotpath = self._screenshotpath + '\error_screenshot'
        self._defaultpicname = 'screenshot.png'
        self.roi_yaml_filepath = os.path.abspath(os.path.dirname(os.getcwd())) + '\\report\\ROI.yaml'

    def get_keycode(self, functionname):
        switcher = {
            'Call': '5',  # 拨号键
            'Endcall': '6',  # 挂机键
            'Homehome': '3',  # 按键
            'Menu': '82',  # 菜单键
            'Back': '4',  # 返回键
            'Search': '84',  # 搜索键
            'Camera': '27',  # 拍照键
            'Focus': '80',  # 拍照对焦键
            'Power': '26',  # 电源键
            'Notification': '83',  # 通知键
            'Mute': '91',  # 话筒静音键
            'Volumemute': '164',  # 扬声器静音键
            'Volumeup': '24',  # 音量增加键
            'Volumedown': '25',  # 音量减小键
             # 控制键
            'Enter': '66',  # 回车键
            'Escapeesc': '111',  # 键
            'Dpadcenter': '23',  # 导航键确定键
            'Dpadup': '19',  # 导航键向上
            'Dpaddown': '20',  # 导航键向下
            'Dpadleft': '21',  # 导航键向左
            'Dpadright': '22',  # 导航键向右
            'Movehome': '122',  # 光标移动到开始键
            'Moveend': '123',  # 光标移动到末尾键
            'Pageup': '92',  # 向上翻页键
            'Pagedown': '93',  # 向下翻页键
            'Del': '67',  # 退格键
            'Forwarddel': '112',  # 删除键
            'Insert': '124',  # 插入键
            'Tabtab': '61',  # 键
            'Numlock': '143',  # 小键盘锁
            'Capslock': '115',  # 大写锁定键
            'Breakbreakpause': '121',  # 键
            'Scrolllock': '116',  # 滚动锁定键
            'Zoomin': '168',  # 放大键
            'Zoomout': '169',  # 缩小键
        }

        return switcher.get(functionname, "82")   # 默认菜单按键 keycode 82
