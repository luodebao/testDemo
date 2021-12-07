# encoding: utf-8
import json
import unittest
import time
import params as params
from common.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
import readExcel
import common.Log

log = common.Log.logger
url = geturlParams.geturlParams().get_Url()  # 调用我们的geturlParams获取我们拼接的URL
login_xls = readExcel.readExcel().get_xls('userCase.xls', 'loginCheck')

print(url)
print(login_xls)


@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
    def setParameters(self, case_name, path, query, method):

        """
    set params
    :param case_name:
    :param path
    :param query
    :param method
    :return:
"""
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)
        log.info("case_name",case_name)
        log.info("path", path)
        log.info("query", query)
        log.info("method", method)

    def description(self):
        """
test report description
:return:
        """
        self.case_name

    def setUp(self):
        """
:return:
        """
        print(self.case_name+"测试开始前准备")

    time.sleep(3)
    def test01case(self):
        self.checkResult()
    time.sleep(3)

    def tearDown(self):
        print("测试结束，输出log完结nn")

    def checkResult(self):
        """
check test result
:return:
        """
        url1 = "http://127.0.0.1:8888/login?"
        new_url = url1+self.query
        print(new_url)
        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))
        print(data1)
        info = RunMain().run_main(self.method, url, data1)
        print(info)
        ss = json.loads(info)
        print(ss)
        if self.case_name == "login":
            self.assertEqual(ss['code'], 200)
        if self.case_name == 'login_error':
            self.assertEqual(ss['code'], -1)
        if self.case_name == 'login_null':
            self.assertEqual(ss['code', -10001])

if __name__ == "__main__":
    testUserLogin()

