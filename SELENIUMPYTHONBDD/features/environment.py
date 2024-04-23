#coding = utf-8
from selenium import webdriver
import time

def before_all(context):
    context.driver =  webdriver.Chrome()

def after_all(context):
    time.sleep(3)
    context.driver.close()