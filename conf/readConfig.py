import configparser
from conf import getpathInfo
import os
from common import base_requsts
path = getpathInfo.get_Path()  # 获取绝对路径
config_path = os.path.join(path, 'conf.ini')  #
config = configparser.ConfigParser()  # 调用外部的读取配置文件的方法
config.read(config_path, encoding='utf-8')


class ReadConfig():
    def get_http(self):
        value = config.get('HTTP', self)
        return value

    def get_email(name):
        value = config.get('EMAIL', name)
        return value

    def get_mysql(self):
        value = config.get('database', self)

        return value


if __name__ == '__main__':
    print("数据库中的host", ReadConfig.get_mysql("host"))
    print("url是", ReadConfig.get_http("url"))
    # print("数据库中的port", ReadConfig.get_mysql("port"))
    # print("数据库中的user", ReadConfig.get_mysql("user"))
    print("数据库中的密码", ReadConfig.get_mysql("password"))
    # print("数据库中的数据库名db", ReadConfig.get_mysql("db"))
    print(base_requsts.BaseRequest.run_main(method="POST",url=ReadConfig.get_http("url")))

