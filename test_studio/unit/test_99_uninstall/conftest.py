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
from test_studio.unit.func.element_wait import Element_wait as ew


@allure.step("点击方法")
def element_click(driver, xpath):
    """封装点击方法"""
    button_start = driver.find_element_by_xpath(xpath)
    button_start.click()
    time.sleep(0)


def is_element_exist(xpath, driver):
    """判断元素是否存在"""
    if ew().xianshi_wait(driver=driver, xpath=xpath) is not None:
        return True
    else:
        return False


@pytest.fixture(scope="function", autouse=True)  # scope 定义作用范围  session > module > class > function
def click_start(open_studio):
    """点击开始"""
    if is_element_exist(
            '//Tab[@ClassName="TabControl"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"][@AutomationId="workspace"]/Custom['
            '@AutomationId="tvWorkspaceExplorerControl"]/Text[@Name="项目"][@AutomationId="tbProjectType"]',
            open_studio):
        element_click(open_studio,
                      '//Menu[@AutomationId="startMenu"]/MenuItem[@ClassName="MenuItem"]/Text[@ClassName="TextBlock"][@Name="开始"]')
    else:
        element_click(open_studio, '//*[@AutomationId="tabStart"]')
    yield
    # url = ""
    # # 前置
    # driver = webdriver.Chrome()
    # driver.get(url)  # url为链接地址
    # yield driver  # yield 之前代码是前置，之后的代码就是后置
    # # 后置
    # driver.quit()
