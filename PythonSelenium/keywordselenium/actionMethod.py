#coding = utf-8
import sys
sys.path.append('D:/PythonSelenium')
from selenium import webdriver
from base.find_element import FindElement
import time

#关键字模型的操作
class ActionMethod():
    def __init__(self):
        pass
    #打开浏览器
    def open_browser(self,brower):
        if brower == 'chrome':
            self.driver = webdriver.Chrome()
        elif brower == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()
    
    #输入地址
    def get_url(self,url):
        self.driver.get(url)

    #定位元素
    def get_ele(self,key):
        find_ele = FindElement(self.driver)
        element = find_ele.get_element(key)
        return element
    
    #输入元素
    def send_value(self,value,key):
        element = self.get_ele(key)
        element.send_keys(value)

    #点击元素
    def click_element(self,key):
        self.get_ele(key).click()

    #等待
    def sleep_time(self):
        time.sleep(3)

    #关闭浏览器
    def close_brower(self):    #可以通过close_brower(self,*args)来兼容不知道传入多少个参数的情况，通过下标0，1……来取参数
        self.driver.close()

    #获取title
    def get_title(self):
        return self.driver.title