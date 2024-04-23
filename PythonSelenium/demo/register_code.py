from selenium import webdriver
import time
import random
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#浏览器初始化
def driver_init():
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()
    time.sleep(5)

#获取element信息
def get_element(id):
    element = driver.find_element(by=By.ID, value=id)
    print(type(element))
    return element

#获取随机数
def get_range_user():
    user_info = ''.join(random.sample("1234567890abcdefg",8))
    return user_info

#获取验证码图片
def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_element =  driver.find_element(by=By.ID, value="getcode_num")
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

def get_code_text(file_name):
    r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
    r.addBodyPara("typeId","35")
    r.addBodyPara("convert_to_jpg","0")
    r.addFilePara("image",file_name)
    res = r.post() #输出格式为json格式
    text = res.json()['showapi_res_id'] #text = res.json()['showapi_res_body']['Result']
    return text

def run_main():
    user_name_info = get_range_user()
    user_email = user_name_info + "@163.com"
    file_name = 'D:/PythonSelenium/image/imooc_test1.png'
    driver_init()
    get_element("register_email").send_keys(user_email)
    get_element("register_nickname").send_keys(user_name_info)
    get_element("register_password").send_keys("12345678")
    get_code_image(file_name)
    text = get_code_text(file_name)
    get_element("captcha_code").send_keys(text)
    get_element("register-btn").click()
    driver.close()

run_main()