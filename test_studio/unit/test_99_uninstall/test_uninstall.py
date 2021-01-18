#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 17:02
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : test_uninstall.py
import allure
import pytest

from test_studio.unit.func.get_uninstall_path import uninstall_software, get_software


@allure.feature("卸载相关")
class Test_卸载():
    @allure.story("卸载程序测试")
    def test_删除程序(self):
        """7783#登录激活#用邮箱激活控制台#0"""
        uninstall_software("Encoo Studio")
        array = get_software()
        assert "Encoo Studio" not in array
