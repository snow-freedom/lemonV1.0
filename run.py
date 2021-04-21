

#引用
import requests
import openpyxl

from lemon_777.lesson04 import read_data,wirte_value,api_fun


#接口测试实战,分装成函数
def execute_fun(filename,sheetname):
    cases = read_data(filename,sheetname)
    # print(cases)
    for case in cases:
        case_id = case['case_id']
        url = case['url']
        data = eval(case['data'])
        # print(case_id,url,data)

        #获取期望结果code、msg
        expect = eval(case['expect'])
        expect_code = expect['code']
        expect_msg = expect['msg']
        print('期望的code:{}'.format(expect_code),'期望的msg:{}'.format(expect_msg))

        # 执行测试用例
        real_results = api_fun(url=url,data=data)
        # print(real_results)
        real_code = real_results['code']
        real_msg = real_results['msg']
        print('实际的code:{}'.format(real_code), '实际的msg:{}'.format(real_msg))
        print('#'*50)

        #断言
        if real_code == expect_code and real_msg == expect_msg:
            print('这条用例执行通过')
            final_result = 'passed'
        else:
            print('这条用例不通过')
            final_result = 'fialed'
        #写入excel表
        wirte_value(filename,sheetname,case_id+1,8,final_result)
execute_fun('C:\\pathon_workspace\\test_data\\test_case_api.xlsx', 'login')
