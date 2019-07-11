import os
import time

time_sleep = 1

try:
    print('执行SD01')
    os.system('SDbackup_01.py')
except:
    print('NG')
    pass

time.sleep(time_sleep)

try:
    print('执行SD02')
    os.system('SDbackup_02.py')
except:
    print('NG')
    pass

