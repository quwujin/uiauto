#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 14:07
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : conftest.py

import allure
import pytest
import time
from test_studio.unit.func.element_wait import Element_wait as ew
from test_studio.unit.func.element_exist import Element_exist as ee


# @pytest.fixture(scope="function",autouse=True)  # scope 定义作用范围  session > module > class > function
# def click_start(open_studio):
#     """点击开始"""
#     if ee(open_studio).isElementCanClick(xpath='//*[@AutomationId="tabStart"]', driver=open_studio) is False:
#         open_studio.find_element_by_xpath('//Menu[@AutomationId="startMenu"]/MenuItem[@ClassName="MenuItem"]/Text[@ClassName="TextBlock"][@Name="开始"]').click()
#     else:
#         open_studio.find_element_by_xpath('//*[@AutomationId="tabStart"]').click()
#     yield
#     # 注意：方法后的输出是在类输出里面看的，此时方法已经结束，看不到了
#     # url = ""
#     # # 前置
#     # driver = webdriver.Chrome()
#     # driver.get(url)  # url为链接地址
#     # yield driver  # yield 之前代码是前置，之后的代码就是后置
#     # # 后置
#     # driver.quit()
