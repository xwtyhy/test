import time
from selenium import webdriver

def mac():
    driver = webdriver.chrome()
    driver.implicitly_wait(5)
    driver.get("http://huazhu.gag.com/mis/main.do")