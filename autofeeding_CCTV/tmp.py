from appium import webdriver
import time
import os
import APPinfo
from inputtext import inputtext
from determine import *

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

#APP启动检测,判断主画面的"連絡先"是否显示
try:
    driver.find_element_by_android_uiautomator('text("連絡先")')
except:
    print('未找到主界面，重启APP')
    desired_caps = APPinfo.getinfo()
    driver = APPinfo.getdriver()
    time.sleep(10)

#发送欢迎语
welcome1 = '宝宝你好，自动饲养监控程序已启动。\n'
welcome2 = '查询模块已上线，欢迎试用。\n'
welcome3 = '回复数字1：开发进度查询。2：呼叫主人。3：调取监控画面（未完成）'
welcome = welcome1 + welcome2 + welcome3
driver.find_element_by_android_uiautomator(name).click()
time.sleep(1)
driver.find_element_by_id('com.tencent.mm:id/ami').send_keys(welcome)  # 通过ID选择输入框，并发送文本
driver.find_element_by_android_uiautomator('text("送信")').click()
driver.keyevent('4')  # backkey,返回主画面

while True:
    # 对反馈信息进行分析，并给出返回值
    check = pet_for_main(driver)
    print(check)
    # 根据取得的返回值判断是否需要执行下一步动作
    # if check == 'safe':
    #     print('饲养目标状态正常')
    #     print('等待一小时,执行下一次循环')
    #     time.sleep(3600)  # 该时间段的询问已经得到反馈,等待1小时进行下一次循环
    # else:
    #     # 返回值为‘warning’的场合执行汇报动作
    #     print('饲养目标状态异常，执行汇报程序')
    #     master(driver, check)  # 调用汇报方法,汇报逻辑持续更新中
    #     print('等待一小时,执行下一次循环')
    #     time.sleep(3600)  # 该时间段的询问已经得到反馈,等待1小时进行下一次循环
    #
    #
    # while True:    #时间逻辑自动询问循环体
    #     try:
    #         driver.find_element_by_android_uiautomator('text("連絡先")')
    #         print('当前为主界面，继续执行')
    #     except:
    #         print('未找到主界面，重启APP')
    #         desired_caps = APPinfo.getinfo()
    #         driver = APPinfo.getdriver()
    #         time.sleep(10)
    #         try:
    #             driver.find_element_by_android_uiautomator('text("連絡先")')
    #             print('当前为主界面，继续执行')
    #         except:
    #             print('重启APP失败，启动汇报程序')
    #             statuscode = 0
    #             master(driver,statuscode)
    #             exit('监控程序运行失败，已执行汇报程序')
    #
    #     time_now = time.strftime("%X", time.localtime())  # 当前时间取得
    #     time_H = time_now[0:2]
    #     text = inputtext(time_H)
    #     if text != 'exit':
    #         driver.find_element_by_android_uiautomator(name).click()
    #         time.sleep(1)
    #         driver.find_element_by_id('com.tencent.mm:id/ami').send_keys(text)  # 通过ID选择输入框，并发送文本
    #         driver.find_element_by_android_uiautomator('text("送信")').click()
    #         driver.keyevent('4')  # backkey,返回主画面
    #         # 对反馈信息进行分析，并给出返回值
    #         check = pet_for_time(driver, text)
    #         # 根据取得的返回值判断是否需要执行下一步动作
    #         if check == 'safe':
    #             print('饲养目标状态正常')
    #             print('等待一小时,执行下一次循环')
    #             time.sleep(3600) #该时间段的询问已经得到反馈,等待1小时进行下一次循环
    #         else:
    #             # 返回值为‘warning’的场合执行汇报动作
    #             print('饲养目标状态异常，执行汇报程序')
    #             master(driver, check)  #调用汇报方法,汇报逻辑持续更新中
    #             print('等待一小时,执行下一次循环')
    #             time.sleep(3600) #该时间段的询问已经得到反馈,等待1小时进行下一次循环
    #     else:
    #         print('当前为非询问时间点，等待３０分钟，现在时间：'+time_now)
    #         time.sleep(1800)