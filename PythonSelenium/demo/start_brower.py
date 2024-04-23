#coding = utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.get("http://www.5itest.cn/register")
time.sleep(5)
print(EC.title_contains("注册"))

driver.find_element(by=By.ID,value="register_email").send_keys("testtest@123.com")

driver.close()

'''
driver.find_element_by_id("register_email").send_keys("testtest@123.com")

#父节点
user_name_element_node = driver.find_elements_by_class_name("controls")[1]
#find_elements_by...才会返回list
#print(len(xxx))   方便查看同名元素有几个，定位到多个同名元素时只会操作第一个，因此要找到唯一定位的方式
#子节点
user_element = user_name_element_node.find_element_by_class_name("form-control")
user_element.send_keys("abcdefg")

driver.find_element_by_name("password").send_keys("12345678")
driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("1111111")
#xpath可以通过在浏览器开发者模式控制台右键该元素copy xpath获取，中间的双引号注意替换为单引号
'''