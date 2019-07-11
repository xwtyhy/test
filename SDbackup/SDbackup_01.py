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
        'automationName': 'uiautomator2'
    }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(1)

driver.find_element_by_id('com.nttdocomo.android.sdcardbackup:id/checkboxAgree').click() #通过ID选择「同意する」
driver.find_element_by_android_uiautomator('text("利用開始")').click()


driver.find_element_by_android_uiautomator('text("バックアップ＆復元")').click()
driver.find_element_by_android_uiautomator('text("スタート")').click()
time.sleep(1)
for i in range(6):
    try:
        driver.find_element_by_android_uiautomator('text("許可")').click()
    except:
        continue

driver.find_element_by_id('com.nttdocomo.android.sdcardbackup:id/menu_export_button').click() #通过ID选择「バックアップ」
driver.find_element_by_android_uiautomator('text("すべて選択")').click()

check = driver.find_element_by_id("com.nttdocomo.android.sdcardbackup:id/checkBoxHistory").get_attribute("checked") #checked値を取得

#输出结果
time = time.strftime("%Y-%m-%d %X",time.localtime())
if check == 'true':
    print(os.path.basename(__file__)+'->OK')
    result = open('result/SDbackup.txt', mode='a')
    result.write('\n'+'SDbackup_01 '+time+' OK')
    result.close()
    driver.get_screenshot_as_file('result/SDbackup_01_OK.png')
else:
    print(os.path.basename(__file__)+'->NG')
    result = open('result/SDbackup.txt', mode='a')
    result.write('\n'+'SDbackup_01 '+time+' NG')
    result.close()
    driver.get_screenshot_as_file('result/SDbackup_01_NG.png')

driver.close_app()
driver.quit()