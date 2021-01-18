#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/19 16:12
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : step.py
import os
import random
import time
from selenium.webdriver import ActionChains  # 鼠标右键
import win32api, win32con  # 鼠标滚动
from selenium.webdriver.common.keys import Keys
import allure
from test_studio.unit.func.element_clip import Clipboard
from test_studio.unit.func.file_exist import FileAndFolder
from test_studio.unit.func.element_wait import Element_wait as ew
from test_studio.unit.func.element_exist import Element_exist as ee


# region 公共模块步骤
class Common_step():
    """父类"""

    def __init__(self, open_studio):
        self.driver = open_studio

    project_path = r'C:\EncooTest'

    @allure.step("切换窗口")
    def switch_window(self):
        """切换到Studio窗口"""
        try:
            time.sleep(3)
            self.driver.switch_to.window(self.driver.window_handles[0])  # 绑定到最新打开的窗口
        except:
            self.switch_window(self.driver)

    @allure.step("点击浏览按钮")
    def click_browse(self):
        """点击浏览按钮"""
        self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"][@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/Custom[@ClassName="LocalProjectView"]/Button[@ClassName="Button"][@Name="浏览"]').click()
        print("点击浏览按钮")

    @allure.step("新建文件夹")
    def mkdir(self, path):
        """新建文件夹"""
        FileAndFolder().mkdir(path=path)

    @allure.step("选择新建的文件夹路径")
    def choose_new_folder(self, path):
        """
        选择新建的文件夹路径
        :param driver:
        :param path: 文件夹路径
        :return:
        """

        if "1" in path:
            self.driver.find_element_by_xpath(
                '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="#32770"][@Name="选择文件夹"]/Pane[@ClassName="ReBarWindow32"]/Pane[@ClassName="Address Band Root"]/ProgressBar[@ClassName="msctls_progress32"]/Pane[@ClassName="Breadcrumb Parent"]/ToolBar[@ClassName="ToolbarWindow32"][@Name="地址: C:\\EncooTest"]/SplitButton[@Name="所有位置"]').click()
        else:
            self.driver.find_element_by_xpath(
                '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="#32770"][@Name="选择文件夹"]/Pane[@ClassName="ReBarWindow32"]/Pane[@ClassName="Address '
                'Band Root"]/ProgressBar[@ClassName="msctls_progress32"]/Pane[@ClassName="Breadcrumb Parent"]/ToolBar[@ClassName="ToolbarWindow32"][@Name="地址: C:\\EncooTest1"]/SplitButton[@Name="所有位置"]').click()
        Clipboard.setText(path)
        self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="#32770"][@Name="选择文件夹"]/Pane[@ClassName="ReBarWindow32"]/Pane['
            '@ClassName="Address Band Root"]/ProgressBar[@ClassName="msctls_progress32"]/ComboBox[@ClassName="ComboBox"][@Name="地址"]/Edit['
            '@ClassName="Edit"][@Name="地址"]').send_keys(Keys.CONTROL, 'v')
        self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="#32770"][@Name="选择文件夹"]/Pane[@ClassName="ReBarWindow32"]/Pane['
            '@ClassName="Address Band Root"]/ProgressBar[@ClassName="msctls_progress32"]/ComboBox[@ClassName="ComboBox"][@Name="地址"]/Edit['
            '@ClassName="Edit"][@Name="地址"]').send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="#32770"][@Name="选择文件夹"]/Button[@ClassName="Button"]['
                                          '@Name="选择文件夹"]').click()

    @allure.step("点击导入按钮")
    def click_import(self):
        """点击导入按钮"""
        self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"][@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/Custom[@ClassName="LocalProjectView"]/Button[@AutomationId="ImportProjectBtn"]').click()
        print("点击导入按钮")

    @allure.step("导入-点击浏览按钮")
    def click_import_browse(self):
        """导入-点击浏览按钮"""
        self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"][@Name="导入项目"]/Button[@ClassName="Button"][@Name="浏览"]').click()
        print("导入-点击浏览按钮")

    @allure.step("点击编辑器菜单栏开始按钮")
    def click_edit_start(self):
        """点击编辑器菜单栏开始按钮"""
        self.driver.find_element_by_xpath('//Menu[@AutomationId="startMenu"]/MenuItem[@ClassName="MenuItem"]/Text[@ClassName="TextBlock"][@Name="开始"]').click()

    @allure.step("点击右键")
    def right_click(self, element):
        """点击鼠标右键"""
        rightClick = ActionChains(self.driver)
        rightClick.context_click(element).perform()

    @allure.step("鼠标向下滚动")
    def mouse_grow_down(self, unit=5):
        """鼠标向下滚动"""
        try:
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -unit)
        except:
            pass

    @allure.step("鼠标移动到指定元素")
    def mouse_moveto(self, target):
        ActionChains(self.driver).move_to_element(target).perform()

    @allure.step("判断是否有弹出框")
    def is_show_yn_dialog(self):
        """判断是否有弹出框"""
        try:
            if ew(self.driver).xianshi_wait(
                    xpath='//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]') is not None:
                return True
            else:
                return False
        except:
            return False


