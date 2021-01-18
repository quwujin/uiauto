#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/8 18:35
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : Send_email.py
import smtplib
from email.mime.text import MIMEText
from test_studio.unit.func import globalvar
from test_studio.unit.func.DB import Mysql


class Send_email:
    """发送邮件功能"""
    global sender
    global pwd
    global email_host

    sender = "sdlzqwj@163.com"
    pwd = "GERXNLMGMBCELRMR"
    email_host = "smtp.163.com"

    def covert_content(self, version, data_table):
        content = rf"""<td style="padding:0;">
    <p style="font-size:12pt;font-family:宋体;margin:0;"><span style="font-size:11pt;">本邮件由系统自动发出，无需回复！</span><span lang="en-US" style="font-size: 11pt; font-family: Tahoma, sans-serif, serif, EmojiFont;"><br>
    </span><span style="font-size:11pt;">各位同事，大家好，以下为</span><span lang="en-US" style="font-size: 11pt; font-family: Tahoma, sans-serif, serif, EmojiFont;">BVT</span><span style="font-size:11pt;">执行报告</span><span lang="en-US" style="font-size: 11pt; font-family: Tahoma, sans-serif, serif, EmojiFont;"></span></p>
    <div>
    <p style="font-size:12pt;font-family:宋体;margin:0;"><span lang="en-US" style="font-size: 11pt; font-family: Tahoma, sans-serif, serif, EmojiFont;">&#65279; </span></p>
    <h1 style="font-size:19pt;font-family:Arial,sans-serif;font-weight:bold;margin-right:0;margin-left:0;">
    <span lang="en-US">BVT Test Report_Studio</span></h1>
    <h2 style="font-size:15pt;font-family:Arial,sans-serif;font-weight:bold;margin-right:0;margin-left:0;">
    <span lang="en-US">Package: studio-test</span></h2>
    <h3 style="font-size:15pt;font-family:Arial,sans-serif;font-weight:bold;margin-right:0;margin-left:0;">
    <span lang="en-US">Branch: dev</span></h3>
    <h4 style="font-size:15pt;font-family:Arial,sans-serif;font-weight:bold;margin-right:0;margin-left:0;">
    <span lang="en-US">Build: {version}</span></h4>
    <table border="1" cellspacing="0" cellpadding="0">
    <tbody><tr>
    <td style="padding:0;">
    <p align="center" style="font-size:12pt;font-family:宋体;text-align:center;margin:0;">
    <b><span lang="en-US" style="font-size: 11.5pt; font-family: Arial, sans-serif, serif, EmojiFont;">SuiteName</span></b></p>
    </td>
    <td style="padding:0;">
    <p align="center" style="font-size:12pt;font-family:宋体;text-align:center;margin:0;">
    <b><span lang="en-US" style="font-size: 11.5pt; font-family: Arial, sans-serif, serif, EmojiFont;">Total</span></b></p>
    </td>
    <td style="padding:0;">
    <p align="center" style="font-size:12pt;font-family:宋体;text-align:center;margin:0;">
    <b><span lang="en-US" style="font-size: 11.5pt; font-family: Arial, sans-serif, serif, EmojiFont;">Passed</span></b></p>
    </td>
    <td style="padding:0;">
    <p align="center" style="font-size:12pt;font-family:宋体;text-align:center;margin:0;">
    <b><span lang="en-US" style="font-size: 11.5pt; font-family: Arial, sans-serif, serif, EmojiFont;">Failed</span></b></p>
    </td>
    <td style="padding:0;">
    <p align="center" style="font-size:12pt;font-family:宋体;text-align:center;margin:0;">
    <b><span lang="en-US" style="font-size: 11.5pt; font-family: Arial, sans-serif, serif, EmojiFont;">Skipped</span></b></p>
    </td>
    </tr>
    
    """
        for i in data_table:
            content += f"""<tr>
    <td style="width:225pt;padding:0;">
    <p style="font-size:12pt;font-family:宋体;margin:0;"><span lang="en-US" style="font-size: 9pt; font-family: Consolas, serif, EmojiFont;">{i[0]}</span><span 
            lang="en-US" style="font-size: 9pt; font-family: Consolas, serif, EmojiFont;"></span></p>
    </td>
    <td style="width:75pt;padding:0;">
    <p align="center" style="font-size:12pt;font-family:宋体;text-align:center;margin:0;">
    <span lang="en-US" style="font-size: 9pt; font-family: Consolas, serif, EmojiFont;">{i[1]}</span></p>
    </td>
    <td style="width:75pt;padding:0;">
    <p align="center" style="font-size:12pt;font-family:宋体;text-align:center;margin:0;">
    <span lang="en-US" style="font-size: 9pt; font-family: Consolas, serif, EmojiFont;">{i[2]}</span></p>
    </td>
    <td style="width:75pt;padding:0;">
    <p align="center" style="font-size:12pt;font-family:宋体;text-align:center;margin:0;">
    <span lang="en-US" style="font-size: 9pt; font-family: Consolas, serif, EmojiFont;">{i[3]}</span></p>
    </td>
    <td style="width:75pt;padding:0;">
    <p align="center" style="font-size:12pt;font-family:宋体;text-align:center;margin:0;">
    <span lang="en-US" style="font-size: 9pt; font-family: Consolas, serif, EmojiFont;">{i[4]}</span></p>
    </td>
    </tr>"""
        content += """</tbody></table>
    <p style="font-size:12pt;font-family:宋体;margin:0 0 12pt 0;"><span lang="en-US" style="font-size: 11pt; font-family: Tahoma, sans-serif, serif, EmojiFont;"><br>
    <br>
    </span></p>
    </div>
    </td>"""

        return content

    def send_mail(self, user_list, sub, content):
        """
        user_list:收件人列表
        sub:邮件标题信息
        content:邮件内容
        """

        sender_info = "qwj" + "<" + sender + ">"

        msg = MIMEText(content, _subtype='html', _charset='utf-8')

        msg['Subject'] = sub
        msg['From'] = sender_info
        msg['To'] = ';'.join(user_list)

        server = smtplib.SMTP()
        server.set_debuglevel(1)
        server.connect(email_host)
        server.login(sender, pwd)
        server.sendmail(sender_info, user_list, msg.as_string())
        server.close()


# if __name__ == '__main__':
#     result = Mysql().select_data(sql=f"SELECT * FROM bvtrundetail where RunID='64fac984-54af-11eb-82bd-000c296b76f3'")
#
#     data_tables = []
#     for i in result:
#         data_table = []
#         data_table.append("IDE_" + i[2])
#         data_table.append(i[3])
#         data_table.append(i[4])
#         data_table.append(i[5])
#         data_table.append(i[6])
#         data_tables.append(data_table)
#     sen = Send_email()
#     # 'product_team@encootech.com','mahaining@encootech.com','product_team@encootech.com'
#     user_list = ["mahaining@encootech.com, quwujin@encootech.com"]
#     sub = "【Studio】BVT测试报告"
#     content = sen.covert_content(version='1.1.2012.12', data_table=data_tables)
#     sen.send_mail(user_list, sub, content)

    # sen = Send_email()
    # user_list = ['quwujin@encootech.com']
    # sub = "【Studio】BVT测试报告"
    # content = sen.covert_content(version=globalvar.get_value('build'))
    # sen.send_mail(user_list, sub, content)
