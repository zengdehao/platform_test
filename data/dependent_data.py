from base.runmethod import RunMethod
from common.operation_excel import OperationExcel
from data.getdata import GetData
import json
from jsonpath_rw import jsonpath,parse


class DependentData:
    def __init__(self,case_id):
        self.case_id = case_id
        self.run_method = RunMethod()
        self.opera_excel = OperationExcel()
        self.data = GetData()

    # 获取依赖数据的行号
    def get_depend_row(self):
        row_num = self.opera_excel.get_row_num(self.case_id)
        return row_num

    # 获取依赖行的数据
    def get_depend_line_data(self):
        row_data = self.opera_excel.get_row_data(self.case_id)
        return row_data

    # 执行依赖数据，获取接口返回的数据
    def get_dependent_data(self):
        row_num = self.opera_excel.get_row_num(self.case_id)   # 根据依赖的case_id获取依赖数据的行号
        request_data = self.data.get_request_data(row_num)  # 根据行号获取请求的数据
        url = self.data.get_request_url(row_num)
        headers = self.data.get_is_header(row_num)
        method = self.data.get_request_method(row_num)
        res = self.run_method.run_main(method,url,request_data,headers)
        return json.loads(res)

    # 根据接口返回的数据，获取依赖字段对应的值
    def get_dependent_values(self,row):
        depend_key = self.data.get_depend_key(row)  # 获取依赖的字段key
        response_data = self.get_dependent_data()  # 获取依赖接口返回的数据
        json_exe = parse(depend_key)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]


if __name__ == '__main__':
    depend_data = DependentData("ly-02")
    depend_lines = depend_data.get_depend_line_data()
    print(depend_lines)
    depend_key = depend_data.data.get_depend_key(3)
    print(depend_key)
    reponse_data = depend_data.get_dependent_data()
    print(reponse_data)
    depend_value = depend_data.get_dependent_values(3)
    print(depend_value)



