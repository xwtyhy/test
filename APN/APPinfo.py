#定义desired_caps
from appium import webdriver
import os
import re

def getinfo():
    readDeviceId = list(os.popen('adb devices').readlines())
    deviceName = re.findall(r"^\w*\b", readDeviceId[1])[0]
    deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
    platformVersion = re.findall(r"^\w*\b", deviceAndroidVersion[0])[0]
    desired_caps = {
        'platformName': 'Android',
        'deviceName': deviceName,
        'platformVersion': platformVersion,
        'appPackage': 'com.android.settings',
        'appActivity': '.Settings',
        'automationName': 'uiautomator2',
        'noReset': 'True'
    }
    global driver
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return desired_caps

def getdriver():
    return driver
