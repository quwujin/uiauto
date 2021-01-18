#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 14:07
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : conftest.py
"""需要退出并点击到开始菜单"""

import allure
import pytest
import time
from test_studio.unit.func.element_exist import Element_exist as ee


@allure.step("点击方法")
def element_click(driver, xpath):
    """封装点击方法"""
    driver.find_element_by_xpath(xpath).click()
    time.sleep(0)


@pytest.fixture(scope="function", autouse=True)  # scope 定义作用范围  session > module > class > function
def click_new(open_studio):
    """点击新建"""
    flag = ee(open_studio).isElementCanClick(xpath='//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: '
                                        'Content:"]/Text['
                                        '@ClassName="TextBlock"][@Name="新建"]')
    # 判断是否在项目编辑页面
    if flag is False:
        element_click(driver=open_studio, xpath='//Menu[@AutomationId="startMenu"]/MenuItem[@ClassName="MenuItem"]')
        element_click(open_studio, '//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: Content:"]/Text['
                                   '@ClassName="TextBlock"][@Name="新建"]')
    else:
        element_click(open_studio, '//Tab[@AutomationId="tabHomePage"]/TabItem[@ClassName="TabItem"][@Name="System.Windows.Controls.TabItem Header: Content:"]/Text['
                                   '@ClassName="TextBlock"][@Name="新建"]')
    yield
