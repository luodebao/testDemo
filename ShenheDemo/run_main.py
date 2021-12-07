#!/usr/bin/env python
# -*- coding=utf-8 -*-
import requests
import json

class RunMain(object):
    #初始化方法
    def __init__(self,method,url,data=None):
        self.res = self.run_main(method,url,data)
    #GET请求
    def send_get(self,url,data):
        res = requests.get(url=url,params=data).json()
        return json.dumps(res,indent=2,sort_keys=True,ensure_ascii=False)
    #POST请求
    def send_post(self,url,data):
        res = requests.post(url=url,data=data).json()
        return json.dumps(res,indent=2,sort_keys=True,ensure_ascii=False)
    #封装GET和POST
    def run_main(self,method,url,data=None):
        if method == 'GET':
            res = self.send_get(url,data)
            return res
        elif method == 'POST':
            res = self.send_post(url,data)
        return res
if __name__ == '__main__':
    run = RunMain ('GET', url="https://api.test.ustax.tech/marketing/crm/cooperated/detail/1447396912391585793",data=None)
    print(run.res)
    run = RunMain('POST',url="https://api.test.ustax.tech/marketing/adviser/manage/sst/page",data={
	"keywords": "众乐邦",
	"current": 1,
	"size": 20,
	"orders": [
		{
			"column": "",
			"asc": False
		}
	]
})
    print(run.res)