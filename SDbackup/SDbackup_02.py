# -*- coding: utf-8 -*-

from appium import webdriver
import time
import os

desired_caps = {
        'platformName': 'Android',
        'deviceName': 'BH9300NEDP',
        'platformVersion': '9',
        'appPackage': 'com.nttdocomo.android.sdcardbackup',
        'appActivity': '.view.LaunchActivity',
        # 'noReset': 'True',
        'automationName': 'uiautomator2'
    }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(3)

try:
    driver.find_element_by_id('com.nttdocomo.android.sdcardbackup:id/checkboxAgree').click() #通过ID选择「同意する」
    driver.find_element_by_android_uiautomator('text("利用開始")').click()
except:
    pass

time.sleep(1)
driver.find_element_by_android_uiautomator('text("バックアップ＆復元")').click()
try:
    driver.find_element_by_android_uiautomator('text("スタート")').click()
    for i in range(6):
        try:
            driver.find_element_by_android_uiautomator('text("許可")').click()
        except:
            pass
except:
    pass

driver.find_element_by_android_uiautomator('text("復元")').click()
time.sleep(3)
driver.find_element_by_android_uiautomator('text("最新データを選択")').click()
time.sleep(1)
driver.find_element_by_android_uiautomator('text("復元開始")').click()
time.sleep(1)
driver.find_element_by_android_uiautomator('text("開始する")').click()
time.sleep(10)
driver.find_element_by_android_uiautomator('text("復元結果")')

check = driver.find_element_by_id("com.nttdocomo.android.sdcardbackup:id/textResult").get_attribute("text")

#输出结果
time = time.strftime("%Y-%m-%d %X",time.localtime())
if check == '成功':
    print(os.path.basename(__file__)+'->OK')
    result = open('result/SDbackup.txt', mode='a')
    result.write('\n'+'SDbackup_02 '+time+' OK')
    result.close()
    driver.get_screenshot_as_file('result/SDbackup_02_OK.png')
else:
    print(os.path.basename(__file__)+'->NG')
    result = open('result/SDbackup.txt', mode='a')
    result.write('\n'+'SDbackup_02 '+time+' NG')
    result.close()
    driver.get_screenshot_as_file('result/SDbackup_02_NG.png')

driver.close_app()
driver.quit()