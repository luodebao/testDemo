import baseRequest
from ddt import ddt,unpack,data
import unittest
import operateExcel
import json
import login
import yaml
import jsonReplace
import jsonpath
import time
from HTMLTestRunner import HTMLTestRunner


login.loginGetToken()

f = open('token.yaml')
yamldata = f.read()
yamlread = yaml.load(yamldata,Loader=yaml.FullLoader)
#print(yamlread['token'])
Authorization = yamlread['token']

testdata = operateExcel.readExcelToList(file='关联固定渠道.xls')
@ddt
class Test(unittest.TestCase):
    @data(*testdata)
    def test01(self,args):
        url = args[2]
        method = str(args[3])
        headers = json.loads(args[4])
        headers['Authorization'] = Authorization
        data = json.loads(args[5])
        isdepend = args[6]
        no = int(args[0])
        if isdepend == 'yes':
            relyrow = str(args[7]).split(',')   #通过‘,’分隔符将获取的依赖接口的行数切片成列表
            for rerow in relyrow:
                rerow = int(float(rerow))
                relyres = eval(operateExcel.readExcel(file='关联固定渠道.xls', row=rerow)[8]) #获取依赖接口的response，并通过eval方法转化成字典
                rule = operateExcel.readExcel(file='关联固定渠道.xls', row=rerow)[9]
                islist = operateExcel.readExcel(file='关联固定渠道.xls', row=rerow)[13] #提取值是否是列表
                print(rule)
                extract = jsonpath.jsonpath(relyres, expr=rule)
                print(type(extract))
                if type(extract) == bool:
                    print('-----------------第%d行出错，依赖提取失败-----------------' % no)
                key = operateExcel.readExcel(file='关联固定渠道.xls', row=rerow)[10]
                if islist == 'y':
                    jsonReplace.ReplaceJsonValue(data, key, extract) #提取值需要用列表就用extract整体
                else:
                    jsonReplace.ReplaceJsonValue(data, key, extract[0]) #提取值不需要列表就用[0]取出值
                print(data)
            res = baseRequest.baseRequest(url=url, headers=headers, data=data, method=method)
            self.assertEqual(res['code'],10000)
            operateExcel.writeExcel(file='关联固定渠道.xls', n=no, c=8, value=str(res))
        elif isdepend == 'urlyes':
            relyrow = str(args[7]).split(',')
            for rerow in relyrow:
                rerow = int(float(rerow))
                key = operateExcel.readExcel(file='关联固定渠道.xls', row=rerow)[12]
                relyres = eval(operateExcel.readExcel(file='关联固定渠道.xls', row=rerow)[8])
                rule = operateExcel.readExcel(file='关联固定渠道.xls', row=rerow)[9]
                extract = jsonpath.jsonpath(relyres, expr=rule)
                if type(extract) == bool:
                    print('-----------------第%d行出错，依赖提取失败-----------------' % no)
                url = url.replace(key, extract[0])
            res = baseRequest.baseRequest(url=url, headers=headers, data=data, method=method)
            self.assertEqual(res['code'], 10000)
            operateExcel.writeExcel(file='关联固定渠道.xls', n=no, c=8, value=str(res))
        elif isdepend == 'allyes':
            relyrow = str(args[7]).split(',')
            for rerow in relyrow:
                rerow = int(float(rerow))
                key1 = operateExcel.readExcel(file='关联固定渠道.xls', row=rerow)[12]
                relyres = eval(operateExcel.readExcel(file='关联固定渠道.xls', row=rerow)[8])
                rule = operateExcel.readExcel(file='关联固定渠道.xls', row=rerow)[9]
                extract = jsonpath.jsonpath(relyres, expr=rule)
                if type(extract) == bool:
                    print('-----------------第%d行出错，依赖提取失败-----------------' % no)
                url = url.replace(key1, extract[0])
                rebodyrow = str(args[11]).split(',')
                for rebody in rebodyrow:
                    rebody = int(float(rebody))
                    relybodyres = eval(operateExcel.readExcel(file='关联固定渠道.xls', row=rebody)[8])
                    relyrule = operateExcel.readExcel(file='关联固定渠道.xls', row=rebody)[9]
                    extract = jsonpath.jsonpath(relybodyres, expr=relyrule)
                    if type(extract) == bool:
                        print('-----------------第%d行出错，依赖提取失败-----------------' % no)
                    key = operateExcel.readExcel(file='关联固定渠道.xls', row=rebody)[10]
                    jsonReplace.ReplaceJsonValue(data, key, extract[0])
                    res = baseRequest.baseRequest(url=url, method=method, headers=headers, data=data)
                    self.assertEqual(res['code'], 10000)
                    operateExcel.writeExcel(file='关联固定渠道.xls', n=no, c=8, value=str(res))
        else:
            data1 = json.loads(args[5])
            res = baseRequest.baseRequest(url=url, headers=headers, data=data1, method=method)
            self.assertEqual(res['code'], 10000)
            operateExcel.writeExcel(file='关联固定渠道.xls', n=no, c=8, value=str(res))


case_dir = './'

discover = unittest.defaultTestLoader.discover(case_dir,pattern='ddtTest.py',top_level_dir=None)

if __name__ == '__main__':
#    unittest.main()
    report_dir = './reports'
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = report_dir + '/' + now + 'result.html'
    print(report_name)
    with open(report_name, 'wb')as f:
        runner = HTMLTestRunner(stream=f, title='测试报告', description='报告如下')
        runner.run(discover)
