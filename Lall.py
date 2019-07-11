# -*- coding: utf-8 -*-
from appium import webdriver
import os
import time
import L1

def main():
    desired_caps = {
                'platformName': 'Android',
                'deviceName': 'BH9300NEDP',
                'platformVersion': '9',
                'appPackage': 'com.nttdocomo.android.sdcardbackup',
                'appActivity': '.view.LaunchActivity',
                'automationName': 'uiautomator2'
            }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver
time.sleep(1)
driver = main()

L1.SD01(driver)



# #if __name__ == '__main__':
# print('定义desired_caps')
# global desired_caps
# desired_caps = {
#     'platformName': 'Android',
#     'deviceName': 'L03K12f02a0',
#     'platformVersion': '9',
#     'appPackage': 'com.android.settings',
#     'appActivity': '.Settings',
#     'automationName': 'uiautomator2'
# }
# print('定义driver')
# global driver
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# print('定义driverinfo')
# global driverinfo
# driverinfo = driver
# def getinfo():
#     return desired_caps
#
# def getdriverinfo():
#     return driverinfo
#
# if __name__ == '__main__':
#     print('开始执行L1.py')
#     os.system('L1.py')
#
#     print('开始执行L2.py')
#     os.system('L2.py')


