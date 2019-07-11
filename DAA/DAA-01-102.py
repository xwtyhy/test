from appium import webdriver
import time
import os
import APPinfo

#「設定」画面に遷移

desired_caps = APPinfo.getinfo()
driver = APPinfo.getdriver()
time.sleep(1)

#「アカウント」を選択
while True:
    try:
        driver.find_element_by_android_uiautomator('text("アカウント")').click()
        break
    except:
        for i in range(1):
            height = driver.get_window_size()['height']
            width = driver.get_window_size()['width']
            driver.swipe(width * 0.5, height * 0.6, width * 0.5, height * 0.3)

#アカウント追加できないの確認
driver.find_element_by_android_uiautomator('text("アカウントを追加")').click()
driver.find_element_by_android_uiautomator('text("docomo")').click()
try:
    driver.find_element_by_android_uiautomator('text("以下のアカウントは既に登録されています")')
    print('OK')
    temp = 'OK'
except:
    try:
        driver.find_element_by_android_uiautomator('text("以下のアカウントの登録が完了しました")')
        print('OK')
        temp = 'OK'
    except:
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