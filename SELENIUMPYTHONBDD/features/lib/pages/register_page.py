#coding = utf-8
from features.lib.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class RegisterPage(BasePage):
    def __init__(self,context):
        #调用父类方法，Python 3和Python 2的区别是: Python 3可以使用直接使用super().xxx代替super(Class, self).xxx
        super(RegisterPage,self).__init__(context.driver)

    def send_useremail(self,useremail):
        self.get_element(By.ID,'register_email').send_keys(useremail)

    def send_username(self,username):
        self.get_element(By.ID,'register_nickname').send_keys(username)

    def send_password(self,password):
        self.get_element(By.ID,'register_password').send_keys(password)

    def send_code(self,code):
        self.get_element(By.ID,'captcha_code').send_keys(code)

    def click_register_button(self):
        self.get_element(By.ID,"register-btn").click()

    def get_code_text(self):
        return self.get_element(By.ID,"captcha_code-error").text