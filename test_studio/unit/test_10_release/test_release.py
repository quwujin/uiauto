#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 17:02
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : test_release.py
import os
import time

import allure
from test_studio.unit.func.file_exist import FileAndFolder
from test_studio.unit.step.step import Release_step, Open_step, Start_step, Login_step, Project_manage_step, Install_step, New_step
import pytest


@allure.feature("发布模块")
class Test_release:

    @pytest.mark.skip()
    @allure.story("IDE_发布_发布到控制台")
    def test_IDE_发布_发布到控制台(self, open_studio):
        """7783#登录激活#用邮箱激活控制台#0"""
        """
        1.点击个人信息，判断是否登录
        2.1 删除"C:\EncooTest\一般业务流程"（若有删除，若没有跳过）
        2.新建"一般业务流程"项目（指定名称，若存在，则更新）
        3.点击发布，选择控制台 点击发布
        4.判断是否输出"项目已成功发布“
        """
        # region 定义变量
        r_step = Release_step(open_studio)  # 发布步骤
        l_step = Login_step(open_studio)  # 登录步骤
        n_step = New_step(open_studio)  # 新建步骤
        s_step = Start_step(open_studio)  # 开始步骤
        username = 'quwujin@encootech.com'  # 邮箱
        pwd = 'Qwj2310287'  # 密码
        # endregion

        l_step.click_personal_info()
        login_result = l_step.is_login()
        print(login_result)
        if login_result == False:
            l_step.click_login()
            l_step.input_username_pwd(username=username, pwd=pwd)
            l_step.click_next()
            l_step.click_enter()
        FileAndFolder().deleteFolder(r'C:\EncooTest\一般业务流程')
        n_step.change_to_new()
        n_step.click_general_business_process()
        if r_step.is_show_yn_dialog():
            s_step.点击提示框中的_是()
        r_step.click_create()
        r_step.click_release()
        r_step.click_console()
        r_step.click_diolog_release()


        result = r_step.Is_show_result()
        assert result


if __name__ == '__main__':
    pytest.main(['-s', '-v'])