# endregion
# region 安装模块步骤
class Install_step(Common_step):
    """下载安装步骤:继承公共父类"""

    def __init__(self, open_studio):
        super().__init__(open_studio)
        self.driver = open_studio

    @allure.step("判断许可证是否显示")
    def is_permit_show(self):
        """判断许可证是否显示"""
        try:
            time.sleep(3)
            print("判断许可证是否显示")
            if ew(self.driver).xianshi_wait(
                    xpath='//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="ActivationWindow"]/Custom[@ClassName="UserControl"]/Button[@Name="使用许可证激活"][@AutomationId="btn_license"]/Text[@ClassName="Text"][@Name="使用许可证激活"]') is not None:
                return True
            else:
                return False
        except:
            return False

    @allure.step("使用许可证激活")
    def use_permit_active(self, qi_licence):
        """使用许可证激活"""
        self.driver.find_element_by_xpath(
            '//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="ActivationWindow"]/Custom[@ClassName="UserControl"]/Button[@Name="使用许可证激活"][@AutomationId="btn_license"]/Text[@ClassName="Text"][@Name="使用许可证激活"]').click()
        time.sleep(3)
        Clipboard().setText(qi_licence)
        self.driver.find_element_by_xpath(
            '//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="ActivationWindow"]/Window[@ClassName="Window"]/Edit[@ClassName="TextBox"]/Edit[@AutomationId="textBox"]').send_keys(
            Keys.CONTROL, "v")
        self.driver.find_element_by_xpath('//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="ActivationWindow"]/Window[@ClassName="Window"]/Button['
                                          '@ClassName="Button"][@Name="激活"]/Text[@ClassName="Text"][@Name="激活"]').click()


