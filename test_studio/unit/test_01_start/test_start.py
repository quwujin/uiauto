#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 14:06
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : test_start.py

import os
import shutil
import time

import allure
import pytest
from selenium.webdriver.common.keys import Keys

from test_studio.unit.func.element_clip import Clipboard
from test_studio.unit.func.element_exist import Element_exist as ee
from test_studio.unit.func.element_wait import Element_wait as ew
from test_studio.unit.step.step import New_step
from test_studio.unit.step.step import Start_step


@pytest.mark.run(order=1)
@allure.feature("侧边栏-开始模块")
class Test_start:
    """定义标签"""

    @pytest.fixture(scope="function", autouse=True)  # scope 定义作用范围  session > module > class > function
    def click_start(self, open_studio):
        """点击开始"""
        if ee(open_studio).isElementCanClick(xpath='//*[@AutomationId="tabStart"]') is False:
            open_studio.find_element_by_xpath('//Menu[@AutomationId="startMenu"]/MenuItem[@ClassName="MenuItem"]/Text[@ClassName="TextBlock"][@Name="开始"]').click()
        else:
            open_studio.find_element_by_xpath('//*[@AutomationId="tabStart"]').click()
        yield
        # 注意：方法后的输出是在类输出里面看的，此时方法已经结束，看不到了
        # url = ""
        # # 前置
        # driver = webdriver.Chrome()
        # driver.get(url)  # url为链接地址
        # yield driver  # yield 之前代码是前置，之后的代码就是后置
        # # 后置
        # driver.quit()

    @allure.story("点击打开流程项目")
    def test_IDE_开始_最近_点击打开流程项目(self, open_studio):
        """23532#开始页面-最近#点击打开流程项目#0"""
        """新建一个流程项目和组件项目，退出到最近列表分别点击"""
        s_step = Start_step(open_studio)
        s_step.点击新建流程项目()
        s_step.输入项目_组件名称(pj_name='测试项目一')
        s_step.enter_project_path()
        s_step.新建流程or组件项目_点击创建项目()
        # 判断项目是否显示
        if s_step.判断项目是否显示():
            # 退出到开始界面
            s_step.退出到开始界面()
            # 新建组件项目
            s_step.新建组件项目()
            # 点击提示框中的“是”
            s_step.点击提示框中的_是()
            # 新建组件项目 - 输入组件项目名称
            s_step.输入项目_组件名称(pj_name='测试组件')
            # 点击创建
            s_step.新建流程or组件项目_点击创建项目()
            if s_step.判断项目是否显示():
                # 退出到开始界面
                s_step.退出到开始界面()
                # 点击最近列表第一个创建的测试项目
                s_step.点击测试项目()
                # 点击提示框中的“是”
                s_step.点击提示框中的_是()
                result = s_step.判断项目是否显示()
                assert result
            else:
                pytest.xfail(reason="创建组件失败")
        else:
            pytest.xfail(reason="创建项目失败")

    @allure.story("点击打开组件项目")
    def test_IDE_开始_最近_点击打开组件项目(self, open_studio):
        """23533#开始页面-最近#点击打开组件项目#0"""
        """新建一个流程项目和组件项目，退出到最近列表分别点击"""
        s_step = Start_step(open_studio)
        # 获取时间，跟下一个case比较
        global case_time_old
        case_time_old = open_studio.find_elements_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                                           '@AutomationId="tabStart"]/Custom[@ClassName="UCHomeStart"]/List['
                                                           '@AutomationId="LocalProjectListBox"]/ListItem[@ClassName="ListBoxItem"]['
                                                           '@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]/Text[@ClassName="TextBlock"]')[5].text
        # 点击第二次创建的测试组件
        s_step.点击组件项目()
        # 点击提示框中的“是”
        s_step.点击提示框中的_是()
        result = s_step.判断项目是否显示()
        assert result

    @allure.story("本地路径不存在_提示是否删除点确定")
    def test_IDE_开始_最近_本地路径不存在提示是否删除点确定(self, open_studio):
        """23535#开始页面-最近#本地路径不存在提示是否删除点确定#0"""
        s_step = Start_step(open_studio)
        s_step.点击新建流程项目()
        # 点击提示框中的“是”
        s_step.点击提示框中的_是()
        s_step.输入项目_组件名称(pj_name='测试项目删除', )
        s_step.新建流程or组件项目_点击创建项目()
        # 判断项目是否显示
        if s_step.判断项目是否显示():
            # 退出到开始界面
            s_step.退出到开始界面()
        # 点击一个测试项目，再回退
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                          '@AutomationId="tabStart"]/Custom[@ClassName="UCHomeStart"]/List[@AutomationId="LocalProjectListBox"]/ListItem['
                                          '@ClassName="ListBoxItem"][@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]//*['
                                          'contains(@Name,"测试项目一")]').click()
        # 点击提示框中的“是”
        s_step.点击提示框中的_是()
        # 判断项目是否显示
        if s_step.判断项目是否显示():
            # 退出到开始界面
            s_step.退出到开始界面()
        # 获取最近列表最近测试项目的地址
        pl_folder = open_studio.find_elements_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                                       '@AutomationId="tabStart"]/Custom[@ClassName="UCHomeStart"]/List[@AutomationId="LocalProjectListBox"]/ListItem['
                                                       '@ClassName="ListBoxItem"][@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]//*['
                                                       'contains(@Name,"测试项目删除")]')[1].text
        pl_folder_str = pl_folder
        # 删除指定文件夹
        #     判断文件夹是否存在，若存在，删除
        if os.path.exists(pl_folder_str):
            shutil.rmtree(pl_folder_str)
        # 点击最近列表最近一个项目
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                          '@AutomationId="tabStart"]/Custom[@ClassName="UCHomeStart"]/List[@AutomationId="LocalProjectListBox"]/ListItem['
                                          '@ClassName="ListBoxItem"][@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]//*['
                                          'contains(@Name,"测试项目删除")]').click()
        assert ew(open_studio).xianshi_wait(xpath='//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"]/Custom['
                                                  '@ClassName="CommonDialogContent"]') is not None  # 是否有"提示"框出现
        # 删除这个项目
        open_studio.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]/Button[@ClassName="Button"][@Name="是"]/Text[@ClassName="Text"][@Name="是"]').click()

    @allure.story("打开其中一个项目该项目的位置被置顶上次使用时间刷新且没有出现2条记录")
    def test_IDE_开始_最近_打开其中一个项目该项目的位置被置顶上次使用时间刷新且没有出现2条记录(self, open_studio):
        """23519#开始页面-最近#打开其中一个项目该项目的位置被置顶上次使用时间刷新且没有出现2条记录#0"""
        # 点击组件项目
        s_step = Start_step(open_studio)
        s_step.点击组件项目()
        # 点击提示框中的“是”
        s_step.点击提示框中的_是()
        result = s_step.判断项目是否显示()
        if result:
            # 退出到开始界面
            s_step.退出到开始界面()
        case_time_new = open_studio.find_elements_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                                           '@AutomationId="tabStart"]/Custom[@ClassName="UCHomeStart"]/List['
                                                           '@AutomationId="LocalProjectListBox"]/ListItem[@ClassName="ListBoxItem"]['
                                                           '@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]/Text[@ClassName="TextBlock"]')[3].text
        time_result = case_time_new != case_time_old
        number_result = len(open_studio.find_elements_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                                               '@AutomationId="tabStart"]/Custom[@ClassName="UCHomeStart"]/List['
                                                               '@AutomationId="LocalProjectListBox"]/ListItem[@ClassName="ListBoxItem"]['
                                                               '@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]//*[contains(@Name,"测试组件")]'))
        assert time_result and number_result == 2

    @allure.story("点击最近里列表删除按钮")
    def test_IDE_开始_最近_点击删除按钮(self, open_studio):
        """23531#开始页面-最近#点击删除按钮#0"""
        s_step = Start_step(open_studio)
        pj = open_studio.find_element_by_xpath(
            '//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"][@AutomationId="tabStart"]/Custom['
            '@ClassName="UCHomeStart"]/List[@AutomationId="LocalProjectListBox"]/ListItem[@ClassName="ListBoxItem"]['
            '@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]/Button[@AutomationId="DeleteBtn"]')
        # 删除创建的测试项目和测试组件
        pj.click()
        pj = open_studio.find_element_by_xpath(
            '//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"][@AutomationId="tabStart"]/Custom['
            '@ClassName="UCHomeStart"]/List[@AutomationId="LocalProjectListBox"]/ListItem[@ClassName="ListBoxItem"]['
            '@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]/Button[@AutomationId="DeleteBtn"]')
        pj.click()
        assert s_step.判断最近列表测试项目或测试组件是否显示() == False


if __name__ == '__main__':
    pytest.main(['-s', '-v'])
