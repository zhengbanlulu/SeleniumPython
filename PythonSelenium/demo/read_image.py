#coding = utf-8
import pytesseract
from PIL import Image

image = Image.open("F:/test.png")
text = pytesseract.image_to_string(image)
print(text)
#利用Pillow库读取图片
#利用pytesseract库将图片转成文字,但是pytesseract库识别能力有限，选择使用第三方API