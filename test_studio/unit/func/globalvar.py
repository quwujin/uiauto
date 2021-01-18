#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 17:23
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : globalvar.py

"""全局变量（跨文件）"""


def _init():
    """设置的时候"""
    global _global_dict
    _global_dict = {}


def set_value(name, value):
    _global_dict[name] = value


def get_value(name, defValue=None):
    try:
        return _global_dict[name]
    except KeyError:
        return defValue
