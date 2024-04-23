#coding = utf-8
from util.read_ini import ReadIni
from selenium.webdriver.common.by import By

class FindElement(object):
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element(By.ID,value)
            elif by == 'name':
                return self.driver.find_element(By.NAME,value)
            elif by == 'className':
                return self.driver.find_element(By.CLASS_NAME,value)
            else:
                return self.driver.find_element(By.XPATH,value)
        except:
            #self.driver.save_screenshot('D:/PythonSelenium/image/%s.png'%value)   #报错时截图
            return None