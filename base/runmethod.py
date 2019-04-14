import requests
import json
class RunMethod:
    def post_main(self,url,data,headers=None):
        if headers != None:
            res = requests.post(url=url,data=data,headers=headers)
        else:
            res = requests.post(url=url,data=data)
        # print(res.status_code)
        return res.json()

    def get_main(self,url,data=None,headers=None):
        if headers != None:
            res = requests.get(url=url,data=data,headers=headers,verify=False)
        else:
            res = requests.get(url=url,data=data,verify=False)
        return res.json()

    def run_main(self,method,url,data=None,headers=None):
        if method == 'POST':
            res = self.post_main(url,data,headers)
        else:
            res = self.get_main(url,data,headers)
        return json.dumps(res,ensure_ascii=False)



