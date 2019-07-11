#定义desired_caps
from appium import webdriver


def getinfo():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'BH9300NEDP',
        'platformVersion': '9',
        'appPackage': 'com.nttdocomo.android.sdcardbackup',
        'appActivity': '.view.LaunchActivity',
        'automationName': 'uiautomator2'
    }
    global driver
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return desired_caps

def getdriver():
    return driver


