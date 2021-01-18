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
from test_studio.unit.func.element_exist import Element_exist as ee


@allure.step("点击方法")
def element_click(driver, xpath):
    """封装点击方法"""
    button_start = driver.find_element_by_xpath(xpath)
    button_start.click()
    time.sleep(0)


def is_element_exist(xpath, driver):
    """判断元素是否存在"""
    if ew(driver).xianshi_wait( xpath=xpath) is not None:
        return True
    else:
        return False


@pytest.fixture(scope="function", autouse=True)  # scope 定义作用范围  session > module > class > function
def click_open(open_studio):
    """点击打开"""
    if ee(open_studio).isElementCanClick(xpath='//*[@AutomationId="tabOpen"]') is False:
        element_click(open_studio,
                      '//Menu[@AutomationId="startMenu"]/MenuItem[@ClassName="MenuItem"]/Text[@ClassName="TextBlock"][@Name="开始"]')
        element_click(open_studio,
                      '//*[@AutomationId="tabOpen"]')
    else:
        element_click(open_studio, '//*[@AutomationId="tabOpen"]')
    yield
