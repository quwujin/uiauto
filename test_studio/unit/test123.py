#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 11:34
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : test123.py
import datetime
import json

import os

# path = r'C:\Users\rebec\AppData\Local\Encoo Studio\Update.exe'
# os.system(r"C:\Users\rebec\AppData\Local\Encoo Studio\Update.exe  --uninstall  -s")
# print(os.system(r"C:\Users\rebec\AppData\Local\Encoo Studio\Update.exe  --uninstall  -s"))

# ss = 'C:\\Users\\qasonar\\Documents\\Encoo'
# ss1 = ss.encode('utf-8')
# print(str(ss1))
# print(ss)
# print(repr(ss))
# print(ss.encode('utf-8'))

# ss1 = json.dumps(ss)
# print(ss1)


# def method_name():
#     appdata = os.getenv("APPDATA")
#     root_path = appdata.split("\\R")[0]
#     print(root_path)
#
#
# str = {'123': '123',
#        'other': [123, 1231, 123, 123, 123, 123, 12, 31, 231, 23, 123]}
# print(str)
# print(123)
# method_name()
#
# member = '{"name":"xiaoming","gender": "male", "age": 18}'
# print(member)
# def testasdf():

# def pj(pj_name):
#     print('//Tab[@AutomationId="tabHomePage"]/TabItem[@Name="System.Windows.Controls.TabItem Header: Content:"]['
#           '@AutomationId="tabStart"]/Custom[@ClassName="UCHomeStart"]/List[@AutomationId="LocalProjectListBox"]/ListItem['
#           '@ClassName="ListBoxItem"][@Name="Encoo.Studio.ViewModel.ProjectInfoModel"]/Text[@ClassName="TextBlock"][starts-with(@Name,'
#           f'"{pj_name}")]')


# pj("测试项目")

# def judge(bool_type):
#     print(bool_type == False)


# judge(False)

# class B:
#     def funcb(self):
#         print("B")
#
#
# class C:
#     def func(self):
#         print("C")
#
#
# class A(B,C):
#     def funca(self):
#         print("A")


# a = A()
# a.funca()
# a.funcb()
# a.func()

# class pj:
#     def __init__(self,name):
#         self.name = name
#     def pp(self):
#         print(self.name+"12313")
#
#
# p = pj("s是是")
# p.pp()
# from test_studio.unit.func.file_exist import File_exist
#
# result = File_exist().is_file_exist(file_path=r"C:\EncooTest\重命名测试组件管理.egs")
#
# print(result)

# appdata = os.getenv("APPDATA")
# root_path = appdata.split("\\R")[0]
# print(root_path)
# from test_studio.unit.func.file_exist import FileAndFolder
#
# FileAndFolder().deleteFolder("C:\EncooTest\一般业务流程")
import time

import pytest


# @pytest.mark.run(order=1)
# class Test_s1:
#     def test_ts1(self):
#         print("ts1")
#
# @pytest.mark.run(order=3)
# class Test_s2:
#     def test_ts2(self):
#         print("ts2")
#
# @pytest.mark.run(order=2)
# class Test_s3:
#     def test_ts3(self):
#         print("ts3")
#
# @pytest.mark.run(order=5)
# class Test_s4:
#     def test_ts4(self):
#         print("ts4")
#
# @pytest.mark.run(order=4)
# class Test_s5:
#     def test_ts5(self):
#         print("ts5")
#
#
# if __name__ == '__main__':
#     pytest.main(['-s','-v'])

def minNums(startTime, endTime):
    '''计算两个时间点之间的分钟数'''
    # 处理格式,加上秒位
    startTime1 = startTime + ':00'
    endTime1 = endTime + ':00'
    # 计算分钟数
    startTime2 = datetime.datetime.strptime(startTime1, "%Y-%m-%d %H:%M:%S")
    endTime2 = datetime.datetime.strptime(endTime1, "%Y-%m-%d %H:%M:%S")
    seconds = (endTime2 - startTime2).seconds
    # 来获取时间差中的秒数。注意，seconds获得的秒只是时间差中的小时、分钟和秒部分的和，并没有包含时间差的天数（既是两个时间点不是同一天，失效）
    total_seconds = (endTime2 - startTime2).total_seconds()
    # 来获取准确的时间差，并将时间差转换为秒
    print(total_seconds)
    mins = total_seconds / 60
    return int(mins)


# a = datetime.datetime.now()
# time.sleep(2)
# b = datetime.datetime.now()

# print( (b-a).seconds)
# print( (b-a).total_seconds())

result =  minNums('2019-07-28 00:00', '2019-07-28 01:00')
print(result)
