#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/14 16:35
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : get_reg_value.py
import win32api, win32con


def get_all_installed_software():
    """获取所有安装过的程序"""
    reg_root = win32con.HKEY_LOCAL_MACHINE
    ref_user = win32con.HKEY_CURRENT_USER
    reg_paths = [r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall", r"SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall",
                 r"Software\Microsoft\Windows\CurrentVersion\Uninstall"]
    rst_list = []
    for path in reg_paths:
        pkey = win32api.RegOpenKeyEx(reg_root, path)
        for item in win32api.RegEnumKeyEx(pkey):
            value_paths = path + "\\" + item[0]
            # print(value_paths)
            try:
                vkey = win32api.RegOpenKeyEx(reg_root, value_paths)
                DisplayName, key_type = win32api.RegQueryValueEx(vkey, "DisplayName")
                UninstallString, key_type = win32api.RegQueryValueEx(vkey, "UninstallString")
                # print({'name':DisplayName,'Uninstall string':UninstallString})
                rst_list.append((DisplayName, UninstallString))
                win32api.RegCloseKey(vkey)
            except:
                pass
        win32api.RegCloseKey(pkey)
    path = r"Software\Microsoft\Windows\CurrentVersion\Uninstall"
    pkey = win32api.RegOpenKeyEx(ref_user, path)
    for item in win32api.RegEnumKeyEx(pkey):
        value_paths = path + "\\" + item[0]
        try:
            vkey = win32api.RegOpenKeyEx(ref_user, value_paths)
            DisplayName, key_type = win32api.RegQueryValueEx(vkey, "DisplayName")
            UninstallString, key_type = win32api.RegQueryValueEx(vkey, "UninstallString")
            rst_list.append((DisplayName, UninstallString))
            win32api.RegCloseKey(vkey)
        except:
            pass
    win32api.RegCloseKey(pkey)
    return rst_list


if __name__ == '__main__':
    software = get_all_installed_software()
    print(software)
