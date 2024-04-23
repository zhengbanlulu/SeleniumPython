#coding = utf-8
import sys
sys.path.append('D:/PythonSelenium')
from selenium import webdriver
import time
import random
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
from selenium.webdriver.common.by import By
from base.find_element import FindElement
from selenium.webdriver.remote.webelement import WebElement

class RegisterFunction(object):
    def __init__(self,url,i):
        self.driver = self.get_driver(url,i)
    #获取driver并且打开url
    def get_driver(self,url,i):
        if i == 1:
            driver = webdriver.Chrome()
        else :
            driver = webdriver.Edge()
        driver.get(url)
        driver.maximize_window()
        time.sleep(5)
        return driver
    #输入用户信息
    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)

    #定位用户信息，获取element
    def get_user_element(self,key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element
    
    #获取随机数
    def get_range_user(self):
        user_info = ''.join(random.sample("1234567890abcdefg",8))
        return user_info

    #获取验证码图片
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element =  self.get_user_element("code_image")
        print(type(code_element))
        print(code_element.location) #{"x":123,"y":345}
        left = code_element.location['x']
        top = code_element.location['y']
        right = left + code_element.size['width']
        bottom = top + code_element.size['height'] 
        #找到验证码图片的四个角坐标

        im = Image.open(file_name)
        img = im.crop((left,top,right,bottom))
        img.save(file_name)
        #利用Pillow库裁剪整个页面中的验证码图片

    #解析验证码图片获取信息
    def get_code_text(self,file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
        r.addBodyPara("typeId","35")
        r.addBodyPara("convert_to_jpg","0")
        r.addFilePara("image",file_name)
        res = r.post() #输出格式为json格式
        text = res.json()['showapi_res_id'] #text = res.json()['showapi_res_body']['Result']
        return text
    
    def main(self,i):
        user_name_info = self.get_range_user()
        user_email = user_name_info + "@163.com"
        file_name = 'D:/PythonSelenium/image/imooc_test2.png'
        code_text = self.get_code_text(file_name)
        self.send_user_info('user_email',user_email)
        self.send_user_info('user_name',user_name_info)
        self.send_user_info('user_password','12345678')
        self.send_user_info('code_text',code_text)
        self.get_user_element('register_button').click()
        code_error = self.get_user_element('code_text_error')
        if code_error == None:
            print('注册成功！')
        else:
            print('注册失败！')
            self.driver.save_screenshot('D:/PythonSelenium/image/code_error'+str(i)+'.png')
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    for i in range(2):
        register_function = RegisterFunction("http://www.5itest.cn/register",i)
        register_function.main(i)