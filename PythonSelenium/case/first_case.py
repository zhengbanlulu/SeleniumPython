#coding = utf-8
import sys
sys.path.append('D:/PythonSelenium')
from business.register_business import RegisterBusiness
from selenium import webdriver
from log.user_log import UserLog
import unittest
import HTMLTestRunner
import os
import time


#分离case
class FirstCase(unittest.TestCase):
    #整体的前置条件，最先被执行
    @classmethod    #装饰器
    def setUpClass(cls):
        cls.file_name = 'D:/PythonSelenium/image/imooc_test001.png'    #全局变量
        cls.log = UserLog()
        cls.logger = cls.log.get_log()

    #每条case的前置条件
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.logger.info("This is Chrome")
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
    
    #整体的后置条件，最后被执行
    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
        

    def test_login_email_error(self):
        email_error = self.login.login_email_error('34uhgufg@qq.com','user111','111111',self.file_name)
        '''
        if email_error == True:
            print('注册成功了，此条case执行失败')
        '''
        #通过assert判断是否为error
        return self.assertFalse(email_error,'注册成功了，此条case执行失败')
    
    def test_login_username_error(self):
        name_error = self.login.login_name_error('34@qq.com','11','111111',self.file_name)
        #通过assert判断是否为error
        self.assertFalse(name_error,'注册成功了，此条case执行失败')

    def test_login_password_error(self):
        password_error = self.login.login_password_error('34@qq.com','user111','11',self.file_name)
        #通过assert判断是否为error
        self.assertFalse(password_error,'注册成功了，此条case执行失败')

    def test_login_code_error(self):
        code_error = self.login.login_code_error('34@qq.com','user111','111111',self.file_name)
        #通过assert判断是否为error
        self.assertFalse(code_error,'注册成功了，此条case执行失败')

    def test_login_success(self):
        self.login.user_base('34@qq.com','user111','111111',self.file_name)
        success = self.login.register_success()
        self.assertFalse(success,'注册成功了')

'''
def main():
    first = FirstCase()
    first.test_login_email_error()
    first.test_login_username_error()
    first.test_login_password_error()
    first.test_login_code_error()
    first.test_login_success()
'''

if __name__ == '__main__':
    #unittest.main()

    #os.getcwd()获取工程当前路径,join拼接
    file_path = os.path.join(os.getcwd()+'/report/'+'first_case.html')
    #python3通过open()函数打开文件，python2通过file()函数打开
    f = open(file_path,'wb')
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_email_error'))
    #suite.addTest(FirstCase('test_login_username_error'))
    #suite.addTest(FirstCase('test_login_password_error'))
    #suite.addTest(FirstCase('test_login_code_error'))
    #suite.addTest(FirstCase('test_login_success'))
    #unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(f,title='This is first report.',description=u'这是第一次测试报告。',verbosity=2)
    runner.run(suite)