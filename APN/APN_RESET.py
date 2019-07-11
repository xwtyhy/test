# -*- coding: utf-8 -*-
from appium import webdriver
import time
import os
import APPinfo

#APN設定画面で「リセット」を実行
desired_caps = APPinfo.getinfo()
driver = APPinfo.getdriver()
time.sleep(1)

os.system('adb shell am start -a android.settings.DATA_ROAMING_SETTINGS')

try:
    driver.find_element_by_android_uiautomator('text("詳細設定")').click()
except:
    print('「詳細設定」がありません')

try:
    driver.find_element_by_android_uiautomator('text("アクセスポイント名")').click()
except:
    print('「詳細設定」がありません')
    exit('「アクセスポイント名」を選択失敗、再修正必要')

#メニューキーを押し
driver.keyevent(82)

#リセトを選択
try:
    driver.find_element_by_android_uiautomator('text("リセト")').click()
except:
    try:
        driver.find_element_by_android_uiautomator('text("初期設定に戻す")').click()
    except:
        print('NG! APN設定メニューの文言が修正必要')

#wait３秒、リセトしたのAPNは自動でSPモードに設定
time.sleep(3)

print('APNをリセットしました')