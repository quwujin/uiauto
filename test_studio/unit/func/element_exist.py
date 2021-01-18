#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 17:08
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : element_exist.py
import allure


class Element_exist:
    def __init__(self,driver):
        self.driver = driver

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

    @allure.step("判断元素是否可以点击")
    def isElementCanClick(self, xpath):
        # 判断页面
        flag = False
        try:
            self.driver.find_element_by_xpath(xpath).click()
            flag = True
            return flag
        except:
            return flag

    def is_element_exist(self, xpath):
        flag = True
        try:
            self.driver.find_element_by_xpath(xpath)
            return flag
        except:
            flag = False
            return flag

    def is_element_show(self, xpath):
        """判断元素是否显示"""
        try:
            element_is_show = self.driver.find_element_by_xpath(xpath)
            return element_is_show.isdisplayed()
        except:
            return False


"""
element=driver.find_element_by_name("XXX")

element.is_enabled()是否可以编辑，或者按钮是否可以点击

element.is_displayed()：判断元素是否显示
　element.is_selected()：判断元素是否选中状态
"""
