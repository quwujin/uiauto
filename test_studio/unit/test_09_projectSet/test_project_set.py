#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 17:02
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : test_project_set.py
import os
import time

import allure
from test_studio.unit.func.file_exist import File_exist
from test_studio.unit.func.file_exist import FileAndFolder
from test_studio.unit.step.step import Open_step,Start_step, Login_step,Project_manage_step,Install_step
import pytest

from test_studio.unit.test_00_install import test_download_and_install
from test_studio.unit.test_00_install.test_download_and_install import Test_验证下载安装

@allure.feature("项目设置模块")
class Test_login():
    """项目设置测试类"""

    @pytest.mark.skip()
    @allure.story("IDE_项目设置_设置默认前延迟")
    def test_IDE_项目设置_设置默认前延迟(self, open_studio):
        """7783#登录激活#用邮箱激活控制台#0"""
        ...

    @pytest.mark.skip()
    @allure.story("IDE_项目设置_设置默认后延迟")
    def test_IDE_项目设置_设置默认后延迟(self,open_studio):
        """7783#登录激活#用邮箱激活控制台#0"""
        ...

    @pytest.mark.skip()
    @allure.story("IDE_项目设置_设置默认浏览器类型")
    def test_IDE_项目设置_设置默认浏览器类型(self,open_studio):
        """7783#登录激活#用邮箱激活控制台#0"""
        ...


if __name__ == '__main__':
    pytest.main(['-s', '-v'])
