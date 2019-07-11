# -*- coding: utf-8 -*-

from appium import webdriver
import time
import os
import APPinfo

#创建请求
desired_caps = APPinfo.getinfo()
driver = APPinfo.getdriver()

#主脚本判断，作为主脚本运行时，执行下记设定条件
if __name__ == '__main__':
    #appsigneを判断
    while True:
        appsigne = input('appsigneを設定（numberを入力ください）、１：商用　　２：開発　　３：スクリプトを終了')
        if appsigne  in ['1','2','１','２']:
            print('ご入力の内容は：'+appsigne)
            break
        elif appsigne in ['3','３']:
            exit('スクリプト終了')
        else:
            print('ご入力の内容ミス、再入力必要')

    #appsigneによりAPPをインストール
    if appsigne in ['1','１']:  #ApnManagerとApnSwitcher:商用の場合、下記APPをインストール
        os.system('adb install -r APP/comm/ApnManager_on_sha2_v2.apk')
        os.system('adb install -r APP/comm/ApnSwitcher_sha2_v2.apk')
    elif appsigne in ['2','２']:   #ApnManagerとApnSwitcher:開発の場合、下記APPをインストール
        os.system('adb install -r APP/dev/ApnManager_signed_on_sha2.apk')
        os.system('adb install -r APP/dev/ApnSwitcher_signed_on_sha2.apk')

    os.system('adb install -r APP/ApnManagerClientSample.apk')  #ApnManagerClientSample：商用と開発は同じです

    #設定ファイルのインポート
    os.system('import_configuration_file.py')

# WiFi ON
os.system('adb shell svc wifi enable')

#APNリセットを実行
os.system('APN_RESET.py')

# #「設定」画面に遷移


#
# #「アカウント」を選択
# while True:
#     try:
#         driver.find_element_by_android_uiautomator('text("アカウント")').click()
#         break
#     except:
#         for i in range(1):
#             height = driver.get_window_size()['height']
#             width = driver.get_window_size()['width']
#             driver.swipe(width * 0.5, height * 0.6, width * 0.5, height * 0.3)
#
# #アカウントを削除できないことを確認
# driver.find_element_by_android_uiautomator('text("docomo")').click()
# driver.find_element_by_android_uiautomator('text("アカウントを削除")').click()
# driver.find_element_by_id('android:id/button1').click() #通过ID选择「削除」
# time.sleep(1)
#
# try:
#     driver.find_element_by_android_uiautomator('text("この変更は管理者によって許可されていません")')
#     print('OK')
#     temp = 'OK'
# except:
#     print('NG')
#     temp = 'NG'
#
#
# #输出结果
# time = time.strftime("%Y-%m-%d %X",time.localtime())
# if temp == 'OK':
#     print(os.path.basename(__file__)+'->OK')
#     result = open('result/DAA.txt', mode='a')
#     path = '\n' + os.path.basename(__file__) + ' ' + time + ' OK'
#     result.write(path)
#     result.close()
#     driver.get_screenshot_as_file('result/'+os.path.basename(__file__)+'_OK.png')
# else:
#     print(os.path.basename(__file__)+'->NG')
#     result = open('result/DAA.txt', mode='a')
#     path = '\n'+os.path.basename(__file__)+' '+time+' NG'
#     result.write(path)
#     result.close()
#     driver.get_screenshot_as_file('result/'+os.path.basename(__file__)+'_NG.png')
#
# driver.close_app()