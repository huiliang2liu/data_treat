import wx


class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, id=wx.NewId(), parent=parent, title=title, size=(420, 320))
        self.top = wx.Panel(self, -1, size=(420, 110), pos=(0, 0))
        self.top.SetBackgroundColour('#db7093')
        self.left = wx.Panel(self, -1, size=(205, 204), pos=(0, 116))
        self.left.SetBackgroundColour('#007fff')
        self.right = wx.Panel(self, -1, size=(205, 204), pos=(215, 116))
        self.right.SetBackgroundColour('#00ff7f')


if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame(None, '计算器')
    frame.Show(True)
    app.MainLoop()
