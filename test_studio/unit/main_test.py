#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 15:01
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : main_test.py
import os

import pytest

if __name__ == '__main__':
    # 运行当前目录下所有（test_*.py  和 *_test.py）
    """
    参数详解
        -s: 显示程序中的print/logging输出
        -v: 丰富信息模式, 输出更详细的用例执行信息
        -q: 安静模式, 不输出环境信息
        -k：关键字匹配，用and区分：匹配范围（文件名、类名、函数名）
        ['-s', '-r', 'test_demo.py', 'test_demo.py']
    """
    # 运行总的实例
    pytest.main(['-s', '-v'])
    # 运行下载安装
    # pytest.main(['-s', '-v','test_download_and_install'])
    # 运行开始
    # pytest.main(['-s', '-v','test_1_start'])
    # 运行新建
    # pytest.main(['-s', '-v','test_2_new'])
    # 运行打开
    # pytest.main(['-s', '-v','test_3_open'])
    # 运行工具
    # pytest.main(['-s', '-v','test_4_tool'])
    # 运行设置
    # pytest.main(['-s', '-v','test_5_set'])
    # 运行帮助
    # pytest.main(['-s', '-v','test_6_help'])
    # 运行项目管理
    # pytest.main(['-s','-v','test_7_projectManage'])
    # 登录激活
    # pytest.main(['-s','-v','test_8_login'])



    # pytest.main(['-s', '-v',''])
# pytest.main(['-s', '-v', '--alluredir=./report/allure_raw', '--clean-alluredir'])
# os.popen('allure serve report/allure_raw')
