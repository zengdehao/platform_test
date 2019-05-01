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
from common.log import Log



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
        error_num = 0
        Log().info("开始执行第%d条用例"%row)
        while error_num <= 3:
            is_run = self.data.get_is_run(row)
            if is_run:
                url = self.data.get_request_url(row)
                method = self.data.get_request_method(row)
                request_data = self.data.get_request_data(row)
                headers = self.data.get_is_header(row)
                expect = self.data.get_expect_data(row)
                depend_case = self.data.get_depend_case(row)
                # 判断是否存在依赖数据
                if depend_case != '':
                    self.depend_data = DependentData(depend_case)
                    depend_reponse_value = self.depend_data.get_dependent_values(row)  # 获取依赖接口返回的数据的依赖的key对应的value值
                    depend_key = self.data.get_field_depend(row)  # 获取依赖数据value所对应的新的接口的key
                    request_data[depend_key] = depend_reponse_value  # key=value

                # 发送请求
                res = self.run_method.run_main(method,url,request_data,headers)
                Log().info("请求传入数据：请求方法：%s，请求url：%s，请求参数：%s，请求的信息头：%s"%(method,url,request_data,headers))

                # 预期结果与实际结果对比
                # result = operator.contains(res,expect)
                try:
                    self.assertIn(expect,res)
                    Log().info("对code断言，断言结果--预期值%s == 实际值%s，测试通过"%(expect,res))
                    self.data.write_result(row, "pass")
                    self.pass_count.append(row)
                    error_num = 0
                    break
                except AssertionError as e:
                    Log().info("对code断言，断言结果--预期值%s != 实际值%s，测试不通过"%(expect,res))
                    if error_num <= 2:
                        error_num += 1
                        Log().info("失败用例重试第%d次"%error_num)
                    else:
                        Log().info("失败重试中次数用完，最后结果不通过")
                        self.data.write_result(row, res)
                        self.fail_count.append(row)
                        # raise
                        break

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