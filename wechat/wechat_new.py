from appium import webdriver
import time
import os
import APPinfo

group = ['大连捉妖交流群','一起来捉妖-夏天来了','不思议迷宫 | LokTar联盟']  #输入相应的捉妖群的群名


desired_caps = APPinfo.getinfo()
driver = APPinfo.getdriver()
time.sleep(8)
c = 0
i = 0
while True:
    try:
        print('本次累计悬赏成功：' + str(c))
        time.sleep(1)
        driver.find_element_by_android_uiautomator('text("連絡先")')  #主界面判断，中文系统改为[通讯录]
        print('当前为主界面，继续执行')
        try:
            name = 'text(' + '\"' + group[i] + '\"' + ")"
            print('当前群：'+ group[i])
            driver.find_element_by_android_uiautomator(name).click()
            print('进入' + group[i] +'成功')
            if i < (len(group) - 1):
                i += 1
            else:
                i = 0
            try:
                driver.find_element_by_android_uiautomator('text("妖灵悬赏")').click()
                print('当前群点击悬赏成功')
                time.sleep(10)
                try:
                    driver.find_element_by_android_uiautomator('text("确定")')
                    print('当前画面显示[确定]POPUP，点击关闭')
                    driver.find_element_by_id('com.tencent.mm:id/ot').click()
                except:
                    pass
                try:
                    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[4]/android.view.View[1]/android.widget.Image').click()
                    print('悬赏成功')
                    c += 1
                    print('本次累计悬赏成功：'+ c)
                    driver.find_element_by_id('com.tencent.mm:id/ot').click()
                    driver.keyevent('4')
                except:
                    driver.find_element_by_id('com.tencent.mm:id/ot').click()
                    time.sleep(1)
                    driver.keyevent('4')
            except:
                print('当前群未找到[悬赏]，返回前一页面')
                driver.keyevent('4')
        except:
            print('进入群失败，尝试寻找悬赏')
            try:
                driver.find_element_by_android_uiautomator('text("妖灵悬赏")').click()
                time.sleep(5)
                try:
                    driver.find_element_by_android_uiautomator('text("确定")')
                    driver.find_element_by_id('com.tencent.mm:id/ot').click()
                except:
                    pass
                try:
                    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[4]/android.view.View[1]/android.widget.Image').click()
                    driver.find_element_by_id('com.tencent.mm:id/ot').click()
                    driver.keyevent('4')
                except:
                    driver.find_element_by_id('com.tencent.mm:id/ot').click()
                    driver.keyevent('4')
            except:
                print('未找到悬赏，返回前一界面')
                driver.keyevent('4')
            pass
    except:
        print('未找到主界面，重启APP')
        driver.close_app()
        time.sleep(2)
        os.system('adb shell am start com.tencent.mm/com.tencent.mm.ui.LauncherUI')
        time.sleep(8)