# endregion
# region 开始模块步骤
class Start_step(Common_step):
    """开始步骤:继承公共父类"""

    def __init__(self, open_studio):
        super().__init__(open_studio)
        self.driver = open_studio

    @allure.step("输入项目路径")
    def enter_project_path(self):
        """输入项目路径"""
        try:
            self.driver.find_element_by_xpath(
                '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"][@Name="新建项目"]/Button[@ClassName="Button"][@Name="浏览"]').click()
            FileAndFolder().mkdir(self.project_path)
            self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"][@Name="新建项目"]/Window[@ClassName="#32770"]['
                                              '@Name="选择文件夹"]/Pane[@ClassName="ReBarWindow32"]/Pane[@ClassName="Address Band Root"]/ProgressBar[@ClassName="msctls_progress32"]/Pane[@ClassName="Breadcrumb Parent"]/ToolBar[@ClassName="ToolbarWindow32"]//SplitButton[@Name="所有位置"]').click()
            Clipboard.setText(self.project_path)
            self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"][@Name="新建项目"]/Window[@ClassName="#32770"]['
                                              '@Name="选择文件夹"]/Pane[@ClassName="ReBarWindow32"]/Pane[@ClassName="Address Band Root"]/ProgressBar['
                                              '@ClassName="msctls_progress32"]/ComboBox[@ClassName="ComboBox"][@Name="地址"]/Edit[@ClassName="Edit"][@Name="地址"]').send_keys(
                Keys.CONTROL, 'v')
            self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"][@Name="新建项目"]/Window[@ClassName="#32770"]['
                                              '@Name="选择文件夹"]/Pane[@ClassName="ReBarWindow32"]/Pane[@ClassName="Address Band Root"]/ProgressBar['
                                              '@ClassName="msctls_progress32"]/ComboBox[@ClassName="ComboBox"][@Name="地址"]/Edit[@ClassName="Edit"][@Name="地址"]').send_keys(
                Keys.ENTER)
        except:
            pass
        finally:
            self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"][@Name="新建项目"]/Window[@ClassName="#32770"]['
                                              '@Name="选择文件夹"]/Button[@ClassName="Button"][@Name="选择文件夹"]').click()

    @allure.step('点击新建流程项目')
    def 点击新建流程项目(self):
        """点击新建流程项目"""
        self.driver.find_element_by_xpath(
            '//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"][@AutomationId="tabStart"]/Custom['
            '@ClassName="UCHomeStart"]/List[@ClassName="ListBox"]/ListItem[@ClassName="ListBoxItem"][@Name="Encoo.Studio.Model.HomePage.HomeStartNewModel"]/Text['
            '@Name="流程项目"][@AutomationId="text"]').click()
        print("点击新建流程项目")
        time.sleep(0)

    @allure.step('输入项目名称')
    def 输入项目_组件名称(self, pj_name):
        """输入项目名称"""
        self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="新建项目"]/Edit[@AutomationId="txtProjectName"]').send_keys(
            pj_name + str(random.randint(10, 999)))
        print("输入项目名称")
        time.sleep(0)

    @allure.step('新建流程or组件项目_点击创建项目')
    def 新建流程or组件项目_点击创建项目(self):
        """新建流程or组件项目_点击创建项目"""
        self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"][@Name="新建项目"]/Button[@ClassName="Button"][@Name="创建"]/Text[@ClassName="Text"][@Name="创建"]').click()
        print("新建流程or组件项目_点击创建项目")
        time.sleep(0)

    @allure.step('判断项目是否显示')
    def 判断项目是否显示(self):
        """判断项目是否显示"""
        try:
            time.sleep(3)
            print("判断项目是否显示")
            if ew(self.driver).xianshi_wait(
                    xpath='//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Pane[@ClassName="Pane"][@Name="AddIn"]/Custom[@Name="属性窗口"][@AutomationId="PropertyInspector"]/Text[@Name="ActivityBuilder"][starts-with(@AutomationId,"TextBlock_")]') is not None:
                return True
            else:
                return False
        except:
            return False

    @allure.step('退出到开始界面')
    def 退出到开始界面(self):
        """退出到开始界面"""
        self.driver.find_element_by_xpath('//Menu[@AutomationId="startMenu"]/MenuItem[@ClassName="MenuItem"]/Text[@ClassName="TextBlock"][@Name="开始"]').click()
        print("退出到开始界面")
        time.sleep(0)

    @allure.step('新建组件项目')
    def 新建组件项目(self):
        """新建组件项目"""
        self.driver.find_element_by_xpath(
            '//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"][@AutomationId="tabStart"]/Custom['
            '@ClassName="UCHomeStart"]/List[@ClassName="ListBox"]/ListItem[@ClassName="ListBoxItem"][@Name="Encoo.Studio.Model.HomePage.HomeStartNewModel"]/Text['
            '@Name="组件项目"][@AutomationId="text"]').click()
        print("退出到开始界面")
        time.sleep(0)

    @allure.step('点击提示框中的_是')
    def 点击提示框中的_是(self):
        """点击提示框中的_是"""
        self.driver.find_element_by_xpath('//Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]/Button[@ClassName="Button"][@Name="是"]/Text['
                                          '@ClassName="Text"][@Name="是"]').click()
        print("点击提示框中的_是")
        time.sleep(0)

    @allure.step('点击最近列表测试项目')
    def 点击测试项目(self):
        """点击最近列表测试项目"""
        self.driver.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                          '@AutomationId="tabStart"]/Custom[@ClassName="UCHomeStart"]/List[@AutomationId="LocalProjectListBox"]/ListItem['
                                          '@ClassName="ListBoxItem"][@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]/Text[@ClassName="TextBlock"][starts-with(@Name,'
                                          '"测试项目")]').click()
        print("点击最近列表测试项目")
        time.sleep(0)

    @allure.step('点击最近列表组件项目')
    def 点击组件项目(self):
        """点击最近列表组件项目"""
        self.driver.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                          '@AutomationId="tabStart"]/Custom[@ClassName="UCHomeStart"]/List[@AutomationId="LocalProjectListBox"]/ListItem['
                                          '@ClassName="ListBoxItem"][@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]/Text[@ClassName="TextBlock"][starts-with(@Name,'
                                          '"测试组件")]').click()
        print("点击最近列表组件项目")
        time.sleep(0)

    @allure.step('点击最近列表指定名称项目')
    def 点击最近列表项目_by_name(self, pj_name):
        """点击最近列表指定名称项目"""
        self.driver.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                          '@AutomationId="tabStart"]/Custom[@ClassName="UCHomeStart"]/List[@AutomationId="LocalProjectListBox"]/ListItem['
                                          '@ClassName="ListBoxItem"][@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]/Text[@ClassName="TextBlock"][starts-with(@Name,'
                                          f'"{pj_name}")]').click()
        print("点击最近列表指定名称项目")
        time.sleep(0)

        # @allure.step('点击最近列表删除按钮')
        # def 点击最近列表删除按钮(self):
        #     """点击最近列表删除按钮"""
        #     driver.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
        #                                  '@AutomationId="tabStart"]/Custom[@ClassName="UCHomeStart"]/List[@AutomationId="LocalProjectListBox"]/ListItem['
        #                                  '@ClassName="ListBoxItem"][@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]/Text[@ClassName="TextBlock"][starts-with(@Name,'
        #                                  '"测试组件")]').click()
        print("点击最近列表删除按钮")
        time.sleep(0)

    @allure.step('判断最近列表测试项目或测试组件是否显示')
    def 判断最近列表测试项目或测试组件是否显示(self):
        """判断最近列表测试项目或测试组件是否显示"""
        print("判断最近列表测试项目或测试组件是否显示")
        if ew(self.driver).xianshi_wait(xpath='//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                              '@AutomationId="tabStart"]/Custom[@ClassName="UCHomeStart"]/List[@AutomationId="LocalProjectListBox"]/ListItem['
                                              '@ClassName="ListBoxItem"][@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]/Text[@ClassName="TextBlock"][starts-with('
                                              '@Name, "测试")]') is not None:
            return True
        else:
            return False


# endregion
# region 新建模块步骤

