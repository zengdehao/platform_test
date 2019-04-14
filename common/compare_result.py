# 比较预期结果与实际结果的方法
import operator
import json

class CompareStr:
    def compare_str(self,expect_data,fact_data):
        '''
        判断一个字符串是否在另一个字符串中
        :param expect_data: 查找的字符串
        :param fact_data: 被查找的字符串
        :return: True or False
        '''
        '''
        if isinstance(expect_data,str):
            expect_data = expect_data.encode('latin-1').decode('unicode-escape')
        elif isinstance(fact_data,str):
            fact_data = fact_data.encode('latin-1').decode('unicode-escape')
            '''
        return operator.contains(fact_data,expect_data)




if __name__ == '__main__':
    o ={"msg": "曾德浩加油"}
    t = {"code": 0, "msg": "曾德浩加油"}
    res = operator.contains(o,'"msg": "曾德浩加油"')
    print(res)

