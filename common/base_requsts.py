import json

import requests

request_session = requests.session()


class BaseRequest(object):
    def post_main(self, url, headers, data=None, files=None):
        """
        post请求主方法
        :param data:
        :param url:
        :param headers:
        :param files:
        :return:
        """
        res = request_session.post(url=url, headers=headers, json=data, files=files, verify=False).text
        return json.loads(res)

    def get_main(self, url, headers, data=None, files=None):
        """
        get请求主方法
        :param data:
        :param url:
        :param headers:
        :param files:
        :return:
        """
        res = request_session.get(url=url, headers=headers, params=data, files=files, verify=False).text
        return json.loads(res)

    def run_main(self, method, url, headers=None, data=None, files=None):
        """
        接口请求主方法
        :param data:
        :param method:
        :param url:
        :param headers:
        :param files:
        :return:dict格式
        """
        if method.upper() == "POST":
            res = self.post_main(url, headers, data, files)
        elif method.upper() == "GET":
            res = self.get_main(url, headers, data, files)
        return res