class New_step(Common_step):
    """新建步骤：继承公共父类"""

    def __init__(self, open_studio):
        super().__init__(open_studio)
        self.driver = open_studio

    @allure.step("切换到新建页面")
    def change_to_new(self):
        """切换到新建页面"""
        """点击新建"""
        flag = ee(self.driver).isElementCanClick(xpath='//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: '
                                                       'Content:"]/Text['
                                                       '@ClassName="TextBlock"][@Name="新建"]')
        # 判断是否在项目编辑页面
        if flag is False:
            self.driver.find_element_by_xpath('//Menu[@AutomationId="startMenu"]/MenuItem[@ClassName="MenuItem"]').click()
            self.driver.find_element_by_xpath(
                '//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: Content:"]/Text['
                '@ClassName="TextBlock"][@Name="新建"]').click()
        else:
            self.driver.find_element_by_xpath(
                '//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: Content:"]/Text['
                '@ClassName="TextBlock"][@Name="新建"]').click()

    @allure.step("新建流程项目")
    def 点击新建_流程项目(self):
        """点击新建_流程项目"""
        self.driver.find_element_by_xpath(
            '//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: Content:"]/Custom['
            '@ClassName="UCHomeNew"]/Pane[@ClassName="ScrollViewer"]/List[@ClassName="ListBox"]/ListItem[@ClassName="ListBoxItem"]['
            '@Name="Encoo.Studio.Model.HomePage.HomeStartNewModel"]/Text[@Name="流程项目"][@AutomationId="text"]').click()
        time.sleep(0)

    @allure.step("选择流程图")
    def 选择流程图(self):
        self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="新建项目"]/RadioButton[@Name="流程图"][@AutomationId="rdFlowchart"]').click()
        time.sleep(0)

    @allure.step("选择序列")
    def 选择序列(self):
        self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="新建项目"]/RadioButton[@Name="序列"][@AutomationId="rdSequence"]').click()
        time.sleep(0)

    @allure.step("选择状态机")
    def 选择状态机(self):
        self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="新建项目"]/RadioButton[@Name="状态机"][@AutomationId="rdStateMachine"]').click()
        time.sleep(0)

    @allure.step("判断状态机是否正常显示")
    def 判断状态机是否显示(self):
        if ew(self.driver).xianshi_wait(xpath='//Pane[@ClassName="Pane"][@Name="AddIn"]/Custom[starts-with(@AutomationId,"UserControl_")]/Pane['
                                              '@AutomationId="scrollViewer"]/Custom[@Name="ActivityBuilder"]['
                                              '@AutomationId="ActivityTypeDesigner"]/Custom[@Name="StateMachine"]['
                                              '@AutomationId="WorkflowItemPresenter"]/Custom[@Name="StateMachine"][@AutomationId="StateMachine('
                                              'StateMachineDesigner)"]/Custom[@AutomationId="stateContainerEditor"]/Custom[@Name="State"]['
                                              '@AutomationId="FinalState(StateDesigner)"]') is not None:
            return True
        else:
            return False

    @allure.step("判断项目是否正常显示")
    def 判断项目是否显示(self):
        time.sleep(3)
        try:
            if ew(self.driver).xianshi_wait(xpath='//Pane[@ClassName="Pane"][@Name="AddIn"]/Custom[starts-with(@AutomationId,"UserControl_")]/Pane['
                                                  '@AutomationId="scrollViewer"]/Custom[@Name="ActivityBuilder"][@AutomationId="ActivityTypeDesigner"]/Custom['
                                                  '@Name="Flowchart"][@AutomationId="WorkflowItemPresenter"]/Custom[@Name="Flowchart"][@AutomationId="Flowchart('
                                                  'FlowchartDesigner)"]/Custom[@Name="StartNode"][@AutomationId="StartSymbol"]/Text[@Name="Start"][starts-with('
                                                  '@AutomationId,"TextBlock_")]', second=20) is not None:
                return True
            else:
                return False
        except:
            return False

    @allure.step("判断序列是否正常显示")
    def 判断序列是否显示(self):
        if ew(self.driver).xianshi_wait(xpath='//Pane[@ClassName="Pane"][@Name="AddIn"]/Custom[starts-with(@AutomationId,"UserControl_")]/Pane['
                                              '@AutomationId="scrollViewer"]/Custom[@Name="ActivityBuilder"][@AutomationId="ActivityTypeDesigner"]/Custom['
                                              '@Name="Sequence"][@AutomationId="WorkflowItemPresenter"]/Custom[@Name="Sequence"][@AutomationId="Sequence('
                                              'SequenceDesigner)"]/Custom[@Name="Sequence"][@AutomationId="DisplayNameReadOnlyControl"]') is not None:
            return True
        else:
            return False

    @allure.step("点击高级设置")
    def 点击高级设置(self):
        self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="新建项目"]/Text[@ClassName="TextBlock"][@Name="高级设置"]').click()
        time.sleep(0)

    @allure.step("选择UIA3")
    def 选择UIA3(self):
        self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="新建项目"]/RadioButton[@Name="UIA3（推荐）"][starts-with(@AutomationId,"rdUIA")]').click()
        time.sleep(0)

    @allure.step("选择UIA")
    def 选择UIA(self):
        self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="新建项目"]/RadioButton[@Name="UIA"][@AutomationId="rdUIA"]').click()
        time.sleep(0)

    @allure.step("判断UIA3的选中状态")
    def 判断UIA3的选中状态(self):
        return self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="新建项目"]/RadioButton[@Name="UIA3（推荐）"][starts-with(@AutomationId,"rdUIA")]').is_selected()

    @allure.step("点击流程市场第一个流程")
    def 点击流程市场第一个流程(self):
        self.driver.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: '
                                          'Content:"]/Custom[@ClassName="UCHomeNew"]/Pane[@ClassName="ScrollViewer"]/Custom[@AutomationId="FlowMarketPage"]/List['
                                          '@AutomationId="FlowMarketPackageListBox"]/ListItem[@ClassName="ListBoxItem"]['
                                          '@Name="BotTime.Studio.Model.PackageExplorerItem"]').click()
        time.sleep(0)

    @allure.step("点击关闭")
    def 点击关闭按钮(self):
        self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="新建项目"]/Button[@AutomationId="CloseBtn"]/Image[@ClassName="Image"]').click()
        time.sleep(0)

    @allure.step("判断元素是否存在")
    def isElementPresent(self, xpath):
        # 从selenium.common.exceptions 模块导入 NoSuchElementException类
        from selenium.common.exceptions import NoSuchElementException
        try:
            element = self.driver.find_element_by_xpath(xpath)
        # 原文是except NoSuchElementException, e:
        except NoSuchElementException as e:
            # 打印异常信息
            print(e)
            # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
            return False
        else:
            # 没有发生异常，表示在页面中找到了该元素，返回True
            return True

    @allure.step("点击一般业务流程")
    def click_general_business_process(self):
        """点击一般业务流程"""
        self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"][@AutomationId="tabNew"]/Custom[@AutomationId="ucHomeNew"]/Pane[@AutomationId="newScrollView"]/List[@ClassName="ListBox"]/ListItem[@ClassName="ListBoxItem"][@Name="Encoo.Studio.Model.HomePage.TemplateModel"]/Text[@Name="一般业务流程"][@AutomationId="text"]').click()


