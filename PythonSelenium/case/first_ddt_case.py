#coding = utf-8
import sys
sys.path.append('D:/PythonSelenium')
import ddt
import unittest
from business.register_business import RegisterBusiness
from selenium import webdriver
import os
import time
import HTMLTestRunner
from util.excel_util import ExcelUtil

ex = ExcelUtil('D:/PythonSelenium/config/casedata.xls',0)
data = ex.get_data()

#数据驱动
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    #整体的前置条件，最先被执行
    @classmethod    #装饰器
    def setUpClass(cls):
        cls.file_name = 'D:/PythonSelenium/image/imooc_test001.png'    #全局变量

    #每条case的前置条件
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.login = RegisterBusiness(self.driver)

    #每条case的后置条件
    def tearDown(self):
        time.sleep(2)
        '''
        #python2中可通过sys.exc_info()方法捕获当前程序运行异常
        if sys.exc_info()[0]:
            self.driver.save_screenshot()
        '''
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd()+'/report/'+case_name+'.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()
        #print('这是每条case的后置条件')
    '''
    #邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
    @ddt.data(
        ['12','nm343dsf','pw34wrre','email_error',"请输入有效的电子邮件地址"],
        ['12dsgfjadh@qq.com','nm','pw34wrre','name_error',"字符长度必须大于等于4，一个中文字算2个字符"],
        ['12dsgfjadh@qq.com','nm343dsf','pw','password_error',"最少需要输入 5 个字符"],
        ['12dsgfjadh@qq.com','nm343dsf','pw34wrre','code_error',"验证码错误"]
    )  
    @ddt.unpack
    def test_register_case(self,email,username,password,assertCode,assertText):
        email_error = self.login.register_function(email,username,password,self.file_name,assertCode,assertText)
        #if email_error == True:
        #    print('注册成功了，此条case执行失败')

        #通过assert判断是否为error
        return self.assertFalse(email_error,'注册成功了，此条case执行失败')
    '''
    @ddt.data(*data)    #取出的数据是list的格式
    def test_register_case(self,data):
        email,username,password,assertCode,assertText = data
        error = self.login.register_function(email,username,password,self.file_name,assertCode,assertText)
        '''
        if error == True:
            print('注册成功了，此条case执行失败')
        '''
        #通过assert判断是否为error
        return self.assertFalse(error,'注册成功了，此条case执行失败')
    
if __name__ == "__main__":
    #unittest.main()
    #os.getcwd()获取工程当前路径,join拼接
    file_path = os.path.join(os.getcwd()+'/report/'+'first_ddt_case.html')
    #python3通过open()函数打开文件，python2通过file()函数打开
    f = open(file_path,'wb')

    #避免一条一条添加case
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(f,title='This is first report1.',description=u'这是第一次测试报告1。',verbosity=2)
    runner.run(suite)