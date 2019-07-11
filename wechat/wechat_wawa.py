from appium import webdriver
import time
import os
import APPinfo

desired_caps = APPinfo.getinfo()
driver = APPinfo.getdriver()
time.sleep(8)
print('自动化科学饲养监控程序开始')

#运行环境开关，正式环境：1   测试环境：2
formal = 2
if formal ==1:
    name = 'text("️胖娃娃")'
else:
    name = 'text("笑问天")'

time_09,time_13,time_20,time_21 = 'F'
while True:
    try:
        driver.find_element_by_android_uiautomator('text("連絡先")')
        print('当前为主界面，继续执行')
        try:
            # 根据当前时间编辑发送内容
            time_now = time.strftime("%X", time.localtime())  # 当前时间取得
            time_H = time_now[0:2]
            if time_H == '09'and time_09 == 'F':
                inputtext = '吃早饭了么'
                time_09 = 'T'
            elif time_H =='13' and time_13 == 'F':
                inputtext = '吃午饭了么'
                time_13 = 'T'
            elif time_H == '20'and time_20 == 'F':
                inputtext = '吃晚饭了么'
                time_20 = 'T'
            elif time_H == '21'and time_21 == 'F':
                inputtext = '吃药了么'
                time_21 = 'T'
            elif time_H == '23':
                time_09,time_13,time_20,time_21 = 'F'
            else:
                inputtext = 'exit'


            # 点击输入栏，发送文本
            if inputtext != 'exit':
                driver.find_element_by_android_uiautomator(name).click()
                driver.find_element_by_id('com.tencent.mm:id/ami').send_keys(inputtext) #通过ID选择输入框，并发送文本
                driver.find_element_by_android_uiautomator('text("送信")').click()
            else:
                print('当前为非询问时间点')
                time.sleep(600)
                pass
        except:
            print('饲养目标选择失败，重启APP')
            driver.close_app()
            time.sleep(2)
            os.system('adb shell am start com.tencent.mm/com.tencent.mm.ui.LauncherUI')
            time.sleep(8)
    except:
        print('未找到主界面，重启APP')
        driver.close_app()
        time.sleep(2)
        os.system('adb shell am start com.tencent.mm/com.tencent.mm.ui.LauncherUI')
        time.sleep(8)
