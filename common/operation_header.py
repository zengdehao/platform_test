import json
import requests
from common.operation_json import OperationJson

class OperationHeader:
    def __init__(self,response):
        self.response = json.loads(response)

    # 通过登录接口的返回值获取cookies
    def get_cookie(self):
        cookie_jar = self.response.cookies
        cookie_dict = requests.utils.dict_from_cookiejar(cookie_jar)
        return cookie_dict

    # 写入cookies
    def write_cookie(self):
        cookie = self.get_cookie()
        op_json = OperationJson()
        op_json.write_data(cookie)
