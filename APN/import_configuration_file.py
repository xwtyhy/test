# -*- coding: utf-8 -*-
import os

#删除既存的APN配置文件
os.system('adb shell rm /sdcard/*.apn')

#获取端末厂商，判断是否是samsung端末，samsung端末使用的配置文件与其它端末不同
brand = os.popen('adb -d shell getprop ro.product.brand') #查询厂商并取得返回值
brand = brand.read() #os.popen返回的是地址，需要read()读出值

if brand == 'samsung' or 'samsung' in brand:  #取得的内容可能空格或换行，所以追加in条件
    os.system('adb push Setting_File_SC sdcard/')
else:
    os.system('adb push Setting_File sdcard/')
