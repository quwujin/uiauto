#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 13:38
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : DB.py
import pymysql


class Mysql:
    def __init__(self):
        # 连接数据库
        self.conn = pymysql.Connect(host='testportaldb.mysql.database.chinacloudapi.cn', user='encooPortal@testportaldb', passwd='EnL-P3*@2a', db='testdb', port=3306,
                                    charset='utf8')
        # self.conn = pymysql.Connect(host='testportaldb.mysql.database.chinacloudapi.cn', user='encooPortal@testportaldb', passwd='EnL-P3*@2a', db='test', port=3306,
        #                             charset='utf8')
        # 获取游标
        self.cur = self.conn.cursor()

    # 创建表
    def create_table(self, sql):
        """创建表"""
        cur = self.cur
        # cur.execute("drop table if EXISTS  pyTest;")
        # sql = """create table pyTest (
        #          id VARCHAR(20) NOT NULL  PRIMARY KEY,
        #          name VARCHAR(20),
        #          sex CHAR(2)"""
        cur.execute(sql)
        # 修改表类型
        change_type = "ALTER TABLE pyTest CONVERT TO CHARACTER SET utf8mb4"
        cur.execute(change_type)
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    # 添加数据
    def add_data(self, sql="insert into pyTest (id,name,sex) values ('123','张三','男')"):
        """添加数据"""
        try:
            # 执行sql语句
            self.cur.execute(sql)
            # #提交到数据库执行
            self.conn.commit()
        except:
            print("添加数据回滚")
            # 发生错误时回滚
            self.conn.rollback()
        finally:
            self.cur.close()
            self.conn.close()

    # 修改数据
    def update_data(self, sql="update pyTest set name='王五' where id='123'"):
        """修改数据"""
        # ----------修改数据-----------------------
        # 写法1：sql="update pyTest set name='李四' where id='%s'" %('123')
        # 写法2：
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            self.cur.close()
            self.conn.close()

    # 查询数据
    def select_data(self, sql="select * from pyTest"):
        """查询数据"""
        # 查询操作
        # sql = "select * from pyTest"
        self.cur.execute(sql)
        self.conn.commit()
        # 使用 fetchall() 方法获取数据对象，可以得到表中所有的信息，如：(('123', '王五', '男'), ('124', '张三', '男'))
        data1 = self.cur.fetchall()
        # print("数据对象是{}".format(data1))
        # print(data1)

        # for i in data1:
        #     print(i)

        # 使用 fetchone() 方法获取一条数据，如：('123', '王五', '男')
        # data2 = cur.fetchone()
        # #cur.fetchall()与cur.fetchone() 不能同时使用哪怕赋值给不同的变量。
        # print(data2)
        # for i in data2:
        #     print(i)
        self.cur.close()
        self.conn.close()
        return data1

    # 删除表
    def delete_data(self, sql=" DROP TABLE pytest"):
        """删除表"""
        # 删除表
        # sql = " DROP TABLE pytest"

        # ----------删除数据-----------------------
        # sql="delete from pyTest"
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            self.cur.close()
        self.conn.close()

# id =   Mysql().select_data(sql="SELECT ID from bvtsummary_copy1 where Product = 'Studio' ORDER BY ExecutionTime desc limit 1")

# if __name__ == '__main__':
#     resutl = Mysql().select_data(sql="SELECT * FROM bvtrundetail where RunID='00f6d2d1-7af7-405c-9adc-466e5b1a0d2f'")
#     print(resutl)
