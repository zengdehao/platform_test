class CaseResult:
    '''
    获取case的通过率和失败率
    '''
    def case_result(self,pass_list,fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num
        if count_num > 0:
            pass_result = "%.2f%%"%(pass_num/count_num*100)
            fail_result = "%.2f%%"%(fail_num/count_num*100)
        else:
            pass_result = 0
            fail_result = 0
        email_content = "此次一共运行接口个数为%s个，通过个数为%s个，通过率为%s，失败个数为%s个，失败率为%s" % (count_num, pass_num, pass_result, fail_num, fail_result)
        return email_content


if __name__ == '__main__':
    case_result = CaseResult()
    email_content = case_result.case_result([1,2,3,4,5,6,7],[8,9,10,11])
    print(email_content)
