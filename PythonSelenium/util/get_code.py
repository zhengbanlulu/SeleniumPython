#coding = utf-8
from selenium import webdriver
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
from selenium.webdriver.common.by import By
import time
class GetCode(object):
    def __init__(self,driver):
        self.driver = driver
    #获取验证码图片
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element =  self.driver.find_element(by=By.ID, value="getcode_num")
        print(type(code_element))
        print(code_element.location) #{"x":123,"y":345}
        #找到验证码图片的四个角坐标
        left = code_element.location['x']
        top = code_element.location['y']
        right = left + code_element.size['width']
        bottom = top + code_element.size['height'] 
        
        #利用Pillow库裁剪整个页面中的验证码图片
        im = Image.open(file_name)
        img = im.crop((left,top,right,bottom))
        img.save(file_name)
        time.sleep(2)
        

    #解析验证码图片获取信息
    def get_code_text(self,file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
        r.addBodyPara("typeId","35")
        r.addBodyPara("convert_to_jpg","0")
        r.addFilePara("image",file_name)
        res = r.post() #输出格式为json格式
        text = res.json()['showapi_res_id'] #text = res.json()['showapi_res_body']['Result']
        time.sleep(2)
        return text