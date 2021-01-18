#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/18 16:23
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : test_download_and_install.py
import os
from time import sleep

import allure
import pytest
from selenium.webdriver.common.keys import Keys

from test_studio.unit.func.element_clip import Clipboard
from test_studio.unit.func.element_wait import Element_wait as ew
from test_studio.unit.func.get_uninstall_path import get_software

@pytest.mark.run(order=1)
@allure.feature("下载安装模块")
class Test_验证下载安装():
    path = r'C:\download'
    """变量提前定义"""
    phone = '17521017079'
    passwd = "qwj2310287"
    qi_linkUrl = "ApiUrl=http://10.238.1.4:8080;AuthenticationUrl=http://10.238.1.4:81;"
    qi_user = "yangxiaoxue@encootech.com"
    qi_password = "perftestyxx"
    qi_licence = "2FA5A3635A144BD5937D574F66D3DF8B-ewAiAE0AYQBjAGgAaQBuAGUASwBlAHkAIgA6ACIAOQA3ADcAMQBGADYARABEADQANgA0AEUAMgBCADYARgA0AEYAMwA0ADAAQgBEADYANAA5ADUAOQAxADMAMwA3ACIALAAiAEwAaQBjAGUAbgBzAGUASQBkACIAOgAiADIARgBBADUAQQAzADYAMwA1AEEAMQA0ADQAQgBEADUAOQAzADcARAA1ADcANABGADYANgBEADMARABGADgAQgAiACwAIgBTAGMAaABlAG0AYQBWAGUAcgBzAGkAbwBuACIAOgAiADEALgAwACIALAAiAFIAZQBxAHUAZQBzAHQAZQBkAEIAeQAiADoAIgB3AGEAbgBnAHAAYQBuAEAAZQBuAGMAbwBvAC4AYwBvAG0AIgAsACIAUgBlAHEAdQBlAHMAdABlAGQAQQB0ACIAOgAiADIAMAAyADAALQAxADIALQAwADIAVAAwADIAOgAwADQAOgA0ADUALgAwADkANgA1ADAAMgA3ACsAMAAwADoAMAAwACIALAAiAE4AbwB0AEIAZQBmAG8AcgBlACIAOgAiADIAMAAyADAALQAxADIALQAwADEAVAAwADIAOgAwADMAOgA0ADUALgAwADAAMQBaACIALAAiAE4AbwB0AEEAZgB0AGUAcgAiADoAIgAyADAAMgAxAC0AMAA2AC0AMAAyAFQAMAAyADoAMAAzADoANAA1AC4AMAAwADEAWgAiACwAIgBMAGkAYwBlAG4AcwBlAGQAVABvACIAOgAiAGyad22BWyIALAAiAFAAcgBvAGQAdQBjAHQAcwAiADoAWwB7ACIATgBhAG0AZQAiADoAIgBzAHQAdQBkAGkAbwAiACwAIgBBAG0AbwB1AG4AdAAiADoAMQAsACIAUwBrAHUAIgA6ACIAZQBuAHQAZQByAHAAcgBpAHMAZQAiAH0AXQB9AA==-H75AK/Yn2LXJtaIxhgePE3nfGFChSOSkB/6eexrzuu2VAKrX/rZ0HFTDOxaUK/LurPkHFQJ2/TxqOEdCfnzQ62X+Kv61v6QKbc9OJ2iWqp6/AB49z8/oIEg8PO7MMH5v/o9P4Q1KGBIJsjDZ73nt0seStiUxGGGKm4D5LSHavfq3PdzP1QfNXoc5iLyXDwyA1n3OBI2OM2qiCVoaambxsLqk+5CSLwh4o9jlYcWpPLdwFTj5idfJUhslcWneyF13rJr3GxIC4gc6Q7iO8Syyx2SGqr3Hc/8/P4fF2vBaLVyuqTRxSSBxWaBl+MVqualH+64WvMVzqC2nFEPFdm3pTw=="

    #  #机器码
    jiqi_code = '646E9D91317F17A4B70240CAF73F76D9'
    qi_licence_local = "85E02727F7E748F28638E03E00F9C9AA-ewAiAE0AYQBjAGgAaQBuAGUASwBlAHkAIgA6ACIANgA0ADYARQA5AEQAOQAxADMAMQA3AEYAMQA3AEEANABCADcAMAAyADQAMABDAEEARgA3ADMARgA3ADYARAA5ACIALAAiAEwAaQBjAGUAbgBzAGUASQBkACIAOgAiADgANQBFADAAMgA3ADIANwBGADcARQA3ADQAOABGADIAOAA2ADMAOABFADAAMwBFADAAMABGADkAQwA5AEEAQQAiACwAIgBTAGMAaABlAG0AYQBWAGUAcgBzAGkAbwBuACIAOgAiADEALgAwACIALAAiAFIAZQBxAHUAZQBzAHQAZQBkAEIAeQAiADoAIgB3AGEAbgBnAHAAYQBuAEAAZQBuAGMAbwBvAC4AYwBvAG0AIgAsACIAUgBlAHEAdQBlAHMAdABlAGQAQQB0ACIAOgAiADIAMAAyADAALQAxADEALQAxADkAVAAwADEAOgA1ADkAOgAzADcALgA5ADcAOQAzADkANQA4ACsAMAAwADoAMAAwACIALAAiAE4AbwB0AEIAZQBmAG8AcgBlACIAOgAiADIAMAAyADAALQAxADEALQAxADgAVAAwADEAOgA0ADgAOgAxADQALgA1ADYAWgAiACwAIgBOAG8AdABBAGYAdABlAHIAIgA6ACIAMgAwADIAMQAtADAANQAtADEAOQBUADAAMQA6ADQAOAA6ADEANAAuADUANgBaACIALAAiAEwAaQBjAGUAbgBzAGUAZABUAG8AIgA6ACIAbJp3bYFbIgAsACIAUAByAG8AZAB1AGMAdABzACIAOgBbAHsAIgBOAGEAbQBlACIAOgAiAHMAdAB1AGQAaQBvACIALAAiAEEAbQBvAHUAbgB0ACIAOgAxACwAIgBTAGsAdQAiADoAIgBlAG4AdABlAHIAcAByAGkAcwBlACIAfQBdAH0A-DgrbK5fNGT9UdAqstRRMJxeoS1a44tSllpmUwOInOOv+MZ0pRUKaKdPSjjZtPbcCsSrg1oNJCrivqIHU4SGtYd1zSbCW5MWYFrfElhAhWxgGDzdQEMxqaeaF+YyFH0Mh3MuP5XrnXbMbqI7ytWH2BBSVSHinpXWvyXZUzyTVpqdWm0Vl7aD/a6EOJg8xWC/5mPMa4urSbaDgAI1BWPjaLlMaEXWzB57CaHFKpO8CbWlEHE76XO8RtlamSkyPUJxDSwPwHcH6ALsiD1++NcTW1ENTDwc3WkOtqDKGQ4vklJkAtykk/8xqdLO9j6ucZuHUNGOpHeUdYmA33dOYw55Puw=="

    @pytest.mark.run(order=1)
    @allure.story("IDE_下载_验证下载路径下是否有文件")
    def test_IDE_下载_验证下载路径下是否有文件(self):
        """0#下载#验证下载路径下是否有文件#0"""
        result  =len(os.listdir(self.path)) > 0
        sleep(3)
        assert result

    @pytest.mark.run(order=2)
    @allure.story("IDE_安装_验证注册表有StudioEncoo")
    def test_IDE_安装_验证注册表有StudioEncoo(self):
        """0#安装#验证注册表有StudioEncoo#0"""
        array = get_software()
        result = "Encoo Studio" in array
        sleep(3)
        assert result



    @allure.step("勾选同意")
    def select_agree(self, driver):
        """打开文件的时候判断有没有同意勾选框"""
        if ew(driver).xianshi_wait(xpath='//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="软件许可条款"]') is not None:
            driver.find_element_by_xpath(
                '//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="软件许可条款"]/CheckBox[@AutomationId="ConfirmCheckBox"]').click()
            sleep(2)
            driver.find_element_by_xpath(
                '//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="软件许可条款"]/Button[@Name="确定"][@AutomationId="OkButton"]/Text[@ClassName="Text"]['
                '@Name="确定"]').click()
            sleep(2)

    @allure.story("社区版激活")
    def test_社区版Activate(self, open_studio):
        """7785#激活#社区版激活#0"""
        self.select_agree(driver=open_studio)
        open_studio.find_element_by_xpath(
            '//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="ActivationWindow"]/Custom[@ClassName="UserControl"]/Button['
            '@Name="社区版激活"][@AutomationId="btn_community"]/Text[@ClassName="Text"][@Name="社区版激活"]').click()
        open_studio.find_element_by_xpath(
            '//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="ActivationWindow"]/Window[@ClassName="Window"][@Name="AccountActivationDialog"]/Edit['
            '@ClassName="TextBox"]/Edit[@AutomationId="textBox"]').send_keys(self.phone)
        Clipboard().setText(self.passwd)
        open_studio.find_element_by_xpath('//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="ActivationWindow"]/Window[@ClassName="Window"]['
                                          '@Name="AccountActivationDialog"]/Edit[@ClassName="TextBox"]/Edit[@AutomationId="passwordBox"]').send_keys(Keys.CONTROL,
                                                                                                                                                     "v")
        open_studio.find_element_by_xpath('//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="ActivationWindow"]/Window[@ClassName="Window"]['
                                          '@Name="AccountActivationDialog"]/Button[@ClassName="Button"][@Name="下一步"]/Text[@ClassName="Text"][@Name="下一步"]').click()
        result = ew(open_studio).xianshi_wait(xpath='//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="ActivationWindow"]/Window['
                                                    '@ClassName="Window"][@Name="AccountActivationDialog"]/Window[@ClassName="Window"][@Name="SelectTenantWindow"]/Button[@Name="上一步"][@AutomationId="Btn_Publish"]/Text[@ClassName="Text"][@Name="上一步"]') is not None
        sleep(5)
        open_studio.find_element_by_xpath(
            '//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="ActivationWindow"]/Window[@ClassName="Window"][@Name="AccountActivationDialog"]/Window[@ClassName="Window"][@Name="SelectTenantWindow"]/Button[@Name="上一步"][@AutomationId="Btn_Publish"]/Text[@ClassName="Text"][@Name="上一步"]').click()
        sleep(2)
        open_studio.find_element_by_xpath('//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="ActivationWindow"]/Window[@ClassName="Window"]['
                                          '@Name="AccountActivationDialog"]/Button[@ClassName="Button"][@Name="上一步"]/Text[@ClassName="Text"][@Name="上一步"]').click()
        sleep(2)
        assert result

    @allure.story("企业版控制台激活")
    def test_企业版console_activate(self, open_studio):
        """7783#激活#控制台激活#0"""
        open_studio.find_element_by_xpath(
            '//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="ActivationWindow"]/Custom[@ClassName="UserControl"]/Button['
            '@Name="登录控制台激活"][@AutomationId="btn_enterprise"]/Text[@ClassName="Text"][@Name="登录控制台激活"]').click()
        Clipboard().setText(self.qi_linkUrl)
        link_address = open_studio.find_element_by_xpath(
            '//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="ActivationWindow"]/Window[@ClassName="Window"]['
            '@Name="AccountActivationDialog"]/Edit[@ClassName="TextBox"]/Edit[@AutomationId="textBox"]')
        link_address.clear()
        sleep(2)
        link_address.send_keys(Keys.CONTROL, "v")
        Clipboard().setText(self.qi_user)
        open_studio.find_elements_by_xpath(
            '//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="ActivationWindow"]/Window[@ClassName="Window"][@Name="AccountActivationDialog"]/Edit['
            '@ClassName="TextBox"]/Edit[@AutomationId="textBox"]')[1].send_keys(
            Keys.CONTROL, "v")
        open_studio.find_element_by_xpath(
            '//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="ActivationWindow"]/Window[@ClassName="Window"][@Name="AccountActivationDialog"]/Edit['
            '@ClassName="TextBox"]/Edit[@AutomationId="passwordBox"]').send_keys(self.qi_password)
        open_studio.find_element_by_xpath('/Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="ActivationWindow"]/Window[@ClassName="Window"]['
                                          '@Name="AccountActivationDialog"]/Button[@ClassName="Button"][@Name="下一步"]/Text[@ClassName="Text"][@Name="下一步"]').click()
        sleep(5)
        result = ew(open_studio).xianshi_wait(xpath='//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="ActivationWindow"]/Window[@ClassName="Window"]['
                                                    '@Name="AccountActivationDialog"]/Window[@ClassName="Window"][@Name="SelectTenantWindow"]/Button[@Name="上一步"][@AutomationId="Btn_Publish"]/Text[@ClassName="Text"][@Name="上一步"]') is not None
        open_studio.find_element_by_xpath(
            '//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="ActivationWindow"]/Window[@ClassName="Window"][@Name="AccountActivationDialog"]/Window[@ClassName="Window"][@Name="SelectTenantWindow"]/Button[@Name="上一步"][@AutomationId="Btn_Publish"]/Text[@ClassName="Text"][@Name="上一步"]').click()
        sleep(2)
        open_studio.find_element_by_xpath(
            '//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="ActivationWindow"]/Window[@ClassName="Window"][@Name="AccountActivationDialog"]/Button[@ClassName="Button"][@Name="上一步"]/Text[@ClassName="Text"][@Name="上一步"]').click()
        assert result

    @allure.story("企业版许可证激活")
    def test_企业版_licence_activate(self, open_studio):
        """9054#激活#许可证激活#0"""
        open_studio.find_element_by_xpath(
            '//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="ActivationWindow"]/Custom[@ClassName="UserControl"]/Button[@Name="使用许可证激活"][@AutomationId="btn_license"]/Text[@ClassName="Text"][@Name="使用许可证激活"]').click()
        sleep(3)

        # 根据不同的环境自动切换
        try:
            jiqima = open_studio.find_element_by_xpath('//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="ActivationWindow"]/Window[@ClassName="Window"]/Text[@ClassName="TextBlock"][@Name="646E9D91317F17A4B70240CAF73F76D9"]').text
        except:
            jiqima = open_studio.find_element_by_xpath('//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="ActivationWindow"]/Window['
                                                       '@ClassName="Window"]/Text[@ClassName="TextBlock"][@Name="9771F6DD464E2B6F4F340BD649591337"]').text
        if jiqima==self.jiqi_code:
            Clipboard().setText(self.qi_licence_local)
        else:
            Clipboard().setText(self.qi_licence)

        open_studio.find_element_by_xpath(
            '//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="ActivationWindow"]/Window[@ClassName="Window"]/Edit[@ClassName="TextBox"]/Edit[@AutomationId="textBox"]').send_keys(
            Keys.CONTROL, "v")
        open_studio.find_element_by_xpath('//Window[@AutomationId="Splash"]/Window[@ClassName="Window"][@Name="ActivationWindow"]/Window[@ClassName="Window"]/Button['
                                          '@ClassName="Button"][@Name="激活"]/Text[@ClassName="Text"][@Name="激活"]').click()
        assert self.判断是否进入编辑器(open_studio)

    @allure.step('判断是否进入编辑器')
    def 判断是否进入编辑器(self, driver):
        """判断是否进入编辑器"""
        try:
            sleep(20)
            driver.switch_to.window(driver.window_handles[0])
            if ew(driver).xianshi_wait(xpath='//*[@AutomationId="tabStart"]') is not None:
                return True
            else:
                return False
        except:
            return False
