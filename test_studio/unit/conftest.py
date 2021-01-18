"""Placeholder.
本地插件库，改善执行流程
公共方法，整个模块都可以调用
    前置或后置方法：
    例：登录方法；退出方法
"""

# todo 打开winappdriver
# todo 判断开始界面有没有激活和各种弹出框
# todo 下载安装放在所有的前面
import datetime
import time
import pytest
import os
import allure
import selenium.webdriver as webdriver
import uuid
# from appium import webdriver
from io import BytesIO
from PIL import ImageGrab
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait

from test_studio.unit.func import globalvar, date_time
from test_studio.unit.func.DB import Mysql
from test_studio.unit.func.Send_email import Send_email
from test_studio.unit.func.studio_download import 下载安装包 as download


def switch_window(driver):
    """切换到Studio窗口"""
    try:
        time.sleep(10)
        driver.switch_to.window(driver.window_handles[0])  # 绑定到最新打开的窗口
    except:
        switch_window(driver)


def download_exe():
    """下载最新Studio安装包 下载的同时调用安装方法"""
    download().download()


# region appium用
# @pytest.fixture(scope="session", autouse=True)
# def open_studio():
#     # download_exe()
#
#     """开始执行程序时打开服务端"""
#     # app_dir = r"../../../src/winappdriver/WinAppDriver.exe"
#     # os.startfile(app_dir)
#     os.system('TASKKILL /F /IM Encoo.Studio.exe')
#
#     desired_caps = {}
#     appdata = os.getenv("APPDATA")
#     root_path = appdata.split("\\R")[0]
#     desired_caps['app'] = rf"{root_path}\Local\Encoo Studio\Encoo.Studio.exe"
#     desired_caps["deviceName"] = "PC"
#     desired_caps["platformName"] = "Windows"
#     # desired_caps["automationName"] = "windows"
#
#     driver = webdriver.Remote(
#         command_executor='http://127.0.0.1:4723/wd/hub',
#         desired_capabilities=desired_caps)
#     switch_window(driver)
#     WebDriverWait(driver, 15).until(lambda x: x.find_element_by_name('设置'))
#     # WebDriverWait(driver, 15).until(lambda x: x.find_element_by_xpath('//Window[@AutomationId="Splash"]'))
#     yield driver
#     """执行结束退出服务端"""
#     # os.system('TASKKILL /F /IM WinAppDriver.exe')
#     driver.quit()
# endregion

# region fixme 测试用
# @pytest.fixture(scope="session", autouse=True)
# def open_studio():
#     # download_exe()
#     # ！定义全局变量
#     globalvar._init()
#     """开始执行程序时打开服务端"""
#     # app_dir = r"../../../src/winappdriver/WinAppDriver.exe"
#     # os.startfile(app_dir)
#     os.system('TASKKILL /F /IM Encoo.Studio.exe')
#
#     desired_caps = {}
#     appdata = os.getenv("APPDATA")
#     root_path = appdata.split("\\R")[0]
#     desired_caps['app'] = rf"{root_path}\Local\Encoo Studio\Encoo.Studio.exe"
#     desired_caps["deviceName"] = "WindowsPC"
#     desired_caps["platforName"] = "Windows"
#     # desired_caps["automationName"] = "windows"
#
#     driver = webdriver.Remote(
#         command_executor='http://127.0.0.1:4723',
#         desired_capabilities=desired_caps)
#     switch_window(driver)
#     WebDriverWait(driver, 15).until(lambda x: x.find_element_by_name('设置'))
#     # WebDriverWait(driver, 15).until(lambda x: x.find_element_by_xpath('//Window[@AutomationId="Splash"]'))
#     yield driver
#     """执行结束退出服务端"""
#     # os.system('TASKKILL /F /IM WinAppDriver.exe')
#     driver.quit()


# endregion

# region 正式环境用
# fixme 正式用
@pytest.fixture(scope="session", autouse=True)
def open_studio():
    globalvar._init()
    download_exe()
    """开始执行程序时打开服务端"""
    # app_dir = r"../../../src/winappdriver/WinAppDriver.exe"
    # os.startfile(app_dir)
    os.system('TASKKILL /F /IM Encoo.Studio.exe')

    desired_caps = {}
    appdata = os.getenv("APPDATA")
    root_path = appdata.split("\\R")[0]
    desired_caps['app'] = rf"{root_path}\Local\Encoo Studio\Encoo.Studio.exe"
    desired_caps["deviceName"] = "WindowsPC"
    desired_caps["platforName"] = "Windows"
    # desired_caps["automationName"] = "windows"

    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723',
        desired_capabilities=desired_caps)
    switch_window(driver)
    # WebDriverWait(driver, 15).until(lambda x: x.find_element_by_name('设置'))
    WebDriverWait(driver, 15).until(lambda x: x.find_element_by_xpath('//Window[@AutomationId="Splash"]'))
    yield driver
    """执行结束退出服务端"""
    current_date = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
    diff_time  = date_time.minNums(globalvar.get_value('current_date'),current_date)
    summary_id = str(globalvar.get_value('summary_id'))
    update_sql = f"UPDATE bvtsummary SET ExecutionDuration={diff_time} WHERE ID='{summary_id}'"
    Mysql().update_data(sql=update_sql)
    result = Mysql().select_data(sql=f"SELECT * FROM bvtrundetail where RunID='{summary_id}'")

    data_tables = []
    for i in result:
        data_table = []
        data_table.append("IDE_"+i[2])
        data_table.append(i[3])
        data_table.append(i[4])
        data_table.append(i[5])
        data_table.append(i[6])
        data_tables.append(data_table)
    sen = Send_email()
    user_list = ['quwujin@encootech.com,mahaining@encootech.com,product_team@encootech.com']
    sub = "【Studio】BVT测试报告"
    content = sen.covert_content(version=globalvar.get_value('build'),data_table=data_tables)
    sen.send_mail(user_list, sub, content)
    # os.system('TASKKILL /F /IM WinAppDriver.exe')
    driver.quit()
