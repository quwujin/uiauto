#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 17:02
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : test_2_new.py
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


@pytest.mark.run(order=2)
@allure.feature("侧边栏-【新建】模块")
class Test_新建侧边栏:
    # @allure.step("点击方法")
    # def element_click(driver, xpath):
    #     """封装点击方法"""
    #     driver.find_element_by_xpath(xpath).click()
    #     time.sleep(0)
    #
    # @pytest.fixture(scope="function", autouse=True)  # scope 定义作用范围  session > module > class > function
    # def click_new(self, open_studio):
    #     """点击新建"""
    #     flag = ee(open_studio).isElementCanClick(xpath='//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: '
    #                                                    'Content:"]/Text['
    #                                                    '@ClassName="TextBlock"][@Name="新建"]')
    #     # 判断是否在项目编辑页面
    #     if flag is False:
    #         self.element_click(driver=open_studio, xpath='//Menu[@AutomationId="startMenu"]/MenuItem[@ClassName="MenuItem"]')
    #         self.element_click(open_studio,
    #                            '//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: Content:"]/Text['
    #                            '@ClassName="TextBlock"][@Name="新建"]')
    #     else:
    #         self.element_click(open_studio,
    #                            '//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: Content:"]/Text['
    #                            '@ClassName="TextBlock"][@Name="新建"]')
    #     yield

    @allure.story("新建_新建流程图")
    def test_IDE_新建_新建流程图(self, open_studio):
        """23544#新建页面-新建流程项目#新建流程图#0"""
        """新建_新建流程图"""
        n_step = New_step(open_studio)
        s_step = Start_step(open_studio)
        # 点击流程项目
        n_step.点击新建_流程项目()
        # 判断是否有提示窗口，如果有的话点是
        if ew(open_studio).xianshi_wait(xpath='//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"]/Custom['
                                              '@ClassName="CommonDialogContent"]') is not None:
            s_step.点击提示框中的_是()
        # 输入项目名称
        s_step.输入项目_组件名称(pj_name="新建测试项目-流程图")
        s_step.enter_project_path()
        # 选择流程图
        n_step.选择流程图()
        # 点击创建
        s_step.新建流程or组件项目_点击创建项目()
        if s_step.判断项目是否显示():
            assert n_step.判断项目是否显示()
        else:
            pytest.xfail(reason="创建项目--流程图失败")

    @allure.story("新建_新建序列")
    def test_IDE_新建_新建序列(self, open_studio):
        """23545#新建页面-新建流程项目#新建序列#0"""
        """新建_新建序列"""
        n_step = New_step(open_studio)
        s_step = Start_step(open_studio)
        # 点击流程项目
        n_step.点击新建_流程项目()
        # 判断是否有提示窗口，如果有的话点是
        if ew(open_studio).xianshi_wait(xpath='//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"]/Custom['
                                              '@ClassName="CommonDialogContent"]') is not None:
            s_step.点击提示框中的_是()
        # 输入项目名称
        s_step.输入项目_组件名称(pj_name="新建测试项目-序列")
        # 选择序列
        n_step.选择序列()
        # 点击创建
        s_step.新建流程or组件项目_点击创建项目()
        if s_step.判断项目是否显示():
            assert n_step.判断序列是否显示()
        else:
            pytest.xfail(reason="创建项目--序列失败")

    @allure.story("新建_新建状态机")
    def test_IDE_新建_新建状态机(self, open_studio):
        """23546#新建页面-新建流程项目#新建状态机#0"""
        """新建_新建状态机"""
        n_step = New_step(open_studio)
        s_step = Start_step(open_studio)
        # 点击流程项目
        n_step.点击新建_流程项目()
        # 判断是否有提示窗口，如果有的话点是
        if ew(open_studio).xianshi_wait(xpath='//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"]/Custom['
                                              '@ClassName="CommonDialogContent"]') is not None:
            s_step.点击提示框中的_是()
        # 输入项目名称
        s_step.输入项目_组件名称(pj_name="新建测试项目-状态机")
        # 选择状态机
        n_step.选择状态机()
        # 点击创建
        s_step.新建流程or组件项目_点击创建项目()
        if s_step.判断项目是否显示():
            assert n_step.判断状态机是否显示()
        else:
            pytest.xfail(reason="创建项目--状态机失败")

    @allure.story("新建_创建UIA项目")
    def test_IDE_新建_创建UIA项目(self, open_studio):
        """23558#新建页面-新建流程项目#新建UIA项目#0"""
        """新建_创建UIA项目"""
        n_step = New_step(open_studio)
        s_step = Start_step(open_studio)
        # 点击流程项目
        n_step.点击新建_流程项目()
        # 判断是否有提示窗口，如果有的话点是
        if ew(open_studio).xianshi_wait(xpath='//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"]/Custom['
                                              '@ClassName="CommonDialogContent"]') is not None:
            s_step.点击提示框中的_是()
        # 输入项目名称
        s_step.输入项目_组件名称(pj_name="新建测试项目-高级设置-UIA")
        # 选择高级设置
        n_step.点击高级设置()
        # 选择UIA
        n_step.选择UIA()
        # 点击创建
        s_step.新建流程or组件项目_点击创建项目()
        if s_step.判断项目是否显示():
            assert n_step.判断项目是否显示()
        else:
            pytest.xfail(reason="创建项目--流程图--高级设置--UIA失败")

    @allure.story("新建_创建UIA3项目")
    def test_IDE_新建_创建UIA3项目(self, open_studio):
        """23559#新建页面-新建流程项目#新建UIA3项目#0"""
        """新建_创建UIA3项目"""
        n_step = New_step(open_studio)
        s_step = Start_step(open_studio)
        # 点击流程项目
        n_step.点击新建_流程项目()
        # 判断是否有提示窗口，如果有的话点是
        if ew(open_studio).xianshi_wait(xpath='//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"]/Custom['
                                              '@ClassName="CommonDialogContent"]') is not None:
            s_step.点击提示框中的_是()
        # 输入项目名称
        s_step.输入项目_组件名称(pj_name="新建测试项目-高级设置-UIA3")
        # 选择高级设置
        n_step.点击高级设置()
        # 选择UIA3
        n_step.选择UIA3()
        # 点击创建
        s_step.新建流程or组件项目_点击创建项目()
        if s_step.判断项目是否显示():
            assert n_step.判断项目是否显示()
        else:
            pytest.xfail(reason="创建项目--流程图--高级设置--UIA失败")

    @allure.story("新建_默认UIA3")
    def test_IDE_新建_默认UIA3(self, open_studio):
        """23560#新建页面-新建流程项目#默认UIA3#0"""
        """新建_默认UIA3"""
        n_step = New_step(open_studio)
        s_step = Start_step(open_studio)
        # 点击流程项目
        n_step.点击新建_流程项目()
        # 判断是否有提示窗口，如果有的话点是
        if ew(open_studio).xianshi_wait(xpath='//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"]/Custom['
                                              '@ClassName="CommonDialogContent"]') is not None:
            s_step.点击提示框中的_是()
        # 输入项目名称
        s_step.输入项目_组件名称(pj_name="新建测试项目-高级设置-UIA3-默认")
        # 选择高级设置
        n_step.点击高级设置()
        assert n_step.判断UIA3的选中状态()
        # 点击关闭
        n_step.点击关闭按钮()

    @allure.story("流程市场-流程详情页-左右切换内容")
    def test_IDE_新建_流程市场_详情页左右切换(self, open_studio):
        """23451#新建页面-流程市场#流程详情页左右切换#0"""
        n_step = New_step(open_studio)
        s_step = Start_step(open_studio)
        # 点击流程市场第一个流程
        n_step.点击流程市场第一个流程()
        # 获取流程标题
        flow_title = open_studio.find_element_by_xpath('//Window[@ClassName="Window"][@Name="流程市场"]/Text[@ClassName="TextBlock"]').text
        # 点击向右按钮 获取新流程标题
        open_studio.find_element_by_xpath('//Window[@ClassName="Window"][@Name="流程市场"]/Button[@AutomationId="NextBtn"]').click()
        time.sleep(0)
        flow_title_right = open_studio.find_element_by_xpath('//Window[@ClassName="Window"][@Name="流程市场"]/Text[@ClassName="TextBlock"]').text
        # 判定新标题不等于原标题 存一个变量，等一起assert
        # 点击向左按钮 获取标题
        open_studio.find_element_by_xpath('//Window[@ClassName="Window"][@Name="流程市场"]/Button[@AutomationId="LastBtn"]').click()
        time.sleep(0)
        # 标题等于第一次获取的标题
        flow_title_left = open_studio.find_element_by_xpath('//Window[@ClassName="Window"][@Name="流程市场"]/Text[@ClassName="TextBlock"]').text
        # 点击关闭详情页
        open_studio.find_element_by_xpath('//Window[@ClassName="Window"][@Name="流程市场"]/Button[@AutomationId="CloseBtn"]/Image[@ClassName="Image"]').click()
        assert flow_title == flow_title_left and flow_title != flow_title_right

    @allure.story("流程市场按标题搜索")
    def test_IDE_新建_流程市场_搜索_按标题搜索(self, open_studio):
        """23464#新建页面-流程市场#按标题搜索#0"""
        # 标题栏输入“Excel文件合并”
        n_step = New_step(open_studio)
        s_step = Start_step(open_studio)
        Clipboard().setText("Excel文件合并")
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: '
                                          'Content:"]/Custom[@ClassName="UCHomeNew"]/Pane[@ClassName="ScrollViewer"]/Custom[@AutomationId="FlowMarketPage"]/Edit['
                                          '@AutomationId="TbSearch"]').send_keys(Keys.CONTROL, 'v')
        time.sleep(0)
        # 点击搜索按钮
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: '
                                          'Content:"]/Custom[@ClassName="UCHomeNew"]/Pane[@ClassName="ScrollViewer"]/Custom[@AutomationId="FlowMarketPage"]/Button['
                                          '@AutomationId="SearchBtn"]').click()
        # 出现结果页面 且 第一个结果标题为Excel文件合并
        result = ew(open_studio).xianshi_wait(xpath='//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem '
                                                    'Header: Content:"]/Custom[@ClassName="UCHomeNew"]/Pane[@ClassName="ScrollViewer"]/Custom['
                                                    '@AutomationId="SearchPage"]') is not None
        title = open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: '
                                                  'Content:"]/Custom[@ClassName="UCHomeNew"]/Pane[@ClassName="ScrollViewer"]/Custom[@AutomationId="SearchPage"]/List['
                                                  '@AutomationId="FlowMarketPackageListBox"]/ListItem[@ClassName="ListBoxItem"]['
                                                  '@Name="BotTime.Studio.Model.PackageExplorerItem"]/Text[@ClassName="TextBlock"]').text
        assert result and str(title) == "Excel文件合并"

    @allure.story("清空搜索显示全部")
    def test_IDE_新建_流程市场_搜索_清空后搜索显示全部(self, open_studio):
        """23468#新建页面-流程市场#清空后搜索显示全部#0"""
        n_step = New_step(open_studio)
        s_step = Start_step(open_studio)
        # 标题栏输入空置
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: '
                                          'Content:"]/Custom[@ClassName="UCHomeNew"]/Pane[@ClassName="ScrollViewer"]/Custom[@AutomationId="SearchPage"]/Edit['
                                          '@AutomationId="TbSearch"]').clear()
        # 点击搜索按钮
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: '
                                          'Content:"]/Custom[@ClassName="UCHomeNew"]/Pane[@ClassName="ScrollViewer"]/Custom[@AutomationId="SearchPage"]/Button['
                                          '@AutomationId="SearchBtn"]').click()
        # 判断 contains 批量发送邮件
        result = ew(open_studio).xianshi_wait(xpath='//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem '
                                                    'Header: '
                                                    'Content:"]/Custom[@ClassName="UCHomeNew"]/Pane[@ClassName="ScrollViewer"]/Custom['
                                                    '@AutomationId="SearchPage"]/List[ '
                                                    '@AutomationId="FlowMarketPackageListBox"]/ListItem[@ClassName="ListBoxItem"]['
                                                    '@Name="BotTime.Studio.Model.PackageExplorerItem"]//*[contains(@Name,"批量发送邮件")]') is not None
        # 点击返回按钮
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: '
                                          'Content:"]/Custom[@ClassName="UCHomeNew"]/Pane[@ClassName="ScrollViewer"]/Custom[@AutomationId="SearchPage"]/Button['
                                          '@AutomationId="BackBtn"]').click()
        assert result

    @allure.story("流程市场搜索点击标签")
    def test_IDE_新建_流程市场_搜索_点击标签(self, open_studio):
        """23470#新建页面-流程市场#点击标签#0"""
        # 点击日常办公标签
        n_step = New_step(open_studio)
        s_step = Start_step(open_studio)
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: '
                                          'Content:"]/Custom[@ClassName="UCHomeNew"]/Pane[@ClassName="ScrollViewer"]/Custom[@AutomationId="FlowMarketPage"]/List['
                                          '@AutomationId="TagListBox"]/ListItem[@ClassName="ListBoxItem"][@Name="日常办公"]/Text[@ClassName="TextBlock"]['
                                          '@Name="日常办公"]').click()
        # 得出结果，点击返回
        result_work = ew(open_studio).xianshi_wait(xpath='//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"]['
                                                         '@Name="System.Windows.Controls.TabItem '
                                                         'Header: '
                                                         'Content:"]/Custom[@ClassName="UCHomeNew"]/Pane[@ClassName="ScrollViewer"]/Custom['
                                                         '@AutomationId="SearchPage"]/List[ '
                                                         '@AutomationId="FlowMarketPackageListBox"]/ListItem[@ClassName="ListBoxItem"]['
                                                         '@Name="BotTime.Studio.Model.PackageExplorerItem"]//*[contains(@Name,"批量发送邮件")]') is not None
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: '
                                          'Content:"]/Custom[@ClassName="UCHomeNew"]/Pane[@ClassName="ScrollViewer"]/Custom[@AutomationId="SearchPage"]/Button['
                                          '@AutomationId="BackBtn"]').click()
        # 点击财务系统标签
        open_studio.find_element_by_xpath(
            '//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: Content:"]/Custom['
            '@ClassName="UCHomeNew"]/Pane[@ClassName="ScrollViewer"]/Custom[@AutomationId="FlowMarketPage"]/List[@AutomationId="TagListBox"]/ListItem['
            '@ClassName="ListBoxItem"][@Name="财务系统"]/Text[@ClassName="TextBlock"][@Name="财务系统"]').click()
        # 得出结果，点击返回
        result_finance = ew(open_studio).xianshi_wait(xpath='//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"]['
                                                            '@Name="System.Windows.Controls.TabItem Header: Content:"]/Custom[@ClassName="UCHomeNew"]/Pane['
                                                            '@ClassName="ScrollViewer"]/Custom[@AutomationId="SearchPage"]/List['
                                                            '@AutomationId="FlowMarketPackageListBox"]/ListItem[@ClassName="ListBoxItem"]['
                                                            '@Name="BotTime.Studio.Model.PackageExplorerItem"]//*[contains(@Name,"SAP开票流程")]') is not None
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: '
                                          'Content:"]/Custom[@ClassName="UCHomeNew"]/Pane[@ClassName="ScrollViewer"]/Custom[@AutomationId="SearchPage"]/Button['
                                          '@AutomationId="BackBtn"]').click()
        # 点击AI操作标签
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: '
                                          'Content:"]/Custom[@ClassName="UCHomeNew"]/Pane[@ClassName="ScrollViewer"]/Custom[@AutomationId="FlowMarketPage"]/List['
                                          '@AutomationId="TagListBox"]/ListItem[@ClassName="ListBoxItem"][@Name="AI操作"]/Text[@ClassName="TextBlock"][@Name="AI操作"]').click()
        # 得出结果，点击返回
        result_ai = ew(open_studio).xianshi_wait(xpath='//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"]['
                                                       '@Name="System.Windows.Controls.TabItem Header: Content:"]/Custom[@ClassName="UCHomeNew"]/Pane['
                                                       '@ClassName="ScrollViewer"]/Custom[@AutomationId="SearchPage"]/List['
                                                       '@AutomationId="FlowMarketPackageListBox"]/ListItem[@ClassName="ListBoxItem"]['
                                                       '@Name="BotTime.Studio.Model.PackageExplorerItem"]//*[contains(@Name,"拼图滑块验证")]') is not None
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: '
                                          'Content:"]/Custom[@ClassName="UCHomeNew"]/Pane[@ClassName="ScrollViewer"]/Custom[@AutomationId="SearchPage"]/Button['
                                          '@AutomationId="BackBtn"]').click()
        assert result_work and result_finance and result_ai

    @allure.story("搜索结果按返回按钮")
    def test_IDE_新建_流程市场_搜索_搜索结果按返回按钮(self, open_studio):
        """23472#新建页面-流程市场#搜索结果按返回按钮#0"""
        n_step = New_step(open_studio)
        s_step = Start_step(open_studio)
        # 点击AI操作标签
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: '
                                          'Content:"]/Custom[@ClassName="UCHomeNew"]/Pane[@ClassName="ScrollViewer"]/Custom[@AutomationId="FlowMarketPage"]/List['
                                          '@AutomationId="TagListBox"]/ListItem[@ClassName="ListBoxItem"][@Name="AI操作"]/Text[@ClassName="TextBlock"][@Name="AI操作"]').click()
        # 得出结果，点击返回
        result_ai = ew(open_studio).xianshi_wait(xpath='//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"]['
                                                       '@Name="System.Windows.Controls.TabItem Header: Content:"]/Custom[@ClassName="UCHomeNew"]/Pane['
                                                       '@ClassName="ScrollViewer"]/Custom[@AutomationId="SearchPage"]/List['
                                                       '@AutomationId="FlowMarketPackageListBox"]/ListItem[@ClassName="ListBoxItem"]['
                                                       '@Name="BotTime.Studio.Model.PackageExplorerItem"]//*[contains(@Name,"拼图滑块验证")]') is not None
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: '
                                          'Content:"]/Custom[@ClassName="UCHomeNew"]/Pane[@ClassName="ScrollViewer"]/Custom[@AutomationId="SearchPage"]/Button['
                                          '@AutomationId="BackBtn"]').click()
        # 验证返回结果
        result = ew(open_studio).xianshi_wait(xpath='//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem '
                                                    'Header: Content:"]/Custom[@ClassName="UCHomeNew"]/Pane[@ClassName="ScrollViewer"]/Custom['
                                                    '@AutomationId="FlowMarketPage"]/Text[@ClassName="TextBlock"][@Name="流程市场"]') is not None
        assert result

    @allure.story("从云扩市场使用最新版本新建一个项目")
    def test_IDE_新建_流程市场_搜索_从云扩市场使用最新版本新建一个项目(self, open_studio):
        """23473#新建页面-流程市场#从云扩市场使用最新版本新建一个项目#0"""
        n_step = New_step(open_studio)
        s_step = Start_step(open_studio)
        # 点击流程市场第一个流程
        n_step.点击流程市场第一个流程()
        # 点击打开按钮
        open_studio.find_element_by_xpath('//Window[@ClassName="Window"][@Name="流程市场"]/Button[@Name="打开"][@AutomationId="OpenBtn"]').click()
        # 判断是否有提示框，如果有点“是”
        if ew(open_studio).xianshi_wait(
                xpath='//Window[@ClassName="Window"][@Name="流程市场"]/Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]') is not None:
            s_step.点击提示框中的_是()
        # 点击创建按钮
        open_studio.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="新建项目"]/Button[@ClassName="Button"][@Name="创建"]/Text[@ClassName="Text"][@Name="创建"]').click()
        # 等待 判断是否创建项目成功
        result = n_step.判断项目是否显示()
        assert result


if __name__ == '__main__':
    pytest.main(['-s', '-v'])
