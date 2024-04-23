#coding = utf-8
import sys
sys.path.append('D:/PythonSelenium')
from util.excel_util import ExcelUtil
from keywordselenium.actionMethod import ActionMethod

#从excel文件中识别关键字方法
class KeywordCase():
    def run_main(self):
        #拿到行数
        #循环行数，去执行每一行的case
        #是否执行
            #拿到执行方法
            #拿到操作值
            #拿到输入数据
            #是否有输入数据
                #执行方法（输入数据，操作元素）
            #没有输入数据
                #执行方法（操作元素）
        self.action_method = ActionMethod()
        excel_u = ExcelUtil('D:/PythonSelenium/config/keyword.xls')
        case_lines = excel_u.get_lines()
        if case_lines:
            for i in range(1,case_lines):   #从第二行开始遍历
                is_run = excel_u.get_col_value(i,3)
                print(is_run)
                if is_run == 'yes':
                    method = excel_u.get_col_value(i,4)
                    send_value = excel_u.get_col_value(i,5)
                    handle_value = excel_u.get_col_value(i,6)
                    expect_result_method = excel_u.get_col_value(i,7)
                    expect_result = excel_u.get_col_value(i,8)
                    self.run_method(method,send_value,handle_value)
                    if expect_result != '':
                        expect_value = self.get_expect_result_value(expect_result)
                        if expect_value[0] == 'text':
                            result = self.run_method(expect_result_method)
                            print('result------>',result)
                            if expect_value[1] in result:
                                excel_u.write_value(i,'pass')
                            else:
                                excel_u.write_value(i,'fail')
                        elif expect_value[0]  == 'element':
                            result = self.run_method(expect_result_method,expect_value[1])
                            if result:
                                excel_u.write_value(i,'pass')
                            else:
                                excel_u.write_value(i,'fail')
                        else:
                            print('无')
                    else:
                        print('预期结果为空')

    def get_expect_result_value(self,expect_result):
        return expect_result.split('=')

    def run_method(self,method,send_value='',handle_value=''):
        print(send_value,'------->',handle_value)
        method_value = getattr(self.action_method,method)    #getattr() 函数用于返回一个对象属性值。
        if send_value != '' and handle_value != '':
            result = method_value(send_value,handle_value)
        elif send_value == '' and handle_value != '':   #判断为空是''而不是None
            result = method_value(handle_value)
        elif send_value != '' and handle_value == '':
            result = method_value(send_value)
        else:
            result = method_value()
        return result

if __name__ == '__main__':
    keyword_case = KeywordCase()
    keyword_case.run_main()
        