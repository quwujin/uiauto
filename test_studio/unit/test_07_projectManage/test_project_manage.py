#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 17:02
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : test_project_manage.py
import time

import allure

from test_studio.unit.func.file_exist import File_exist
from test_studio.unit.func.file_exist import FileAndFolder
from test_studio.unit.step.step import Start_step
from test_studio.unit.step.step import Project_manage_step
from test_studio.unit.step.step import Open_step
import pytest


@allure.feature("项目管理模块")
class Test_project_manage():
    """项目管理测试类"""

    @pytest.mark.skip
    @allure.story("IDE_项目管理_右键关闭项目")
    def test_IDE_项目管理_右键关闭项目(self, open_studio):
        """23645#项目管理#右键关闭项目#0"""
        """
        1.新建指定名称的项目
        2.进指定的项目     进行项目管理测试   判断项目加载完
        3.右键点击
        4.选择关闭项目
        验证：项目关闭，页面跳转
        """
        s_step = Start_step(open_studio)
        pm_step = Project_manage_step(open_studio)

        open_studio.find_element_by_xpath('//*[@AutomationId="tabStart"]').click()

        s_step.点击新建流程项目()
        s_step.点击提示框中的_是()
        s_step.输入项目_组件名称(pj_name="新建测试项目管理")
        s_step.新建流程or组件项目_点击创建项目()
        if s_step.判断项目是否显示():
            pm_step.项目标题右键(pj_name="新建测试项目管理")
            pm_step.选择项目关闭()
            time.sleep(2)
            pm_step.switch_window()
            assert s_step.判断项目是否显示() == False
        else:
            pytest.xfail(reason="打开项目失败")

    @pytest.mark.skip
    @allure.story("IDE_项目管理_关闭xaml文件不关闭项目")
    def test_IDE_项目管理_关闭所有xaml文件不关闭项目(self, open_studio):
        """23646#项目管理#关闭所有xaml文件不关闭项目#0"""
        """
        1.点击测试项目
        2.判断编辑页面打开
        3.点击xaml的关闭按钮
        判断项目不退出
        """
        s_step = Start_step(open_studio)
        pm_step = Project_manage_step(open_studio)
        s_step.点击最近列表项目_by_name(pj_name="新建测试项目管理")
        if s_step.判断项目是否显示():
            pm_step.close_tab()
            assert s_step.判断项目是否显示() == False
        else:
            pytest.xfail(reason="打开项目失败")

    @pytest.mark.skip
    @allure.story("IDE_项目管理_单击打开文件")
    def test_IDE_项目管理_单击打开文件(self, open_studio):
        """8844#项目管理#单击打开文件#0"""
        """
        1.点击开始，退出到开始届面
        2.新建测试组件项目 （提示新项目框点击是，输入组件名称，点击创建）
        3.判断编辑窗口是否显示（若显示：点击开始，点击测试项目，提示新项目框点击是）
        判断是否显示项目---开始菜单栏 测试完成
        4.点击开始，退到开始界面
        5.点击打开，点击本地项目，点击组件项目，提示框点是
        6.判断是否显示项目 -- 打开菜单栏 测试完成
        """
        s_step = Start_step(open_studio)
        pm_step = Project_manage_step(open_studio)
        o_step = Open_step(open_studio)
        pm_step.click_edit_start()
        s_step.新建组件项目()
        s_step.点击提示框中的_是()
        s_step.输入项目_组件名称(pj_name="新建测试组件管理")
        s_step.新建流程or组件项目_点击创建项目()
        if s_step.判断项目是否显示():
            pm_step.click_edit_start()
            s_step.点击最近列表项目_by_name(pj_name="新建测试项目管理")
            s_step.点击提示框中的_是()
            if s_step.判断项目是否显示():
                global result_start
                result_start = True
                pm_step.click_edit_start()
            else:
                result_start = False
                pytest.xfail("开始菜单栏 - 打开测试项目失败")
            o_step.点击打开侧边栏()
            o_step.click_local_item()
            o_step.click_last_list_item(pj_name="新建测试组件管理")
            s_step.点击提示框中的_是()
            result_open = s_step.判断项目是否显示()
            assert result_open and result_start
        else:
            pytest.xfail("创建组件项目失败")

    @pytest.mark.skip
    @allure.story("IDE_项目管理_项目重命名后导出")
    def test_IDE_项目管理_项目重命名后导出(self,open_studio):
        """10579#项目管理#项目重命名后导出#0"""
        """
        IDE_项目管理_项目重命名后导出
        1.组件测试编辑页面，项目名称点击右键
        2.点击重命名
        3.输入其他项目名称，先清空，输入完点回车
        4.点击文件
        5.点击项目导出
        6.弹出框点击导出按钮
        7.检查"C:\EncooTest"文件夹下有没有指定项目名称的dgs文件
        """
        pm_step = Project_manage_step(open_studio)
        pm_step.项目标题右键(pj_name="新建测试组件管理")
        pm_step.click_rename()
        pm_step.input_pj_name(pj_name="重命名测试组件管理")
        pm_step.click_fold()
        pm_step.click_out_pj()
        result = File_exist().is_file_exist(file_path=r"C:\EncooTest\重命名测试组件管理.egs")
        FileAndFolder().deleteFolder(r"C:\EncooTest\重命名测试组件管理")
        FileAndFolder().deleteFile(r"C:\EncooTest\重命名测试组件管理.egs")
        assert result

    @pytest.mark.skip
    @allure.story("IDE_项目管理_文件重命名_修改当前文件名")
    def test_IDE_项目管理_文件重命名_修改当前文件名(self,open_studio):
        """10605#项目管理#文件重命名_修改当前文件名#0"""
        """
        IDE_项目管理_文件重命名_修改当前文件名
        1.xaml文件点击右键
        2.点击重命名
        3.输入新的文件名 点击回车
        验证 文件名正确，没有xaml.xaml
        """
        pm_step = Project_manage_step(open_studio)
        o_step = Open_step(open_studio)
        o_step.click_last_list_item(pj_name="新建测试组件管理")
        pm_step.right_click_file()
        pm_step.click_file_rename()
        pm_step.input_file_name(file_name="测试组件项目重命名.xaml")
        file_name = pm_step.get_file_name()
        assert file_name == "测试组件项目重命名.xaml"


if __name__ == '__main__':
    pytest.main(['-s', '-v'])
