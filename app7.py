# -*- coding :utf-8 -*-
#PM脚本做成功能分析一：
import wx
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id, title='PM自动化脚本编辑机能逻辑分析',size=(600,300))
        self.Center()       #新生成的窗口居中显示
        #创建一个分割窗口
        swindow = wx.SplitterWindow(parent=self, id=-1)
        # 创建面板
        panel_list = wx.Panel(parent=swindow) #在当前窗口内的左侧显示功能列表
        panel_dispaly = wx.Panel(parent=swindow) #在当前窗口内的右侧显示脚本编辑界面
        # 设置左右布局的分割窗口panel_list和panel_dispaly
        swindow.SplitVertically(panel_list,panel_dispaly, 200)

        # 创建功能控件按钮，并绑定事件
        self.bt_text = wx.Button(panel_list, label='1通过文本选择元素')
        self.bt_text.Bind(wx.EVT_BUTTON,self.Onclickfortext)
        self.bt_id = wx.Button(panel_list, label='通过id选择元素')
        self.bt_id.Bind(wx.EVT_BUTTON, self.Onclickforid)

        # self.bt_text_conf = wx.StaticText(panel_dispaly, label='1.请从左侧控件列表选择')
        # self.bt_id_conf = wx.StaticText(panel_dispaly, label='2.请从左侧控件列表选择')
        # self.bt_text_conf = wx.Button(panel_dispaly, label='确认文本选择元素')
        # self.bt_id_conf = wx.Button(panel_dispaly, label='确认id选择元素')


        # 创建容器，容器中控件纵向排列
        hsizer_list=wx.BoxSizer(wx.VERTICAL)
        hsizer_list.Add(self.bt_text, proportion=0, flag=wx.LEFT, border=5)
        hsizer_list.Add(self.bt_id, proportion=0, flag=wx.LEFT, border=5)
        #在panel_list面板中加载容器
        panel_list.SetSizer(hsizer_list)

        # 创建容器，容器中控件纵向排列
        hsizer_dispaly = wx.BoxSizer(wx.VERTICAL)
        # hsizer_dispaly.Add(self.bt_text_conf, proportion=0, flag=wx.RIGHT, border=5)
        # hsizer_dispaly.Add(self.bt_id_conf, proportion=0, flag=wx.LEFT, border=5)
        panel_dispaly.SetSizer(hsizer_dispaly)


    def Onclickfortext(self,event):
        '''单击panel_list中的控件，执行方法'''
        swindow = wx.SplitterWindow(parent=self, id=-1)
        panel_list = wx.Panel(parent=swindow)
        panel_dispaly = wx.Panel(parent=swindow)
        swindow.SplitVertically(panel_list, panel_dispaly, 100)
        hsizer_dispaly = wx.BoxSizer(wx.VERTICAL)
        self.bt_text_conf = wx.StaticText(panel_dispaly, label='1.请从左侧控件列表选择')
        hsizer_dispaly.Add(self.bt_text_conf, proportion=0, flag=wx.LEFT, border=5)
        panel_dispaly.SetSizer(hsizer_dispaly)


        # self.bt_text_conf.SetLabelText('Select_For_TEXT')
        # swindow = wx.SplitterWindow(parent=self, id=-1)
        # # 创建面板
        # panel_list = wx.Panel(parent=swindow)
        # panel_dispaly = wx.Panel(parent=swindow)
        # swindow.SplitVertically(panel_list, panel_dispaly, 200)
        # MyFrame.bt_text_conf = wx.Button(MyFrame.panel_dispaly, label='确认文本选择元素')
        # hsizer_dispaly = wx.BoxSizer(wx.VERTICAL)
        # hsizer_dispaly.Add(MyFrame.bt_text_conf, proportion=0, flag=wx.RIGHT, border=5)
        # MyFrame.panel_dispaly.SetSizer(hsizer_dispaly)

    def Onclickforid(self, event):
        '''单击panel_list中的控件，执行方法'''
        message = '追加ｉｄ'
        wx.MessageBox(message)
        # hsizer_dispaly.Add(self.bt_id_conf, proportion=0, flag=wx.LEFT, border=5)
        # panel_dispaly.SetSizer(hsizer_dispaly)


if __name__ == '__main__':
    app =wx.App()
    frame =MyFrame(parent=None,id =-1)
    frame.Show()
    app.MainLoop()