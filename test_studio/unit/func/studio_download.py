#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 11:25
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : studio_download.py
import datetime
import os
import uuid
import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep

from test_studio.unit.func import globalvar
from test_studio.unit.func.element_wait import Element_wait as ew
from  test_studio.unit.func.DB import Mysql
import json
import shutil
from test_studio.unit.func.studio_install import 安装
import allure


class 下载安装包():
    user = 'quwujin@encoo.com'
    pwd = 'Encootech@123'
    path = r'C:\download'

    @allure.story("下载最新安装包")
    def download(self):
        # 实例化一个Options
        chrome_options = Options()
        # 用于定义下载不弹窗和默认下载地址（默认下载地址还要再后面的commands里启动，默认是不开启的）
        prefs = {"download.default_directory": self.path, "download.prompt_for_download": False, }
        chrome_options.add_experimental_option("prefs", prefs)
        # 无头模式（就是不打开浏览器）
        # chrome_options.add_argument("--headless")
        browser = webdriver.Chrome(options=chrome_options)
        # 老外的样例，我先照着写，有没有大神可以解释一下的。下面的downloadpath要改成和上面一样
        browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': self.path}}
        command_result = browser.execute("send_command", params)

        # try:
        # 超时重新加载 15 秒
        # browser.set_page_load_timeout(20)
        # browser.set_script_timeout(20)
        # 登录前清除所有cookie

        # browser.delete_all_cookies()
        # 打印登录前的cookie
        cookieBefore = browser.get_cookies()
        print(cookieBefore)
        print("-------------------------------------------------------------------------------------------------")
        # 首先获取cookie 使用cookie免登录进入网站

        # 如果出现登录框，证明cookie失效，再重新获取cookie写入文件
        if os.path.getsize('./func/cookie.txt') != 0:
            try:
                browser.get("https://beta.bottime.com/tree")
                f1 = open('./func/cookie.txt')
                current_cookie = json.loads(f1.read())
                for co in current_cookie:
                    browser.add_cookie(co)
            except:
                browser.execute_script("window.stop()")
            browser.refresh()  # 再次刷新页面得到登录后的页面
        else:
            try:
                browser.get("https://beta.bottime.com/tree")
            except:
                browser.execute_script("window.stop()")
        self.refresh_login(browser)
        if ew(browser).xianshi_wait(xpath='//*[@class="ant-table-tbody"]') is not None:
            sleep(2)
            browser.find_elements_by_xpath('//*[@title="IDE"]/following-sibling::td/button[@type="button"]')[0].click()
            browser.implicitly_wait(5)
            #region 获取版本号
            build = browser.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td[4]').text
            guid =str(uuid.uuid1())
            current_date = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
            insert_sql = f"insert into bvtsummary VALUES('{guid}', 'Studio','dev','{build}',0,0,0,0,'{current_date}',0,'Pass',NULL)"
            Mysql().add_data(sql=insert_sql)
            # select_sql = f"SELECT ID from bvtsummary where Product = 'Studio' ORDER BY ExecutionTime desc limit 1"
            # id = Mysql().select_data(sql=select_sql)[0][0]
            globalvar.set_value('build',build)
            globalvar.set_value('summary_id',guid)
            globalvar.set_value('current_date',current_date)
            # endregion
            if os.path.exists(self.path):
                shutil.rmtree(self.path)
                os.mkdir(self.path)
            browser.execute_script('document.querySelector("body > div:nth-child(10) > div > div > div > div.ant-popover-inner > div > div > div.ant-popover-buttons > '
                                   'button.ant-btn.ant-btn-primary.ant-btn-sm > span").click()')
            安装().install_exe(browser)
        # assert len(os.listdir(self.path)) > 0

    def refresh_login(self, browser):
        if ew(browser).xianshi_wait(xpath='//*[@name="loginfmt"]', second=10) is not None:
            browser.maximize_window()
            browser.find_element_by_name('loginfmt').send_keys(self.user)
            browser.find_element_by_id('idSIButton9').click()
            sleep(2)
            if ew(browser).xianshi_wait(xpath='//*[@name="passwd"]', second=10) is not None:
                browser.find_element_by_name('passwd').send_keys(self.pwd)
                browser.find_element_by_id('idSIButton9').click()
                sleep(2)
                if ew(browser).xianshi_wait(xpath='//*[contains(text(),"保持登录状态") and @role="heading"]', second=10) is not None:
                    browser.find_element_by_id('idSIButton9').click()
                    # print(browser.get_cookies())
                    cookies = browser.get_cookies()
                    jsonCookies = json.dumps(cookies)
                    with open('./func/cookie.txt', 'w') as f:  # 可自定义文件路径默认当前路径
                        f.write(jsonCookies)
                    print("-------------------------------------------------------------------------------------------------")
        else:
            browser.refresh()
            self.refresh_login(browser)
# except Exception as e:
#     print(e)
