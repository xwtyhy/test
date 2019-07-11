def inputtext(time_H):
    # 根据当前时间编辑发送内容
    '''
    时间逻辑：09、13、20点的进食询问，21点的吃药询问
    非以上时间段:text='exit'
    （持续更新）
    '''
    if time_H == '09':
        text = '吃早饭了么'
    elif time_H =='13' :
        text = '吃午饭了么'
    elif time_H =='18' :
        text = '下班了么'
    elif time_H == '20':
        text = '吃晚饭了么'
    elif time_H == '21':
        text = '吃药了么'
    else:
        text = 'exit'
    return text