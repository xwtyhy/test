from appium import webdriver
import time
import os
import APPinfo

#「設定」画面に遷移
desired_caps = {
        'platformName': 'Android',
        'deviceName': 'L03K12f02a0',
        'platformVersion': '9',
        'appPackage': 'com.android.settings',
        'appActivity': '.Settings',
        'automationName': 'uiautomator2'
    }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# desired_caps = APPinfo.getinfo()
# driver = APPinfo.getdriver()
# time.sleep(1)

#「アプリ情報」画面に遷移
os.system('adb shell am start -a android.settings.APPLICATION_DETAILS_SETTINGS package:com.nttdocomo.android.accountauthenticator')
time.sleep(1)
try:
    driver.find_element_by_android_uiautomator('text("ストレージ")').click()
except:
    try:
        driver.find_element_by_android_uiautomator('text("SDカードと保存領域")').click()
    except:
        print('ストレージ画面に遷移失敗')

#データを消去前の値を取得
check1 = driver.find_element_by_id("android:id/summary").get_attribute("text")

driver.find_element_by_android_uiautomator('text("データを消去")').click()
driver.find_element_by_android_uiautomator('text("OK")').click()

#データを消去後の値を取得
check2 = driver.find_element_by_id("android:id/summary").get_attribute("text")

#消去前後の値が変化しないの確認
if check1 == check2:
    print('OK')
    temp = 'OK'
else:
    print('NG')
    temp = 'NG'

#输出结果
time = time.strftime("%Y-%m-%d %X",time.localtime())
if temp == 'OK':
    print(os.path.basename(__file__)+'->OK')
    result = open('result/DAA.txt', mode='a')
    path = '\n' + os.path.basename(__file__) + ' ' + time + ' OK'
    result.write(path)
    result.close()
    driver.get_screenshot_as_file('result/'+os.path.basename(__file__)+'_OK.png')
else:
    print(os.path.basename(__file__)+'->NG')
    result = open('result/DAA.txt', mode='a')
    path = '\n'+os.path.basename(__file__)+' '+time+' NG'
    result.write(path)
    result.close()
    driver.get_screenshot_as_file('result/'+os.path.basename(__file__)+'_NG.png')

driver.close_app()