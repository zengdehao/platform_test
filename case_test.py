import time
from base.HTMLTestRunner import HTMLTestRunner
import unittest
import os

# 制定测试用例的文件目录
test_dir = os.path.dirname(os.path.abspath(__file__))
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')
if __name__ == '__main__':
    now_time = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    file_name =os.path.dirname(os.path.abspath(__file__)) + '\\report\\' + now_time + '_result.html'
    fp = open(file_name,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Tvyuetravel TestResult',
                            description='Implementation Example with: ')
    runner.run(discover)
    fp.close()
    print("\nsuccess")