# endregion
# region 打开模块步骤

class Open_step(Common_step):
    """打开步骤：继承公共父类"""

    def __init__(self, open_studio):
        super().__init__(open_studio)
        self.driver = open_studio

    @allure.step("点击打开侧边栏")
    def 点击打开侧边栏(self):
        self.driver.find_element_by_xpath('//*[@AutomationId="tabOpen"]').click()
        time.sleep(1)

    @allure.step("打开-点击本地项目")
    def click_local_item(self):
        self.driver.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                          '@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/List[@AutomationId="OpenNavigateListBox"]/ListItem['
                                          '@ClassName="ListBoxItem"][@Name="Encoo.Studio.ViewModel.OpenItem"]/Text[@ClassName="TextBlock"][@Name="本地项目"]').click()

    @allure.step("打开-点击最近使用")
    def 点击最近使用(self):
        self.driver.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                          '@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/List[@AutomationId="OpenNavigateListBox"]/ListItem['
                                          '@ClassName="ListBoxItem"][@Name="Encoo.Studio.ViewModel.OpenItem"]/Text[@ClassName="TextBlock"][@Name="最近使用"]').click()
        time.sleep(1)

    @allure.step("最近使用-输入关键字")
    def 搜索框输入关键字(self, keys):
        self.driver.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                          '@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/Custom[@ClassName="RecentProjectView"]/Edit['
                                          '@ClassName="TextBox"]').send_keys(keys)
        time.sleep(1)

    @allure.step("本地项目 - 文件列表 - 指定项目")
    def click_last_list_item(self, pj_name):
        # 点击本地项目 指定项目
        try:
            Common_step(self.driver).mouse_moveto(self.driver.find_element_by_xpath(
                '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"][@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/Custom[@ClassName="LocalProjectView"]/List[@AutomationId="LocalProjectListBox"]'))
            target = self.driver.find_element_by_xpath('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
                                                       '@AutomationId="tabOpen"]/Custom[@AutomationId="openView"]/Custom[@ClassName="LocalProjectView"]/List['
                                                       '@AutomationId="LocalProjectListBox"]/ListItem[@ClassName="ListBoxItem"]['
                                                       f'@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]//*[contains(@Name,"{pj_name}")]')

            Common_step(self.driver).mouse_grow_down(unit=20)
            target.click()
        except:
            Common_step(self.driver).mouse_grow_down(unit=10)
            self.click_last_list_item(pj_name=pj_name)
        time.sleep(0)

    @allure.step("点击取消")
    def click_cancle(self):
        """点击取消"""
        self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"][@Name="导入项目"]/Window[@ClassName="#32770"][@Name="打开"]/Button[@ClassName="Button"][@Name="取消"]').click()
        self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"][@Name="导入项目"]/Button[@ClassName="Button"][@Name="取消"]/Text[@ClassName="Text"][@Name="取消"]').click()


# endregion
# region 工具模块步骤

