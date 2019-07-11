#生成子list2
while True:
    try:
        list_x = []
        list_tmp =random_num_9()   #创建一个临时列表
        print('为list_x获取的临时列表为:',list_tmp)
        i = 0
        c = 0       #当前位数判断
        while True:
            #print('当前为第',i,'次循环','判断位置:',c,',判断值为',list_tmp[i])
            print('---------------------------')
            if len(list_tmp) == 0:
                print('列表为空，退出循环')
                break
            elif list_tmp[i] not in list1[0:3] and c<=2:
                print('当前数据为：',list_tmp[i],'插入list_x,并删除临时列表中对应数据')
                list_x.append(list_tmp[i])
                list_tmp.pop(i)
                print('当前list_x内容为：', list_x)
                print('当前list_tmp内容为：', list_tmp)
                c += 1
                i = 0
            elif list_tmp[i] not in list1[3:6] and 3 <= c <= 5:
                print('当前数据为：', list_tmp[i], '插入list_x,并删除临时列表中对应数据')
                list_x.append(list_tmp[i])
                list_tmp.pop(i)
                print('当前list_x内容为：', list_x)
                print('当前list_tmp内容为：', list_tmp)
                c += 1
                i = 0
            elif list_tmp[i] not in list1[6:-1] and 6 <= c <= 8:
                print('当前数据为：', list_tmp[i], '插入list_x,并删除临时列表中对应数据')
                list_x.append(list_tmp[i])
                list_tmp.pop(i)
                print('当前list_x内容为：', list_x)
                print('当前list_tmp内容为：', list_tmp)
                c += 1
                i = 0
            else:
                print('***', list_tmp[i], '*** 不能插入当前位置，i+=1')
                i +=1
        break
    except:
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        pass
list2 = list_x
print('生成的list2:',list2)