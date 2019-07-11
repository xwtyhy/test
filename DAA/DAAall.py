import os
import time

#设置脚本间隔时间，时间小于60秒会导致连续执行失败
time_sleep = 3

try:
    print('开始执行DAA-01-102.py')
    os.system('DAA-01-102.py')
except:
    print('NG')

time.sleep(time_sleep)

try:
    print('开始执行DAA-01-104.py')
    os.system('DAA-01-104.py')
except:
    print('NG')

time.sleep(time_sleep)

try:
    print('开始执行15w_DAA_1-1-1-5.py')
    os.system('15w_DAA_1-1-1-5.py')
except:
    print('NG')