class Tool_step(Common_step):
    """工具步骤：继承公共父类"""

    def __init__(self, open_studio):
        super().__init__(open_studio)
        self.driver = open_studio


# endregion
# region 设置模块步骤

class Set_step(Common_step):
    """设置步骤：继承公共父类"""

    def __init__(self, open_studio):
        super().__init__(open_studio)
        self.driver = open_studio


# endregion
# region 帮助模块步骤

class Help_step(Common_step):
    """帮助步骤：继承公共父类"""

    def __init__(self, open_studio):
        super().__init__(open_studio)
        self.driver = open_studio


# endregion
# region 卸载模块步骤

class Uninstall_step(Common_step):
    """卸载步骤:继承公共父类"""

    def __init__(self, open_studio):
        super().__init__(open_studio)
        self.driver = open_studio


# endregion
# region 项目管理模块步骤

class Project_manage_step(Common_step):
    """项目管理：继承公共父类"""

    def __init__(self, open_studio):
        super().__init__(open_studio)
        self.driver = open_studio

    @allure.step("项目标题右键")
    def 项目标题右键(self, pj_name):
        """项目标题右键"""
        title_item = self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Tab[@ClassName="TabControl"]/TabItem['
                                                       '@Name="System.Windows.Controls.TabItem '
                                                       'Header: Content:"][@AutomationId="workspace"]/Custom[@AutomationId="tvWorkspaceExplorerControl"]/Tree[starts-with(@AutomationId,'
                                                       '"treeView")]/TreeItem[@ClassName="TreeViewItem"][@Name="BotTime.Studio.Model.ProjectExplorerItem"]/Custom['
                                                       f'@AutomationId="Mtxt"]/Text[starts-with(@Name,"{pj_name}")][@AutomationId="TxtContent"]')
        Common_step(self.driver).right_click(element=title_item)

    @allure.step("选择项目关闭")
    def 选择项目关闭(self):
        """选择项目关闭"""
        self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Popup"]/Menu[@AutomationId="ProjectMenus"]/MenuItem[@ClassName="MenuItem"][@Name="关闭项目"]/Text[@ClassName="TextBlock"][@Name="关闭项目"]').click()

    @allure.step("关闭xaml标签页")
    def close_tab(self):
        """关闭xaml标签页"""
        self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Tab[@AutomationId="layoutDocPanel"]/TabItem[@ClassName="TabItem"][@Name="Main.xaml"]/Button[@AutomationId="PART_Close_TabItem"]/Image[@AutomationId="imgClose"]').click()
        time.sleep(2)

    @allure.step("项目点击重命名")
    def click_rename(self):
        self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Popup"]/Menu[@AutomationId="ProjectMenus"]/MenuItem[@ClassName="MenuItem"][@Name="重命名"]').click()

    @allure.step("输入项目名")
    def input_pj_name(self, pj_name):
        re_pj_name = self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Tab[@ClassName="TabControl"]/TabItem['
                                                       '@Name="System.Windows.Controls.TabItem Header: Content:"][@AutomationId="workspace"]/Custom[@AutomationId="tvWorkspaceExplorerControl"]/Tree[starts-with(@AutomationId,"treeView")]/TreeItem[@ClassName="TreeViewItem"][@Name="BotTime.Studio.Model.ProjectExplorerItem"]/Edit[@AutomationId="TbTbEditingDisplayName"]')
        re_pj_name.clear()
        re_pj_name.send_keys(pj_name)
        re_pj_name.send_keys(Keys.ENTER)

    @allure.step("点击文件")
    def click_fold(self):
        # 点击文件
        self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Menu[@ClassName="Menu"]/MenuItem[@ClassName="MenuItem"][@Name="文件"]/Text[@ClassName="TextBlock"][@Name="文件"]').click()

    @allure.step("点击导出项目")
    def click_out_pj(self, fold_path=""):
        """
        点击导出项目
        folder_path:导出文件路径
        """
        self.driver.find_element_by_xpath('//Window[@ClassName="Popup"]/MenuItem[@ClassName="MenuItem"]/Text[@ClassName="TextBlock"][@Name="导出项目"]').click()
        # 若 文件路径 不为空 则输入文件路径，若为空，则使用默认地址
        if len(fold_path) > 0:
            Clipboard.setText(fold_path)
            self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="导出项目"]/Edit[@AutomationId="FilePathTxt"]').send_keys(Keys.CONTROL, "v")
        # 点击导出按钮
        self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"][@Name="导出项目"]/Button[@AutomationId="Btn_export"]/Text[@ClassName="Text"]').click()

    @allure.step("右键点击文件名")
    def right_click_file(self):
        """右键点击文件名"""
        file_element = self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Tab[@ClassName="TabControl"]/TabItem['
                                                         '@Name="System.Windows.Controls.TabItem '
                                                         'Header: Content:"][@AutomationId="workspace"]/Custom[@AutomationId="tvWorkspaceExplorerControl"]/Tree[starts-with(@AutomationId,"treeView")]/TreeItem[@ClassName="TreeViewItem"][@Name="BotTime.Studio.Model.ProjectExplorerItem"]/TreeItem[@ClassName="TreeViewItem"][@Name="BotTime.Studio.Model.ProjectExplorerItem"]/Custom[@AutomationId="Mtxt"]/Text[@Name="NewActivity.xaml"][@AutomationId="TxtContent"]')

        Common_step(self.driver).right_click(element=file_element)

    @allure.step("文件点击重命名")
    def click_file_rename(self):
        """文件点击重命名"""
        self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Popup"]/Menu[@AutomationId="FileMenus"]/MenuItem['
                                          '@ClassName="MenuItem"][@Name="重命名"]').click()

    @allure.step("修改当前文件名称")
    def input_file_name(self, file_name):
        """修改当前文件名称"""
        file_element = self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Tab[@ClassName="TabControl"]/TabItem['
                                                         '@Name="System.Windows.Controls.TabItem '
                                                         'Header: Content:"][@AutomationId="workspace"]/Custom[@AutomationId="tvWorkspaceExplorerControl"]/Tree[starts-with('
                                                         '@AutomationId,"treeView")]/TreeItem[@ClassName="TreeViewItem"][@Name="BotTime.Studio.Model.ProjectExplorerItem"]/TreeItem['
                                                         '@ClassName="TreeViewItem"][@Name="BotTime.Studio.Model.ProjectExplorerItem"]/Edit['
                                                         '@AutomationId="TbTbEditingDisplayName"]')
        file_element.clear()
        Clipboard().setText(file_name)
        file_element.send_keys(Keys.CONTROL, "v")
        file_element.send_keys(Keys.ENTER)

    @allure.step("获取文件名称")
    def get_file_name(self):
        """获取文件名称"""
        return self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Tab[@ClassName="TabControl"]/TabItem['
                                                 '@Name="System.Windows.Controls.TabItem Header: Content:"][@AutomationId="workspace"]/Custom[@AutomationId="tvWorkspaceExplorerControl"]/Tree[starts-with(@AutomationId,"treeView")]/TreeItem[@ClassName="TreeViewItem"][@Name="BotTime.Studio.Model.ProjectExplorerItem"]/TreeItem[@ClassName="TreeViewItem"][@Name="BotTime.Studio.Model.ProjectExplorerItem"]/Custom[@AutomationId="Mtxt"]/Text[@Name="测试组件项目重命名.xaml"][@AutomationId="TxtContent"]').text


