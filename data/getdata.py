# coding:utf-8
# 封装获取接口的数据
from common.operation_excel import OperationExcel
from data import dataconfig
import json


class GetData:
    def __init__(self):
        self.opera_excel = OperationExcel()

    # 去获取Excel的行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 获取是否执行
    def get_is_run(self,row):
        flag = None
        col = int(dataconfig.get_run())
        run_modul = self.opera_excel.get_cell_value(row,col)
        if run_modul == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 判断是否携带header
    def get_is_header(self,row):
        col = int(dataconfig.get_header())
        header = json.loads(self.opera_excel.get_cell_value(row,col))
        if header != '':
            header = dataconfig.get_header_value()
        else:
            header = None
        return header

    # 获取请求方式
    def get_request_method(self,row):
        col = int(dataconfig.get_request_way())
        request_method = self.opera_excel.get_cell_value(row,col)
        return request_method

    # 获取url
    def get_request_url(self,row):
        col = int(dataconfig.get_url())
        request_url = self.opera_excel.get_cell_value(row,col)
        return request_url

    # 获取请求的数据
    def get_request_data(self,row):
        col = int(dataconfig.get_data())
        request_data = json.loads(self.opera_excel.get_cell_value(row,col))
        return request_data

    # 获取依赖的case_id
    def get_depend_case(self,row):
        col = int(dataconfig.get_case_depend())
        case_id = self.opera_excel.get_cell_value(row,col)
        return case_id

    # 获取依赖的字段
    def get_depend_key(self,row):
        col = int(dataconfig.get_data_depend())
        depend_key = self.opera_excel.get_cell_value(row,col)
        return depend_key

    # 获取依赖数据的传参的key
    def get_field_depend(self,row):
        col = int(dataconfig.get_field_depend())
        depend_field = self.opera_excel.get_cell_value(row,col)
        return depend_field


    # 获取预期结果数据
    def get_expect_data(self,row):
        col = int(dataconfig.get_expect())
        except_data = self.opera_excel.get_cell_value(row,col)
        return except_data

    # 写入实际结果
    def write_result(self,row,value):
        col = int(dataconfig.get_result())
        self.opera_excel.write_value(row,col,value)

if __name__ == '__main__':
    data = GetData()
    rows_count = data.get_case_lines()
    case_id = data.get_depend_case(3)
    key = data.get_field_depend(3)
    print(key)
    if case_id != '':
        print(case_id)
    for row in range(1, rows_count):
        method = data.get_request_method(row)
        expect_data = data.get_expect_data(row)
        print(method,expect_data,type(expect_data))

