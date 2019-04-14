import sys
import os
sys.path.append('./base')
sys.path.append('./data')
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from base.runmethod import RunMethod
from data.getdata import GetData
from data.dependent_data import DependentData
from common.send_email import SendEmail
import unittest

class RunTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.run_method = RunMethod()
        cls.data = GetData()
        cls.pass_count = []
        cls.fail_count = []

    @classmethod
    def tearDownClass(cls):
        cls.send = SendEmail(cls.pass_count,cls.fail_count)
        cls.send.send_email()

    # 定义函数，最终生成的测试用例的执行方法
    def run_test(self,row):
        is_run = self.data.get_is_run(row)
        if is_run:
            url = self.data.get_request_url(row)
            method = self.data.get_request_method(row)
            request_data = self.data.get_request_data(row)
            headers = self.data.get_is_header(row)
            expect = self.data.get_expect_data(row)
            print(type(expect),expect)
            depend_case = self.data.get_depend_case(row)
            print(type(depend_case))
            # 判断是否存在依赖数据
            if depend_case != '':
                self.depend_data = DependentData(depend_case)
                depend_reponse_value = self.depend_data.get_dependent_values(row)  # 获取依赖接口返回的数据的依赖的key对应的value值
                depend_key = self.data.get_field_depend(row)  # 获取依赖数据value所对应的新的接口的key
                request_data[depend_key] = depend_reponse_value  # key=value

            # 发送请求
            res = self.run_method.run_main(method,url,request_data,headers)

            # 预期结果与实际结果对比
            # result = operator.contains(res,expect)
            try:
                result = self.assertIn(expect,res)
                self.data.write_result(row, "pass")
                self.pass_count.append(row)
                print(type(res), res)
                print(result)
                print(self.pass_count)
                print("第%d条用例执行完毕" % row)
            except AssertionError as e:
                self.data.write_result(row, res)
                self.fail_count.append(row)
                print(self.fail_count)
                raise

    @staticmethod
    def get_case_all(row):
        def get_case(self):
            self.run_test(row)
        return get_case

# 根据Excel用例的数量批量生成以“test”开头的测试方法
def add_test_method():
    data = GetData()
    rows_count = data.get_case_lines()
    for row in range(1, rows_count):
        setattr(RunTest, "test_%d" % row, RunTest.get_case_all(row))

# 生成test方法
add_test_method()


if __name__ == '__main__':
    unittest.main()