#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 17:12
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : element_wait.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 显示等待
class Element_wait:
    """等待元素出现的三种方式"""

    def __init__(self, open_studio):
        self.driver = open_studio

    def xianshi_wait(self, xpath, second=15):
        """显示等待,默认15秒钟"""
        try:
            element = WebDriverWait(self.driver, second).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except:
            return None

    def yinshi_wait_return(self, xpath, second=10):
        """返回元素隐式等待"""
        try:
            self.driver.implicitly_wait(second)  # seconds
            myDynamicElement = self.driver.find_element_by_xpath(xpath)
            return myDynamicElement
        except:
            return None

    def yinshi_wait(self, second=10):
        """返回元素隐式等待"""
        try:
            self.driver.implicitly_wait(second)  # seconds

        except:
            return None
