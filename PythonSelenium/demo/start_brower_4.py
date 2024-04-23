#coding = utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import random
from PIL import Image
from util.ShowapiRequest import ShowapiRequest

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
time.sleep(5)
print(EC.title_contains("注册"))

driver.save_screenshot("F:/imooc_test.png")
code_element =  driver.find_element(By.ID,"getcode_num")
print(code_element.location) #{"x":123,"y":345}
left = code_element.location['x']
top = code_element.location['y']
right = left + code_element.size['width']
bottom = top + code_element.size['height'] 
#找到验证码图片的四个角坐标

im = Image.open("F:/imooc_test.png")
img = im.crop((left,top,right,bottom))
img.save("F:/imooc_test1.png")
#利用Pillow库裁剪整个页面中的验证码图片

r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
r.addBodyPara("typeId","35")
r.addBodyPara("convert_to_jpg","0")
r.addFilePara("image",r"F:/imooc_test1.png")
res = r.post() #输出格式为json格式
text = res.json()['showapi_res_id'] #text = res.json()['showapi_res_body']['Result']
print(res.text)

driver.find_element(By.ID,"captcha_code").send_keys(text)
time.sleep(5)
driver.close()
