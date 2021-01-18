#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 17:02
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : test_3_open.py
import os
import shutil
import time
import pytest
import allure
from selenium.webdriver.common.keys import Keys
from test_studio.unit.func.element_wait import Element_wait as ew
from test_studio.unit.step.step import Common_step
from test_studio.unit.test_02_new.test_new import Test_新建侧边栏 as tn
from selenium.webdriver import ActionChains
from test_studio.unit.func.element_clip import Clipboard
from test_studio.unit.step.step import Open_step
from test_studio.unit.step.step import New_step
from test_studio.unit.step.step import Start_step


@allure.feature("侧边栏-【打开】模块")
class Test_打开侧边栏:

    
    @allure.story("打开_最近_搜索项目")
    def test_IDE_打开_最近_搜索项目(self, open_studio):
        """23594#打开页面-最近#搜索项目#0"""
        # 避免执行顺序的影响，新建两个项目，然后查找第一次创建的项目
        s_step = Start_step(open_studio)
        o_step = Open_step(open_studio)
        # 点击新建侧边栏
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: '
                                          'Content:"]/Text['
                                          '@ClassName="TextBlock"][@Name="新建"]').click()
        tn().test_IDE_新建_新建流程图(open_studio=open_studio)
        # 退出，
        # 判断项目是否显示
        if s_step.判断项目是否显示():
            # 退出到开始界面
            s_step.退出到开始界面()
        # 点击新建侧边栏
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: '
                                          'Content:"]/Text['
                                          '@ClassName="TextBlock"][@Name="新建"]').click()
        tn().test_IDE_新建_新建序列(open_studio=open_studio)
        # 判断项目是否显示
        if s_step.判断项目是否显示():
            # 退出到开始界面
            s_step.退出到开始界面()
        # 点击打开
        open_studio.find_element_by_xpath('//*[@AutomationId="tabOpen"]').click()
        # 点击最近使用
        o_step.点击最近使用()
        # 输入框输入“新建测试项目-流程图”
        o_step.搜索框输入关键字(keys="新建测试项目-流程图")
        # 判断第一个包含“新建测试项目-流程图”的元素存在
        result = ew(open_studio).xianshi_wait(xpath='//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                                    '@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/Custom[@ClassName="RecentProjectView"]/List['
                                                    '@AutomationId="LocalProjectListBox"]/ListItem[@ClassName="ListBoxItem"]['
                                                    '@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]//*[contains(@Name,"新建测试项目-流程图")]') is not None
        assert result

    
    @allure.story("打开_最近_按关闭显示全部")
    def test_IDE_打开_最近_按关闭显示全部(self, open_studio):
        """23595#打开页面-最近#按关闭显示全部#0"""
        s_step = Start_step(open_studio)
        # 点击关闭
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                          '@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/Custom[@ClassName="RecentProjectView"]/Image['
                                          '@AutomationId="ClearFilterImage"]').click()
        # 查找序列图
        result = ew(open_studio).xianshi_wait(xpath='//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                                    '@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/Custom[@ClassName="RecentProjectView"]/List['
                                                    '@AutomationId="LocalProjectListBox"]/ListItem[@ClassName="ListBoxItem"]['
                                                    '@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]//*[contains(@Name,"新建测试项目-序列")]') is not None
        assert result

    
    @allure.story("打开_本地项目_切换本地目录")
    def test_IDE_打开_本地项目_切换本地目录(self, open_studio):
        """23596#打开页面-本地项目#切换本地目录#0"""
        s_step = Start_step(open_studio)
        # 点击本地项目
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                          '@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/List[@AutomationId="OpenNavigateListBox"]/ListItem['
                                          '@ClassName="ListBoxItem"][@Name="Encoo.Studio.ViewModel.OpenItem"]/Text[@ClassName="TextBlock"][@Name="本地项目"]').click()
        # 判断浏览
        liulan_button = ew(open_studio).xianshi_wait(xpath='//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: '
                                                           'Content:"][@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/Custom['
                                                           '@ClassName="LocalProjectView"]/Button[@ClassName="Button"][@Name="浏览"]/Text['
                                                           '@ClassName="TextBlock"][@Name="浏览"]') is not None
        assert liulan_button

    
    @allure.story("打开_本地项目_点击打开流程项目")
    def test_IDE_打开_本地项目_点击打开流程项目(self, open_studio):
        """23602#打开页面-本地项目#点击打开流程项目#0"""
        s_step = Start_step(open_studio)
        n_step = New_step(open_studio)
        # 查找“新建测试项目-流程图”并点击
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                          '@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/Custom[@ClassName="LocalProjectView"]/List['
                                          '@AutomationId="LocalProjectListBox"]/ListItem[@ClassName="ListBoxItem"][@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]//*['
                                          'contains(@Name,"新建测试项目-流程图")]').click()
        # 判断是否有关闭项目提示
        if ew(open_studio).xianshi_wait(xpath='//Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]') is not None:
            # 点击提示框中的“是”
            s_step.点击提示框中的_是()
        # 判断项目打开
        result = n_step.判断项目是否显示()
        assert result

    
    @allure.story("打开_本地项目_点击打开组件项目")
    def test_IDE_打开_本地项目_点击打开组件项目(self, open_studio):
        """23603#打开页面-本地项目#点击打开组件项目#0"""
        s_step = Start_step(open_studio)
        # 点击新建侧边栏
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: '
                                          'Content:"]/Text[@ClassName="TextBlock"][@Name="新建"]').click()
        # 新建组件项目
        open_studio.find_element_by_xpath('//Text[@Name="组件项目"][@AutomationId="text"]').click()
        # 判断是否有提示框，如果有点“是”
        if ew(open_studio).xianshi_wait(
                xpath='//Window[@ClassName="Window"]/Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]') is not None:
            # 点击提示框中的“是”
            s_step.点击提示框中的_是()
        # 新建组件项目 - 输入组件项目名称
        open_studio.find_element_by_xpath('//Window[@ClassName="Window"][@Name="新建项目"]/Edit[@AutomationId="txtProjectName"]').send_keys("测试组件")
        # 点击创建
        s_step.新建流程or组件项目_点击创建项目()
        if s_step.判断项目是否显示():
            # 退出到开始界面
            s_step.退出到开始界面()
        # 点击打开
        open_studio.find_element_by_xpath('//*[@AutomationId="tabOpen"]').click()
        # 点击流程图
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                          '@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/Custom[@ClassName="LocalProjectView"]/List['
                                          '@AutomationId="LocalProjectListBox"]/ListItem[@ClassName="ListBoxItem"]['
                                          '@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]//*[contains(@Name,"新建测试项目-流程图")]').click()
        # 判断是否有提示框，如果有点“是”
        if ew(open_studio).xianshi_wait(
                xpath='//Window[@ClassName="Window"]/Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]') is not None:
            # 点击提示框中的“是”
            s_step.点击提示框中的_是()
        # 判断窗口
        if s_step.判断项目是否显示():
            # 退出到开始界面
            s_step.退出到开始界面()
        # 点击打开
        open_studio.find_element_by_xpath('//*[@AutomationId="tabOpen"]').click()
        # 查找“测试组件”并点击
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                          '@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/Custom[@ClassName="LocalProjectView"]/List['
                                          '@AutomationId="LocalProjectListBox"]/ListItem[@ClassName="ListBoxItem"]['
                                          '@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]//*[contains(@Name,"测试组件")]').click()
        # 判断是否有提示框，如果有点“是”
        if ew(open_studio).xianshi_wait(
                xpath='//Window[@ClassName="Window"]/Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]') is not None:
            # 点击提示框中的“是”
            s_step.点击提示框中的_是()
        # 判断项目打开
        result = ew(open_studio).xianshi_wait(xpath='//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Text[@ClassName="TextBlock"][@Name="云扩RPA编辑器"]') is not None
        assert result

    
    @allure.story("打开_本地项目_项目路径不存在_提示是否删除点确定")
    def test_IDE_打开_本地项目_项目路径不存在_提示是否删除点确定(self, open_studio):
        """23604#打开页面-本地项目#项目路径不存在_提示是否删除点确定#0"""
        s_step = Start_step(open_studio)
        # 点击流程图
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                          '@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/Custom[@ClassName="LocalProjectView"]/List['
                                          '@AutomationId="LocalProjectListBox"]/ListItem[@ClassName="ListBoxItem"]['
                                          '@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]//*[contains(@Name,"新建测试项目-流程图")]').click()
        # 判断是否有提示框，如果有点“是”
        if ew(open_studio).xianshi_wait(
                xpath='//Window[@ClassName="Window"]/Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]') is not None:
            # 点击提示框中的“是”
            s_step.点击提示框中的_是()
        # 判断窗口
        if s_step.判断项目是否显示():
            # 退出到开始界面
            s_step.退出到开始界面()
        # 点击打开
        open_studio.find_element_by_xpath('//*[@AutomationId="tabOpen"]').click()
        # 获取路径
        path = open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                                 '@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/Custom[@ClassName="LocalProjectView"]/Edit['
                                                 '@AutomationId="SearchLocalProjectTBox"]').text
        # 删除指定组件项目
        pl_folder_str = eval(repr(path).replace('\\\\', '\\'))
        # 删除指定文件夹
        # 判断文件夹是否存在，若存在，删除
        path_activity = pl_folder_str + r"\测试组件"
        if os.path.exists(path_activity):
            shutil.rmtree(path_activity)
        # 点击组件项目查看是否有提示窗口
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                          '@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/Custom[@ClassName="LocalProjectView"]/List['
                                          '@AutomationId="LocalProjectListBox"]/ListItem[@ClassName="ListBoxItem"]['
                                          '@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]//*[contains(@Name,"测试组件")]').click()
        result = ew(open_studio).xianshi_wait(xpath='//Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]') is not None
        if result:
            open_studio.find_element_by_xpath('//Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]/Button[@ClassName="Button"][@Name="是"]/Text['
                                              '@ClassName="Text"][@Name="是"]').click()
            # open_studio.find_element_by_xpath('//Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]/Button[@ClassName="Button"][@Name="是"]/Text['
            #                                   '@ClassName="Text"][@Name="是"]').click()
        assert result

    
    @allure.story("打开_本地项目_已打开其它项目_点击提示是否关闭项目选是")
    def test_IDE_打开_本地项目_已打开其它项目_点击提示是否关闭项目选是(self, open_studio):
        """23606#打开页面-本地项目#已打开其它项目_点击提示是否关闭项目选是#0"""
        s_step = Start_step(open_studio)
        # 点击新建测试项目-流程图
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                          '@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/Custom[@ClassName="LocalProjectView"]/List['
                                          '@AutomationId="LocalProjectListBox"]/ListItem[@ClassName="ListBoxItem"]['
                                          '@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]//*[contains(@Name,"新建测试项目-流程图")]').click()
        if s_step.判断项目是否显示():
            # 退出到开始界面
            s_step.退出到开始界面()
        # 点击打开
        open_studio.find_element_by_xpath('//*[@AutomationId="tabOpen"]').click()
        # 点击新建测试项目-序列
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                          '@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/Custom[@ClassName="LocalProjectView"]/List['
                                          '@AutomationId="LocalProjectListBox"]/ListItem[@ClassName="ListBoxItem"]['
                                          '@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]//*[contains(@Name,"新建测试项目-序列")]').click()
        # 判断是否有关闭项目提示
        xulie_result = ew(open_studio).xianshi_wait(xpath='//Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]') is not None
        # 提示框点否
        if xulie_result:
            open_studio.find_element_by_xpath('//Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]/Button[@ClassName="Button"][@Name="是"]/Text['
                                              '@ClassName="Text"][@Name="是"]').click()
        # 判断跳转，退回到打开页面
        if s_step.判断项目是否显示():
            # 退出到开始界面
            s_step.退出到开始界面()
        # 点击打开
        open_studio.find_element_by_xpath('//*[@AutomationId="tabOpen"]').click()
        assert xulie_result

    
    @allure.story("打开_本地项目_已打开其它项目_点击提示是否关闭项目选否")
    def test_IDE_打开_本地项目_已打开其它项目_点击提示是否关闭项目选否(self, open_studio):
        """23607#打开页面-本地项目#已打开其它项目_点击提示是否关闭项目选否#0"""
        s_step = Start_step(open_studio)
        # 点击新建测试项目-流程图
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                          '@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/Custom[@ClassName="LocalProjectView"]/List['
                                          '@AutomationId="LocalProjectListBox"]/ListItem[@ClassName="ListBoxItem"]['
                                          '@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]//*[contains(@Name,"新建测试项目-流程图")]').click()
        # 判断是否有关闭项目提示
        liucheng_result = ew(open_studio).xianshi_wait(xpath='//Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]') is not None
        # 提示框点否
        if liucheng_result:
            open_studio.find_element_by_xpath('//Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]/Button[@ClassName="Button"][@Name="否"]/Text['
                                              '@ClassName="Text"][@Name="否"]').click()
        # 点击新建测试项目-序列
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                          '@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/Custom[@ClassName="LocalProjectView"]/List['
                                          '@AutomationId="LocalProjectListBox"]/ListItem[@ClassName="ListBoxItem"]['
                                          '@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]//*[contains(@Name,"新建测试项目-序列")]').click()
        # 判断是否有关闭项目提示
        xulie_result = ew(open_studio).xianshi_wait(xpath='//Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]') is not None
        # 提示框点否
        if xulie_result:
            open_studio.find_element_by_xpath('//Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]/Button[@ClassName="Button"][@Name="否"]/Text['
                                              '@ClassName="Text"][@Name="否"]').click()
        assert liucheng_result or xulie_result

    
    @allure.story("打开_本地项目_已打开其它项目且未保存_提示是否保存选确定")
    def test_IDE_打开_本地项目_已打开其它项目且未保存_提示是否保存选确定(self, open_studio):
        """23608#打开页面-本地项目#已打开其它项目且未保存_提示是否保存选确定#0"""
        s_step = Start_step(open_studio)
        o_step = Open_step(open_studio)
        # 点击开始侧边栏
        open_studio.find_element_by_xpath('//*[@AutomationId="tabStart"]').click()
        s_step.点击新建流程项目()
        # 判断是否有提示框，如果有点“是”
        if ew(open_studio).xianshi_wait(
                xpath='//Window[@ClassName="Window"]/Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]') is not None:
            # 点击提示框中的“是”
            s_step.点击提示框中的_是()
        # 新建组件项目 - 输入组件项目名称
        s_step.输入项目_组件名称(pj_name='测试项目', )
        # 点击创建
        s_step.新建流程or组件项目_点击创建项目()
        if s_step.判断项目是否显示():
            # 编辑项目内容
            # 【开始】按住拖动
            # 选择拖动的节点
            start_button = open_studio.find_element_by_xpath('//Pane[@ClassName="Pane"][@Name="AddIn"]/Custom[starts-with(@AutomationId,"UserControl_")]/Pane['
                                                             '@AutomationId="scrollViewer"]/Custom[@Name="ActivityBuilder"]['
                                                             '@AutomationId="ActivityTypeDesigner"]/Custom[@Name="Flowchart"]['
                                                             '@AutomationId="WorkflowItemPresenter"]/Custom[@Name="Flowchart"][@AutomationId="Flowchart('
                                                             'FlowchartDesigner)"]/Custom[@Name="StartNode"][@AutomationId="StartSymbol"]/Text[@Name="Start"]['
                                                             'starts-with(@AutomationId,"TextBlock_")]')
            # 鼠标滑动操作
            action = ActionChains(open_studio)
            # 按住鼠标左键
            action.click_and_hold(start_button)
            # 相对鼠标位置移动一点距离
            action.move_by_offset(100, 0)
            # 释放鼠标
            action.release()
            # 执行动作
            action.perform()
            # 退出到开始界面
            s_step.退出到开始界面()
        # 点击 - 打开 - 本地项目 - 其他项目
        o_step.点击打开侧边栏()
        # 点击新建测试项目-流程图
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                          '@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/Custom[@ClassName="LocalProjectView"]/List['
                                          '@AutomationId="LocalProjectListBox"]/ListItem[@ClassName="ListBoxItem"]['
                                          '@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]//*[contains(@Name,"新建测试项目-流程图")]').click()
        # 查看是否有保存提示框
        close_confirm = ew(open_studio).xianshi_wait(xpath='//Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]') is not None
        if close_confirm:
            open_studio.find_element_by_xpath('//Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]/Button[@ClassName="Button"][@Name="是"]/Text['
                                              '@ClassName="Text"][@Name="是"]').click()
            # 保存框点是
            save_confirm = ew(open_studio).xianshi_wait(xpath='//Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]') is not None
            if save_confirm:
                open_studio.find_element_by_xpath(
                    '//Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]/Button[@ClassName="Button"][@Name="是"]/Text[@ClassName="Text"][@Name="是"]').click()
                assert save_confirm
            else:
                pytest.xfail(reason="没有保存确认框")
        else:
            pytest.xfail(reason="没有关闭确认框")

    
    @allure.story("打开_本地项目_已打开其它项目且未保存_提示是否保存选取消或关闭")
    def test_IDE_打开_本地项目_已打开其它项目且未保存_提示是否保存选取消或关闭(self, open_studio):
        """23609#打开页面-本地项目#已打开其它项目且未保存_提示是否保存选取消或关闭#0"""
        s_step = Start_step(open_studio)
        o_step = Open_step(open_studio)
        # 点击测试项目
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                          '@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/Custom[@ClassName="LocalProjectView"]/List['
                                          '@AutomationId="LocalProjectListBox"]/ListItem[@ClassName="ListBoxItem"]['
                                          '@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]//*[contains(@Name,"测试项目-流程图")]').click()
        # 查看是否有关闭提示框
        close_confirm = ew(open_studio).xianshi_wait(xpath='//Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]') is not None
        if close_confirm:
            open_studio.find_element_by_xpath('//Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]/Button[@ClassName="Button"][@Name="是"]/Text['
                                              '@ClassName="Text"][@Name="是"]').click()
        if s_step.判断项目是否显示():
            # 【开始】按住拖动
            time.sleep(5)
            # 选择拖动的节点
            start_button = open_studio.find_element_by_xpath('//Pane[@ClassName="Pane"][@Name="AddIn"]/Custom[starts-with(@AutomationId,"UserControl_")]/Pane['
                                                             '@AutomationId="scrollViewer"]/Custom[@Name="ActivityBuilder"]['
                                                             '@AutomationId="ActivityTypeDesigner"]/Custom[@Name="Flowchart"]['
                                                             '@AutomationId="WorkflowItemPresenter"]/Custom[@Name="Flowchart"][@AutomationId="Flowchart('
                                                             'FlowchartDesigner)"]/Custom[@Name="StartNode"][@AutomationId="StartSymbol"]/Text[@Name="Start"]['
                                                             'starts-with(@AutomationId,"TextBlock_")]')
            # 鼠标滑动操作
            action = ActionChains(open_studio)
            # 按住鼠标左键
            action.click_and_hold(start_button)
            # 相对鼠标位置移动一点距离
            action.move_by_offset(100, 0)
            # 释放鼠标
            action.release()
            # 执行动作
            action.perform()
            # 退出到开始界面
            s_step.退出到开始界面()
        # 点击 - 打开 - 本地项目 - 其他项目
        o_step.点击打开侧边栏()
        # 点击新建测试项目-流程图
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                          '@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/Custom[@ClassName="LocalProjectView"]/List['
                                          '@AutomationId="LocalProjectListBox"]/ListItem[@ClassName="ListBoxItem"]['
                                          '@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]//*[contains(@Name,"新建测试项目-序列")]').click()
        # 查看是否有保存提示框
        close_confirm = ew(open_studio).xianshi_wait(xpath='//Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]') is not None
        if close_confirm:
            open_studio.find_element_by_xpath('//Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]/Button[@ClassName="Button"][@Name="是"]/Text['
                                              '@ClassName="Text"][@Name="是"]').click()
            # 保存框点否
            unsave_confirm = ew(open_studio).xianshi_wait(xpath='//Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]') is not None
            if unsave_confirm:
                open_studio.find_element_by_xpath(
                    '//Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]/Button[@ClassName="Button"][@Name="否"]/Text[@ClassName="Text"]['
                    '@Name="否"]').click()
                assert unsave_confirm
            else:
                pytest.xfail(reason="没有保存确认框")
        else:
            pytest.xfail(reason="没有关闭确认框")

    
    @allure.story("打开_导入_导入打开项目")
    def test_IDE_打开_导入_导入打开项目(self, open_studio):
        """23611#打开页面-导入#导入打开项目#0"""
        """
        选择一个流程图项目，
        进入编辑页面，
        点击文件-导出项目，获取弹出框中文件路径，选择导出
        点击开始，点击打开
        点击导入，文件地址栏填入路径
        提示框点击是
        判断是否打开项目
        """
        # 点击测试项目
        s_step = Start_step(open_studio)
        o_step = Open_step(open_studio)
        open_studio.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                          '@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/Custom[@ClassName="LocalProjectView"]/List['
                                          '@AutomationId="LocalProjectListBox"]/ListItem[@ClassName="ListBoxItem"]['
                                          '@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]//*[contains(@Name,"测试项目")]').click()
        # 查看是否有关闭提示框
        close_confirm = ew(open_studio).xianshi_wait(xpath='//Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]') is not None
        if close_confirm:
            open_studio.find_element_by_xpath('//Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]/Button[@ClassName="Button"][@Name="是"]/Text['
                                              '@ClassName="Text"][@Name="是"]').click()
        # 导出的dgs路径
        global fold_path
        if s_step.判断项目是否显示():
            # 文件
            open_studio.find_element_by_xpath(
                '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Menu[@ClassName="Menu"]/MenuItem[@ClassName="MenuItem"][@Name="文件"]/Text[@ClassName="TextBlock"][@Name="文件"]').click()
            # 导出项目
            open_studio.find_element_by_xpath('//Window[@ClassName="Popup"]/MenuItem[@ClassName="MenuItem"]/Text[@ClassName="TextBlock"][@Name="导出项目"]').click()
            # 文件路径
            fold_path = open_studio.find_element_by_xpath('//Window[@ClassName="Window"][@Name="导出项目"]/Edit[@AutomationId="FilePathTxt"]').text
            # 点击导出按钮
            open_studio.find_element_by_xpath(
                '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"][@Name="导出项目"]/Button[@AutomationId="Btn_export"]/Text[@ClassName="Text"]').click()
            # 退出到开始界面
            s_step.退出到开始界面()
        o_step.点击打开侧边栏()
        # 点击导入按钮
        open_studio.find_element_by_xpath(
            '//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"][@AutomationId="tabOpen"]/Custom['
            '@AutomationId="openView"]/Custom[@ClassName="LocalProjectView"]/Button[@AutomationId="ImportProjectBtn"]').click()
        # 输入文件路径
        # fold_path_new = eval(repr(fold_path).replace('\\\\', '\\'))
        fold_path_new = fold_path
        Clipboard().setText(fold_path_new)
        open_studio.find_element_by_xpath('//Window[@ClassName="Window"][@Name="导入项目"]/Edit[@AutomationId="PositionTxt"]').send_keys(Keys.CONTROL, 'v')
        # 点击导入
        open_studio.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"][@Name="导入项目"]/Button[@AutomationId="btnImport"]/Text[@ClassName="Text"]').click()
        # 查看是否有关闭提示框
        close_confirm = ew(open_studio).xianshi_wait(xpath='//Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]') is not None
        if close_confirm:
            open_studio.find_element_by_xpath('//Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]/Button[@ClassName="Button"][@Name="是"]/Text['
                                              '@ClassName="Text"][@Name="是"]').click()
        # 判断项目打开
        result = s_step.判断项目是否显示()
        assert result

    @allure.story("打开_导入_切换位置后_导入的位置更新")
    def test_IDE_打开_导入_切换位置后_导入的位置更新(self, open_studio):
        """23627#打开页面-导入#切换位置后_导入的位置更新#0"""
        """
        点击浏览
        判断文件夹有无，若无，新建文件夹
        点击切换到新建的文件夹 EncooTest1
        点击选择文件夹
        点击导入
        点击浏览
        出现“没有与搜索条件匹配的项” 【判断】
        再切换到有项目的文件夹
        """
        s_step = Start_step(open_studio)
        path = r'C:\EncooTest1'
        path_new = r'C:\EncooTest'
        step = Common_step(open_studio)
        o_step = Open_step(open_studio)

        step.click_browse()
        step.mkdir(path=path)
        step.choose_new_folder(path=path)
        step.click_import()
        step.click_import_browse()
        result = ew(open_studio).xianshi_wait(xpath='//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"][@Name="导入项目"]/Window['
                                                    '@ClassName="#32770"][@Name="打开"]/Pane[@ClassName="DUIViewWndClassName"]/Pane[@Name="Shell 文件夹视图"]['
                                                    '@AutomationId="listview"]/List[@ClassName="UIItemsView"][@Name="项目视图"]/Text[@Name="没有与搜索条件匹配的项。"]['
                                                    '@AutomationId="EmptyText"]') is not None
        o_step.click_cancle()
        step.click_browse()
        step.choose_new_folder(path=path_new)
        assert result


if __name__ == "__main__":
    pytest.main(['-s', '-v'])