# endregion


# 更新组表
def update_rundetail(type, sum_id, suite_name, passed=0, skipped=0, failed=0):
    """更新组表
    type:状态 skipped passed failed
    sum_id:主表id
    suite_name: 组名
    实现逻辑： 先查询组名是否存在
            若存在，则更新
            若不存在，添加 获取id 存变量
    """
    if type == "passed":
        passed += 1
    elif type == "skipped":
        skipped += 1
    elif type == "failed":
        failed += 1

    select_sql = f"SELECT COUNT(*) FROM bvtrundetail where runid = (SELECT ID from bvtsummary where Product = 'Studio' ORDER BY ExecutionTime desc limit 1) and " \
                 f"SuiteName='{suite_name}'"
    suite_count = str(Mysql().select_data(sql=select_sql)[0][0])
    if suite_count == '0':
        # 添加
        guid = str(uuid.uuid1())
        globalvar.set_value(suite_name, guid)
        current_time = str(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'))
        insert_sql = f"INSERT INTO bvtrundetail (id,RunID,SuiteName,Total,Pass,Fail,Skip,ExecutionTime) VALUES('{guid}','{sum_id}','{suite_name}',1,{passed},{failed}," \
                     f"{skipped},'{current_time}')"
        Mysql().add_data(sql=insert_sql)
    else:
        # 更新
        update_sql = f"UPDATE bvtrundetail SET Total=Total+1, Pass=Pass+{passed},Fail = Fail+{failed},Skip = Skip+{skipped} WHERE id = " \
                     f"'{globalvar.get_value(suite_name)}'"
        Mysql().update_data(sql=update_sql)


# 更新case 表
def add_suitdetail(type, suite_name, case_name, case_id, priority, execution_time):
    """更新case 表
    type:状态
    suite_name:组名
    case_name:用例名
    case_id:用例id
    priority:优先级
    execution_time:执行时间 可以存在全局变量
    """
    guid = str(uuid.uuid1())
    suite_id = globalvar.get_value(suite_name)
    current_time = str(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'))
    insert_sql = f"INSERT INTO  bvtsuitedetail (id,SuiteID,CaseName,CaseId,Priority,Result,ExecutionTime,UpdateTime) VALUES('{guid}','{suite_id}','{case_name}','" \
                 f"{case_id}',{priority},'{type}','{execution_time}','{current_time}')"
    Mysql().add_data(sql=insert_sql)



# 钩子，用来钩住失败
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """处理失败截图和获取结果存到DB"""
    outcome = yield
    rep = outcome.get_result()
    # we only look at actual failing test1 calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        with BytesIO() as output:
            img = ImageGrab.grab()
            img.save(output, 'PNG')
            data = output.getvalue()
        # 将异常截图附加到allure报告中
        allure.attach(data, name="异常截图", attachment_type=AttachmentType.PNG)
    """将用例结果插入到DB"""
    global case_name, case_id, case_priority, case_suite
    """实现思路：
    1.report.outcome 运行结果 用于统计数量
    2. 用例描述中获取用例信息
        例：id#用例组名#用例名#用例优先级
    2.1  bvtsuiteddetail 表
        a.补充用例id
        b.优先级
        c.用例名
    获取Bvtsummary表的最新ID
        if判断执行结果
            在相应的总数上+1，若有失败，将type更新为fail
        判断Bvtrundetail 组名是否存在 及状态
            若存在更新
            若不存在，添加，添加后获取id，存到全局变量
    执行单条case 的时候先往 Bvtsuitedetail 插入一条数据
    """
    # 用例执行结果 out
    # outcome = yield
    # 从钩子方法的调用结果中获取测试报告 rep
    report = outcome.get_result()
    # rep.when  call 步骤结果 setup：用例结果  teardown
    # print('测试报告：%s' % report)

    desc = str(item.function.__doc__)
    if len(desc) > 0 and "#" in desc:
        case_id = desc.split('#')[0]  # 用例ID
        case_suite = desc.split('#')[1]  # 用例组名
        case_name = desc.split('#')[2]  # 用例名
        case_priority = desc.split('#')[3]  # 用例优先级
    # sum 表id
    summary_id = str(globalvar.get_value('summary_id'))
    # print('步骤：%s' % report.when)
    if report.when == "setup":
        # print("用例方法")
        if report.outcome == "passed":
            update_sql = f"UPDATE bvtsummary SET Total=Total+1,Pass = Pass+1 WHERE id='{summary_id}'"
            Mysql().update_data(sql=update_sql)
        elif report.outcome == "skipped":
            update_sql = f"UPDATE bvtsummary SET Total=Total+1,Skip = Skip+1 WHERE id='{summary_id}'"
            Mysql().update_data(sql=update_sql)
        elif report.outcome == "failed":
            update_sql = f"UPDATE bvtsummary SET Total=Total+1,Fail = Fail+1,Type = 'Fail'  WHERE id='{summary_id}'"
            Mysql().update_data(sql=update_sql)
        else:
            ...
        update_rundetail(type=report.outcome, sum_id=summary_id, suite_name=case_suite)
        add_suitdetail(type=report.outcome, suite_name=case_suite, case_name=case_name, case_id=case_id, priority=case_priority,
                       execution_time=globalvar.get_value('current_date'))

    # 测试方法
    # print('nodeid：%s' % report.nodeid)
    # 用例描述 就是方法注释
    # print('description:%s' % str(item.function.__doc__))
    # passed or failed
    # print(('运行结果: %s' % report.outcome))





# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#      """将用例结果插入到DB"""
    # global case_name, case_id, case_priority, case_suite
    # """实现思路：
    # 1.report.outcome 运行结果 用于统计数量
    # 2. 用例描述中获取用例信息
    #     例：id#用例组名#用例名#用例优先级
    # 2.1  bvtsuiteddetail 表
    #     a.补充用例id
    #     b.优先级
    #     c.用例名
    #
    # 获取Bvtsummary表的最新ID
    #     if判断执行结果
    #         在相应的总数上+1，若有失败，将type更新为fail
    #     判断Bvtrundetail 组名是否存在 及状态
    #         若存在更新
    #         若不存在，添加，添加后获取id，存到全局变量
    # 执行单条case 的时候先往 Bvtsuitedetail 插入一条数据
    # """
    # # 用例执行结果 out
    # outcome = yield
    # # 从钩子方法的调用结果中获取测试报告 rep
    # report = outcome.get_result()
    # # rep.when  call 步骤结果 setup：用例结果  teardown
    # # print('测试报告：%s' % report)
    #
    # desc = str(item.function.__doc__)
    # if len(desc)>0 and "#" in desc:
    #     case_id = desc.split('#')[0]  # 用例ID
    #     case_suite = desc.split('#')[1]  # 用例组名
    #     case_name = desc.split('#')[2]  # 用例名
    #     case_priority = desc.split('#')[3]  # 用例优先级
    # # sum 表id
    # summary_id = str(globalvar.get_value('summary_id'))
    # # print('步骤：%s' % report.when)
    # if report.when == "setup":
    #     # print("用例方法")
    #     if report.outcome == "passed":
    #         update_sql = f"UPDATE bvtsummary SET Total=Total+1,Pass = Pass+1 WHERE id='{summary_id}'"
    #         Mysql().update_data(sql=update_sql)
    #     elif report.outcome == "skipped":
    #         update_sql = f"UPDATE bvtsummary SET Total=Total+1,Skip = Skip+1 WHERE id='{summary_id}'"
    #         Mysql().update_data(sql=update_sql)
    #     elif report.outcome == "failed":
    #         update_sql = f"UPDATE bvtsummary SET Total=Total+1,Fail = Fail+1,Type = 'Fail'  WHERE id='{summary_id}'"
    #         Mysql().update_data(sql=update_sql)
    #     else:
    #         ...
    #     update_rundetail(type=report.outcome,sum_id=summary_id,suite_name=case_suite)
    #     add_suitdetail(type=report.outcome,suite_name=case_name,case_name=case_name,case_id=case_id,priority=case_priority,execution_time=globalvar.get_value('current_date'))
    #
    # # 测试方法
    # # print('nodeid：%s' % report.nodeid)
    # # 用例描述 就是方法注释
    # # print('description:%s' % str(item.function.__doc__))
    # # passed or failed
    # # print(('运行结果: %s' % report.outcome))

# @pytest.fixture(scope="class")  # scope 定义作用范围  session > module > class > function
# def open_url():
#     """打开链接"""
#     url = ""
#     # 前置
#     driver = webdriver.Chrome()
#     driver.get(url)  # url为链接地址
#     yield driver  # yield 之前代码是前置，之后的代码就是后置
#     # 后置
#     driver.quit()


# 刷新页面
# @pytest.fixture()  # 默认scope function级别
# def refresh_page(open_url):
#     """
#     调用的每个方法执行时调用
#     :param open_url:
#     :return:
#     """
#     yield
#     open_url.refresh()


# @pytest.fixture(scope="function", autouse=False)
# def open_home(request):
#     """
#     调用的每个类执行时会调用 可以写在公共方法中，或者写在类中
#     autouse:为true时，所有的test方法都会调用
#     :param request:
#     :return:
#     """
#     print("function:%s \n--回到首页--" % request.function.__name__)
