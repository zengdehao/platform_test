import requests
import json
from common.log import Log


class RunMethod:
    def post_main(self,url,data,headers=None):
        try:
            if headers != None:
                res = requests.post(url=url,data=data,headers=headers)
            else:
                res = requests.post(url=url,data=data)
            res_code = res.status_code
            Log().info("成功发送POST请求，请求结果code为：%s,请求结果字段为：%s" % (res_code, res.json()))
            return res.json()
        except Exception as e:
            Log().error("POST请求出错，出错原因：%s" % e)
            return {'code': 1, 'result': 'post请求出错，出错原因:%s' % e}


    def get_main(self,url,data=None,headers=None):
        try:
            if headers != None:
                res = requests.get(url=url,data=data,headers=headers,verify=False)
            else:
                res = requests.get(url=url,data=data,verify=False)
            res_code = res.status_code
            Log().info("成功发送GET请求，请求结果code为：%s,请求结果字段为：%s" % (res_code, res.json()))
            return res.json()
        except Exception as e:
            Log().error("GET请求出错，出错原因：%s" % e)
            return {'code': 1, 'result': 'post请求出错，出错原因:%s' % e}

    def run_main(self,method,url,data=None,headers=None):
        if method == 'POST':
            res = self.post_main(url,data,headers)
        else:
            res = self.get_main(url,data,headers)
        return json.dumps(res,ensure_ascii=False)



