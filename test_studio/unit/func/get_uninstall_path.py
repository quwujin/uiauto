#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/14 16:30
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : get_uninstall_path.py
import os
import subprocess

from test_studio.unit.func import get_reg_value

"""
可扩展，卸载任何一款在注册表出现的软件都可以
"""


# appdata = os.getenv("APPDATA")
# root_path = appdata.split("\\R")[0]

def get_software():
    """获取软件列表"""
    rst_list = get_reg_value.get_all_installed_software()
    rst = []
    for each in rst_list:
        rst.append(each[0])
    return rst


def uninstall_software(software_name):
    """卸载指定windows程序"""
    rst_list = get_reg_value.get_all_installed_software()
    uninstall_string = ""
    for each in rst_list:
        if each[0] == software_name:
            uninstall_string = each[1]
            break
    if uninstall_string == "":
        print("Not found installed program.")
        return
    else:
        print("uninstall " + software_name)
        uninstall_string = uninstall_string.replace('\\', '\\\\')
        cd_path = "\\".join(uninstall_string.split('\\')[:-1]).replace('"','')
        os.chdir(cd_path)
        cmd = uninstall_string.split('\\')[-1].replace('"','')
        print(cmd)
        subprocess.Popen(cmd)


# uninstall_software("Encoo Studio")
