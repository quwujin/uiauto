#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 16:58
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : file_exist.py

import os
import shutil


class File_exist():
    """文件和文件夹相关操作"""
    def mul_file_exist(self, path, file_type_list: list):
        """判断文件夹下是否有指定的一种或多种文件"""
        Your_Dir = path
        Files = os.listdir(Your_Dir)
        for k in range(len(Files)):
            # 提取文件夹内所有文件的后缀
            Files[k] = os.path.splitext(Files[k])[1]

        Str2 = file_type_list
        if len(list(set(Str2).intersection(set(Files)))) == len(Str2):
            return True
        else:
            return False

    def file_exist(self, path, file_type: str):
        """判断文件夹下是否存在某种类型的文件"""
        Your_Dir = path
        Files = os.listdir(Your_Dir)
        for k in range(len(Files)):
            # 提取文件夹内所有文件的后缀
            Files[k] = os.path.splitext(Files[k])[1]

        # 你想要找的文件的后缀
        Str = file_type
        if Str in Files:
            return True
        else:
            return False

    def is_file_exist(self,file_path):
        """判断文件是否存在"""
        try:
           return os.path.exists(file_path)
        except:
            return False

class FileAndFolder():
    """文件和文件夹相关"""
    def mkdir(self, path):
        """判断文件夹有无，若无，新建"""
        try:
            if os.path.exists(path):
                print("文件夹存在")
                return False
            else:
                os.mkdir(path)
                return True
        except:
            print("新建文件夹出错了！")
            return False

    def deleteFolder(self,folder_path):
        """删除文件夹及其子文件"""
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)

    def deleteFile(self,file_path):
        """删除文件"""
        try:
            os.remove(file_path)
        except OSError as e:
            print("Error: %s : %s" % (file_path, e.strerror))