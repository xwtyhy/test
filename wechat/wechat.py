from appium import webdriver
import time
import os
import APPinfo


desired_caps = APPinfo.getinfo()
driver = APPinfo.getdriver()
time.sleep(3)

while True:
    try:
        driver.find_element_by_android_uiautomator('text("WeChat")')
        try:
            driver.find_element_by_android_uiautomator('text("大连捉妖交流群")').click()
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
                driver.keyevent('4')
        except:
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
                driver.keyevent('4')
            pass

        try:
            driver.find_element_by_android_uiautomator('text("一起来捉妖-夏天来了")').click()
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
                driver.keyevent('4')
        except:
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
                driver.keyevent('4')
            pass

        try:
            driver.find_element_by_android_uiautomator('text("不思议迷宫 | LokTar联盟")').click()
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
                driver.keyevent('4')
        except:
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
                driver.keyevent('4')
            pass
    except:
        os.system('adb shell am start com.tencent.mm/com.tencent.mm.ui.LauncherUI')
        time.sleep(5)
