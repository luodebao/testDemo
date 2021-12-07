# -*- coding: utf-8 -*-
import requests
import json
class RunMain():
    def __init__(self):
        super().__init__()
    #get请求
    def send_get(self,url,data):
        res = requests.get(url=url,params=data).json()
        return json.dumps(res,indent=2,sort_keys=True)
    #post请求
    def send_post(self,url,data):
        res = requests.post(url=url,data=data).json()
        return json.dumps(res,indent=2,sort_keys=True)
    def run_main(self,method,url,data=None):
        if method == 'GET':
            res = self.send_get(url,data)
        elif method == 'POST':
            res = self.send_post(url,data)
        return res
if __name__ == '__main__':
    url = 'http://api.test.ustax.tech/marketing/adviser/manage/sst/fuzzy-search'
    data = {"keywords":"渠道"}
    print(RunMain().run_main('GET',url,data))
    # url = 'http://api.test.ustax.tech/marketing/adviser/manage/sst/fuzzy-search '
    # data = {"userId":"admin","pwd":"123456","date":"20210817"}
    # print(RunMain().run_main('POST',url,data))
    url="http://api.uat.ustax.com.cn/marketing/app-crm/intended/detail"
    data={
	"customerId": "1319636602368062238",
	"customerLoction": 4
}
    print (RunMain().run_main ('POST', url, data))