# endregion
# region 登录模块步骤

class Login_step(Common_step):
    """登录激活：继承公共父类"""

    def __init__(self, open_studio):
        super().__init__(open_studio)
        self.driver = open_studio

    @allure.step("点击个人信息")
    def click_personal_info(self):
        """点击个人信息"""
        self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Button[@AutomationId="imgMouseOver"]/Image[@AutomationId="image"]').click()

    @allure.step("点击登录按钮")
    def click_login(self):
        """点击登录按钮"""
        self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Popup"]/Text[@ClassName="TextBlock"][@Name="登录"]').click()

    @allure.step("输入用户名密码")
    def input_username_pwd(self, username, pwd):
        """输入用户名密码"""
        Clipboard().setText(username)
        self.driver.find_elements_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"][@Name="AccountActivationDialog"]/Edit[@ClassName="TextBox"]/Edit['
            '@AutomationId="textBox"]')[1].send_keys(Keys.CONTROL,"v")
        self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"][@Name="AccountActivationDialog"]/Edit[@ClassName="TextBox"]/Edit[@AutomationId="passwordBox"]').send_keys(
            pwd)

    @allure.step("登录框点击下一步")
    def click_next(self):
        """点击下一步"""
        self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"][@Name="AccountActivationDialog"]/Button[@ClassName="Button"][@Name="下一步"]/Text[@ClassName="Text"][@Name="下一步"]').click()

    @allure.step("获取租户名称")
    def get_account_name(self):
        """获取租户名称"""
        return self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"][@Name="AccountActivationDialog"]/Window[@ClassName="Window"][@Name="SelectTenantWindow"]/ComboBox[@AutomationId="ComboResourceList"]').text

    @allure.step("点击确定")
    def click_enter(self):
        """点击确定"""
        time.sleep(4)
        self.driver.find_elements_by_name('确定')[0].click()

    @allure.step("点击查看许可证")
    def click_view_permit(self):
        """点击查看许可证"""
        self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Popup"]/Text[@ClassName="TextBlock"][@Name="查看许可证"]').click()

    @allure.step("点击解除当前许可证")
    def click_unlock_permit(self):
        """解除当前许可证"""
        self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"]/Text[@ClassName="TextBlock"]['
                                          '@Name="解除当前许可证"]').click()

    @allure.step("解除许可证提示框-点击是")
    def click_alert_yes(self):
        """解除许可证提示框-点击是"""
        self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"]/Window[@ClassName="Window"]/Custom[@ClassName="CommonDialogContent"]/Button[@ClassName="Button"][@Name="是"]/Text[@ClassName="Text"][@Name="是"]').click()

    @allure.step("点击退出登录")
    def click_logout(self):
        """点击退出登录"""
        self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Popup"]/Text[@ClassName="TextBlock"][@Name="退出登录"]').click()

    @allure.step("判断退出登录提示框是否显示")
    def is_alert_show(self):
        """判断退出登录提示框是否显示"""
        try:
            if ew(self.driver).xianshi_wait(xpath='//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"]/Custom['
                                                  '@ClassName="CommonDialogContent"]/Button['
                                                  '@ClassName="Button"][@Name="确定"]/Text[@ClassName="Text"][@Name="确定"]') is not None:
                return True
        except:
            return False

    @allure.step("判断是否登录控制台")
    def is_login(self):
        """判断是否登录控制台"""
        try:
            time.sleep(2)
            # print(self.driver.page_source)
            if ew(self.driver).xianshi_wait('//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Popup"]/Text['
                                                       '@ClassName="TextBlock"][@IsOffscreen="False"][@Name="退出登录"]') is not None:
                return True
            else:
                return False
        except:
            return False


