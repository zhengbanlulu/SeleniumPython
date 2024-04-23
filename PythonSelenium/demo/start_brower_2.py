#coding = utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.get("http://www.5itest.cn/register")

#element = driver.find_element_by_class_name("controls")
#WebDriverWait(driver,10).until(EC.visibility_of(element))
#visibility_of传的参数为元素

locator = (By.CLASS_NAME,"controls")
WebDriverWait(driver,10).until(EC.visibility_of_element_located(locator))
#visibility_of_element_located传的参数为定位方式

#在规定时间内找到了这个元素就往下运行，如果没找到就返回false
#用来寻找 class name 为 controls 的元素是否可见

#presence_of_all_elements_located检测该定位方式至少有一个元素存在