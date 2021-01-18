#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 16:25
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : studio_install.py


from test_studio.unit.func.file_exist import File_exist as fe
import os
from time import sleep


"""
循环判断C:斜杠download是否有安装文件
    定义一个方法，下载时候就调用
如果有指定类型exe的文件则安装
勾选同意协议
点击确定
1.选择社区版激活
    输入邮箱，密码
     下拉选择租户
2.控制台激活
    设置连接字符串
    输入账号，密码
    下拉选择租户
3.许可证激活
    输入许可证
"""

"""
判断应用程序是否安装成功，查看指定路径有没有exe文件
    如果有则双击安装
"""



class 安装():
    def install_exe(self,browser):
        """判断下载路径安装文件是否存在，若存在则安装"""
        path = r'C:\download'
        sleep(30)
        while True:
            if fe().file_exist(path=path, file_type='.exe'):
                print("下载完成")
                break
            else:
                continue
        # 安装
        file_arr = os.listdir(path=path)
        exe_file = [path + "\\" + file for file in file_arr][0]
        # 打开安装文件，进行安装
        os.startfile(exe_file)
        browser.quit()
        sleep(100)