# endregion
# region 项目设置模块步骤
class Project_set_step(Common_step):
    """项目设置：继承公共父类"""

    def __init__(self, open_studio):
        super().__init__(open_studio)
        self.driver = open_studio

    @allure.step("点击项目设置")
    def click_project_set(self):
        """点击项目设置"""
        self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Popup"]/Menu[@AutomationId="ProjectMenus"]/MenuItem[@ClassName="MenuItem"][@Name="项目设置"]').click()

    @allure.step("点击自动化")
    def click_automation(self):
        """点击自动化"""
        self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"][@Name="Window1"]/List[@AutomationId="listView"]/ListItem[@ClassName="ListBoxItem"][@Name="自动化"]/Text[@ClassName="TextBlock"][@Name="自动化"]').click()

    @allure.step("设置前延迟")
    def input_pre_delay(self, num):
        """设置前延迟"""
        element = self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"][@Name="Window1"]/Pane[@ClassName="ScrollViewer"]/Edit[@AutomationId="DelayBefore"]')
        element.cleat()
        element.send_keys(num)

    @allure.step("设置后延迟")
    def input_after_delay(self, num):
        """设置后延迟"""
        element = self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"][@Name="Window1"]/Pane[@ClassName="ScrollViewer"]/Edit[@AutomationId="DelayAfter"]')
        element.cleat()
        element.send_keys(num)

    @allure.step("点击确定")
    def click_enter(self):
        """点击确定"""
        self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"][@Name="Window1"]/Button[@ClassName="Button"][@Name="确定"]/Text[@ClassName="Text"][@Name="确定"]').click()

    @allure.step("选择浏览器类型")
    def select_browse_type(self, browse):
        """选择浏览器类型"""
        self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"][@Name="Window1"]/Pane[@ClassName="ScrollViewer"]/ComboBox[@AutomationId="BrowserType"]').click()
        # 选择浏览器
        browse_type = ['IE', 'Chrome', 'FireFox', 'Web360', 'Edge']
        if browse in browse_type:
            self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"][@Name="Window1"]/Window['
                                              f'@ClassName="Popup"]/ListItem[@ClassName="ListBoxItem"][@Name="{browse}"]').click()
        else:
            print("浏览器类型不在支持的范围内")


# endregion
# region 发布模块步骤
class Release_step(Common_step):
    """发布：继承公共父类"""

    def __init__(self, open_studio):
        super().__init__(open_studio)
        self.driver = open_studio

    @allure.step("点击创建")
    def click_create(self):
        """点击创建"""
        self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Window"][@Name="新建项目"]/Button[@ClassName="Button"][@Name="创建"]/Text[@ClassName="Text"][@Name="创建"]').click()
        time.sleep(3)

    @allure.step("点击发布菜单")
    def click_release(self):
        """点击发布菜单"""
        self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Menu[@ClassName="Menu"]/MenuItem[@ClassName="MenuItem"][@Name="发布"]').click()

    @allure.step("点击控制台")
    def click_console(self):
        """点击控制台"""
        self.driver.find_element_by_xpath(
            '//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Window[@ClassName="Popup"]/MenuItem[@Name="控制台"][@AutomationId="menuConsole"]').click()

    @allure.step("弹出框点击发布")
    def click_diolog_release(self):
        """弹出框点击发布"""
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '//Button[@AutomationId="Btn_Publish"]/Text[@ClassName="Text"]').click()

    @allure.step("查看输出面板")
    def Is_show_result(self):
        """查看输出面板"""
        time.sleep(8)
        Common_step(self.driver).switch_window()

        # todo 查找输出信息内容 有问题
        content = self.driver.find_element_by_xpath('//Window[@ClassName="Window"][@Name="云扩RPA编辑器"]/Tab[@AutomationId="layoutDocPanel"]//*[contains(@Name,"项目已成功发布")]')
        return "项目已成功发布" in content


# endregion

# region 运行模块步骤
class Run_step(Common_step):
    ...


# endregion


# region 市场模块步骤
class Market_step(Common_step):
    ...
# endregion


