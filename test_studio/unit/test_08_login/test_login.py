#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 17:02
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : test_login.py
import os
import time

import allure
from test_studio.unit.func.file_exist import File_exist
from test_studio.unit.func.file_exist import FileAndFolder
from test_studio.unit.step.step import Open_step, Start_step, Login_step, Project_manage_step, Install_step
import pytest

from test_studio.unit.test_00_install import test_download_and_install
from test_studio.unit.test_00_install.test_download_and_install import Test_验证下载安装


@allure.feature("登录激活模块")
class Test_login():
    """项目管理测试类"""

    @allure.story("IDE_登录激活_用邮箱激活控制台")
    def test_IDE_登录激活_用邮箱激活控制台(self, open_studio):
        """7783#登录激活#用邮箱激活控制台#0"""
        """
        1.点击个人信息
        2.点击登录
        3.输入邮箱和密码
        4.点击下一步
        5.租户名称显示云扩企业测试，点击确定
        验证：account.json 文件存在
        """
        l_step = Login_step(open_studio)
        username = 'quwujin@encootech.com'  # 邮箱
        pwd = 'Qwj2310287'  # 密码
        appdata = os.getenv("APPDATA")
        root_path = appdata.split("\\R")[0]
        file_path = rf'{root_path}\Local\Encoo\Data\account.json'

        l_step.click_personal_info()
        l_step.click_login()
        l_step.input_username_pwd(username=username, pwd=pwd)
        l_step.click_next()
        l_step.click_enter()
        result = File_exist().is_file_exist(file_path)

        assert result

    @allure.story("IDE_登录激活_解除许可证")
    def test_IDE_登录激活_解除许可证(self, open_studio):
        """9068#登录激活#解除许可证#0"""
        """
        点击个人信息
        点击查看许可证
        点击解除当前许可证
        弹窗点击是
        判断 显示激活方式 and license.json文件删除
        """
        qi_licence = test_download_and_install.qi_licence
        appdata = os.getenv("APPDATA")
        root_path = appdata.split("\\R")[0]
        file_path = rf'{root_path}\Local\Encoo\Data\license.json'
        l_step = Login_step(open_studio)
        i_step = Install_step(open_studio)

        l_step.click_personal_info()
        l_step.click_view_permit()
        l_step.click_unlock_permit()
        l_step.click_alert_yes()
        time.sleep(5)

        result = File_exist().is_file_exist(file_path=file_path)
        show_result = i_step.is_permit_show()
        if i_step.is_permit_show():
            i_step.use_permit_active(qi_licence=qi_licence)
        else:
            pytest.xfail("显示界面异常")

        assert result == False and show_result == True

    @allure.story("IDE_登录激活_查看登录信息_点击注销")
    def test_IDE_登录激活_查看登录信息_点击注销(self, open_studio):
        """9098#登录激活#查看登录信息-点击注销#0"""
        """
        IDE_登录激活_查看登录信息_点击注销
        点击个人信息
        点击退出登录
        验证 弹出框
        """
        l_step = Login_step(open_studio)
        l_step.click_personal_info()
        l_step.click_logout()
        assert l_step.is_alert_show()


if __name__ == '__main__':
    pytest.main(['-s', '-v'])
