#coding = utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import random

for i in range (5):
    usr_email =  ''.join(random.sample("0123456789abcdefg",5))+"@163.com"
    #''.join()将list转换成str
    print(usr_email)

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.get("http://www.5itest.cn/register")


pw_element = driver.find_element_by_name("email")
print(pw_element.get_attribute("placeholder"))
pw_element.send_keys(usr_email)
print(pw_element.get_attribute("value"))

driver.close()

#调用随机数生成用户名，邮箱地址等