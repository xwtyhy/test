import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="分隔窗口", size=(450, 300))
        self.Center()
        swindow = wx.SplitterWindow(parent=self, id=-1)
        left = wx.Panel(parent=swindow)
        right = wx.Panel(parent=swindow)
        # 设置左右布局的分割窗口left和right
        swindow.SplitVertically(left, right, 100)
        # 设置最小窗格大小，左右布局指左边窗口大小
        swindow.SetMinimumPaneSize(80)
        # # 创建一个ListBox对象
        self.list = ['苹果', '橘子', '香蕉', '梨子', '芒果']
        lb2 = wx.ListBox(left, 1, choices=self.list, style=wx.LB_SINGLE)
        self.Bind(wx.EVT_LISTBOX, self.on_listbox, lb2)
        # 为left面板设置一个布局管理器
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        left.SetSizer(vbox1)
        vbox1.Add(lb2, 1, flag=wx.EXPAND | wx.ALL, border=5)
        # 为right面板设置一个布局管理器
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        right.SetSizer((vbox2))
        self.st = wx.StaticText(right, 2, label='请选择')
        vbox2.Add(self.st, 1, flag=wx.EXPAND | wx.ALL, border=5)

    def on_listbox(self, event):
        self.st.SetLabelText(event.GetString())


class App(wx.App):
    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print("应用程序退出")
        return 0


if __name__ == '__main__':
    app = App()
    app.MainLoop()
