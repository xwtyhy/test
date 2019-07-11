import pymouse
import time
m = pymouse.PyMouse()
x,y =m.position()#获取当前坐标的位置

m.move(x - 50, y)
while True:
    time.sleep(290)
    m.move(x-1,y)
    time.sleep(290)
    m.move(x+1,y)