import random
import time


def list9X9():
    con = 0  # 统计用变量
    msg_display = 'ON'  # 信息显示开关
    # 定义生成9个随机数字的方法
    def random_num_9():
        i = 0
        list_tmp = []
        while i < 9:  # 生成９个不重复数字
            a = random.randint(1, 9)
            if a not in list_tmp:
                list_tmp.append(a)
                i += 1
            else:
                pass
        return list_tmp
    global list_complete,list1,list2,list3,list4,list5,list6,list7,list8,list9
    # 对所有list初始化
    list_complete =[]
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list9 = []
    while True:
        if len(list_complete) == 9:
            break
        else:
            # 生成子list1
            list1 = random_num_9()
            if msg_display == 'ON':
                print('生成的list1:', list1)

            # 生成子list2
            while True:
                try:
                    list_x = []
                    list_tmp = random_num_9()  # 创建一个临时列表
                    i = 0
                    c = 0  # 当前位数判断
                    while True:
                        if len(list_tmp) == 0:
                            break
                        elif list_tmp[i] not in list1[0:3] and c <= 2:
                            list_x.append(list_tmp[i])
                            list_tmp.pop(i)
                            c += 1
                            i = 0
                        elif list_tmp[i] not in list1[3:6] and 3 <= c <= 5:
                            list_x.append(list_tmp[i])
                            list_tmp.pop(i)
                            c += 1
                            i = 0
                        elif list_tmp[i] not in list1[6:] and 6 <= c <= 8:
                            list_x.append(list_tmp[i])
                            list_tmp.pop(i)
                            c += 1
                            i = 0
                        else:
                            i += 1
                    break
                except:
                    if len(list_x) == 9:
                        break
                    else:
                        pass
                    pass
            list2 = list_x
            if msg_display == 'ON':
                print('生成的list2:', list2)

            # 生成子list3
            while True:
                list_x = []
                list_tmp = random_num_9()  # 创建一个临时列表
                i = 0
                c = 0  # 当前位数判断
                a = 0  # 统计循环次数
                try:
                    while True:
                        if len(list_tmp) == 0:
                            break
                        elif list_tmp[i] not in (list1[0:3] + list2[0:3]) and c <= 2:
                            list_x.append(list_tmp[i])
                            list_tmp.pop(i)
                            c += 1
                            i = 0
                        elif list_tmp[i] not in (list1[3:6] + list2[3:6]) and 3 <= c <= 5:
                            list_x.append(list_tmp[i])
                            list_tmp.pop(i)
                            c += 1
                            i = 0
                        elif list_tmp[i] not in (list1[6:] + list2[6:]) and 6 <= c <= 8:
                            list_x.append(list_tmp[i])
                            list_tmp.pop(i)
                            c += 1
                            i = 0
                        else:
                            if a <= 81:
                                i += 1
                                a += 1
                                pass
                            else:
                                break
                    break
                except:
                    if len(list_x) == 9:
                        break
                    else:
                        pass
            list3 = list_x
            if msg_display == 'ON':
                print('生成的list3:', list3)

            # 生成子list4
            list_x = []  # 初始化list_x
            while True:
                if len(list_x) == 9:
                    break
                else:
                    list_x = []
                    list_tmp = random_num_9()  # 创建一个临时列表
                    i = 0  # 临时列表的下标
                    c = 0  # 当前位数判断
                    a = 0  # 统计循环次数
                    try:
                        while True:
                            if len(list_tmp) == 0:
                                break
                            elif list_tmp[i] not in (list1[c], list2[c], list3[c]):
                                list_x.append(list_tmp[i])
                                list_tmp.pop(i)
                                c += 1
                                i = 0
                            else:
                                if a <= 999:
                                    i += 1
                                    a += 1
                                else:
                                    break
                        break
                    except:
                        if len(list_x) == 9:
                            break
                        else:
                            pass
            list4 = list_x
            if msg_display == 'ON':
                print('生成的list4:', list4)

            # 生成子list5
            list_x = []  # 初始化list_x
            while True:
                if len(list_x) == 9:
                    break
                else:
                    list_x = []
                    list_tmp = random_num_9()  # 创建一个临时列表
                    i = 0  # 临时列表的下标
                    c = 0  # 当前位数判断
                    a = 0  # 统计循环次数
                    try:
                        while True:
                            # print('*list5*当前临时列表',list_tmp)
                            if len(list_tmp) == 0:
                                break
                            elif list_tmp[i] not in (
                            list1[c], list2[c], list3[c], list4[c], list4[0], list4[1], list4[2]) and c <= 2:
                                list_x.append(list_tmp[i])
                                list_tmp.pop(i)
                                c += 1
                                i = 0
                            elif list_tmp[i] not in (
                            list1[c], list2[c], list3[c], list4[c], list4[3], list4[4], list4[5]) and 3 <= c <= 5:
                                list_x.append(list_tmp[i])
                                list_tmp.pop(i)
                                c += 1
                                i = 0
                            elif list_tmp[i] not in (
                            list1[c], list2[c], list3[c], list4[c], list4[6], list4[7], list4[8]) and 6 <= c <= 8:
                                list_x.append(list_tmp[i])
                                list_tmp.pop(i)
                                c += 1
                                i = 0
                            else:
                                if a <= 999:
                                    i += 1
                                    a += 1
                                else:
                                    break
                        break
                    except:
                        if len(list_x) == 9:
                            break
                        else:
                            pass
            list5 = list_x
            if msg_display == 'ON':
                print('生成的list5:', list5)

            # 生成子list6
            list_x = []  # 初始化list_x
            con = 0  # 初始化统计用变量
            while True:
                if len(list_x) == 9:
                    break
                else:
                    list_x = []
                    list_tmp = random_num_9()  # 创建一个临时列表
                    i = 0  # 临时列表的下标
                    c = 0  # 当前位数判断
                    a = 0  # 统计循环次数
                    try:
                        while True:
                            # print('*list6*当前临时列表：',list_tmp)
                            # print('*list6*当前处理数据：', list_tmp[i])
                            # print('*list6*当前list_x：', list_x)
                            if len(list_tmp) == 0:
                                break
                            elif list_tmp[i] not in (
                            list1[c], list2[c], list3[c], list4[c], list5[c], list4[0], list4[1], list4[2], list5[0],
                            list5[1], list5[2]) and c <= 2:
                                # print('当前数据', list_tmp[i],'追加成功')
                                list_x.append(list_tmp[i])
                                list_tmp.pop(i)
                                # print('当前list_x',list_x)
                                c += 1
                                i = 0
                            elif list_tmp[i] not in (
                            list1[c], list2[c], list3[c], list4[c], list5[c], list4[3], list4[4], list4[5], list5[3],
                            list5[4], list5[5]) and 3 <= c <= 5:
                                list_x.append(list_tmp[i])
                                list_tmp.pop(i)
                                c += 1
                                i = 0
                            elif list_tmp[i] not in (
                            list1[c], list2[c], list3[c], list4[c], list5[c], list4[6], list4[7], list4[8], list5[6],
                            list5[7], list5[8]) and 6 <= c <= 8:
                                list_x.append(list_tmp[i])
                                list_tmp.pop(i)
                                c += 1
                                i = 0
                            else:
                                if a <= 999:
                                    i += 1
                                    a += 1
                                else:
                                    #print('***********a值超过最大循环***********')
                                    break
                        #print('***********赋值循环完成***********')
                        break
                    except:
                        if len(list_x) == 9:
                            break
                        else:
                            pass
                        # print('***********循环内出现未知错误***********')
                        # print('a=', a)
                        # print('i=', i)
                        # print('--------------')
                        # print(list1)
                        # print(list2)
                        # print(list3)
                        # print(list4)
                        # print(list5)
                        # print('--------------')
                        # print(list_tmp)
                        # print(list_x)
                        con += 1
                        #print('当前为第', con, '次失败')
                        if con == 999:
                            print('重试超过999次')
                            break
                        else:
                            pass
                        time.sleep(0)
            if len(list_x) < 9:
                print('list_x生成失败')
                continue
            list6 = list_x
            if msg_display == 'ON':
                print('生成的list6:', list6)

            # 生成子list7
            list_x = []  # 初始化list_x
            while True:
                if len(list_x) == 9:
                    break
                else:
                    list_x = []
                    list_tmp = random_num_9()  # 创建一个临时列表
                    i = 0  # 临时列表的下标
                    c = 0  # 当前位数判断
                    a = 0  # 统计循环次数
                    try:
                        while True:
                            if len(list_tmp) == 0:
                                break
                            elif list_tmp[i] not in (list1[c], list2[c], list3[c], list4[c], list5[c], list6[c]):
                                list_x.append(list_tmp[i])
                                list_tmp.pop(i)
                                c += 1
                                i = 0
                            else:
                                if a <= 999:
                                    i += 1
                                    a += 1
                                else:
                                    break
                        break
                    except:
                        if len(list_x) == 9:
                            break
                        else:
                            pass
            list7 = list_x
            if msg_display == 'ON':
                print('生成的list7:', list7)

            # 生成子list8
            list_x = []  # 初始化list_x
            while True:
                if len(list_x) == 9:
                    break
                else:
                    list_x = []
                    list_tmp = random_num_9()  # 创建一个临时列表
                    i = 0  # 临时列表的下标
                    c = 0  # 当前位数判断
                    a = 0  # 统计循环次数
                    try:
                        while True:
                            # print('*list8*当前临时列表',list_tmp)
                            if len(list_tmp) == 0:
                                break
                            elif list_tmp[i] not in (
                            list1[c], list2[c], list3[c], list4[c], list5[c], list6[c], list7[0], list7[1],
                            list7[2]) and c <= 2:
                                list_x.append(list_tmp[i])
                                list_tmp.pop(i)
                                c += 1
                                i = 0
                            elif list_tmp[i] not in (
                            list1[c], list2[c], list3[c], list4[c], list5[c], list6[c], list7[3], list7[4],
                            list7[5]) and 3 <= c <= 5:
                                list_x.append(list_tmp[i])
                                list_tmp.pop(i)
                                c += 1
                                i = 0
                            elif list_tmp[i] not in (
                            list1[c], list2[c], list3[c], list4[c], list5[c], list6[c], list7[6], list7[7],
                            list7[8]) and 6 <= c <= 8:
                                list_x.append(list_tmp[i])
                                list_tmp.pop(i)
                                c += 1
                                i = 0
                            else:
                                if a <= 999:
                                    i += 1
                                    a += 1
                                else:
                                    break
                        break
                    except:
                        if len(list_x) == 9:
                            break
                        else:
                            pass
            list8 = list_x
            if msg_display == 'ON':
                print('生成的list8:', list8)

            # 生成子list9
            list_x = []  # 初始化list_x
            while True:
                if len(list_x) == 9:
                    break
                else:
                    list_x = []
                    list_tmp = random_num_9()  # 创建一个临时列表
                    i = 0  # 临时列表的下标
                    c = 0  # 当前位数判断
                    a = 0  # 统计循环次数
                    try:
                        while True:
                            # print('*list9*当前临时列表',list_tmp)
                            if len(list_tmp) == 0:
                                break
                            elif list_tmp[i] not in (
                            list1[c], list2[c], list3[c], list4[c], list5[c], list6[c], list7[c], list8[c], list7[0],
                            list7[1], list7[2], list8[0], list8[1], list8[2]) and c <= 2:
                                # print('当前数据', list_tmp[i],'追加成功')
                                list_x.append(list_tmp[i])
                                list_tmp.pop(i)
                                # print('当前list_x',list_x)
                                c += 1
                                i = 0
                            elif list_tmp[i] not in (
                            list1[c], list2[c], list3[c], list4[c], list5[c], list6[c], list7[c], list8[c], list7[3],
                            list7[4], list7[5], list8[3], list8[4], list8[5]) and 3 <= c <= 5:
                                list_x.append(list_tmp[i])
                                list_tmp.pop(i)
                                c += 1
                                i = 0
                            elif list_tmp[i] not in (
                            list1[c], list2[c], list3[c], list4[c], list5[c], list6[c], list7[c], list8[c], list7[6],
                            list7[7], list7[8], list8[6], list8[7], list8[8]) and 6 <= c <= 8:
                                list_x.append(list_tmp[i])
                                list_tmp.pop(i)
                                c += 1
                                i = 0
                            else:
                                if a <= 999:
                                    i += 1
                                    a += 1
                                else:
                                    break
                        break
                    except:
                        if len(list_x) == 9:
                            break
                        else:
                            pass
            list9 = list_x
            if msg_display == 'ON':
                print('生成的list9:', list9)
        # print('生成的list9:',list9)
        # print('生成的list8:',list8)
        # print('生成的list7:',list7)
        # print('生成的list6:',list6)
        # print('生成的list5:',list5)
        # print('生成的list4:',list4)
        # print('生成的list3:',list3)
        # print('生成的list2:',list2)
        # print('生成的list1:',list1)
        list_complete = []
        list_complete.append(list1)
        list_complete.append(list2)
        list_complete.append(list3)
        list_complete.append(list4)
        list_complete.append(list5)
        list_complete.append(list6)
        list_complete.append(list7)
        list_complete.append(list8)
        list_complete.append(list9)
        #print(list_complete)
        #print('计算结束', list_complete)
        return list_complete
        break

print('测试开始')
con = 0
for i in range(100):
    con +=1
    list_test = []  #初始化
    list_test = list9X9()
    print('当前为第',con,'次取得结果')
    print(list_test)