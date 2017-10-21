import wx
def hello(event):
    print "hello world!"
    
app = wx.App()
win = wx.Frame(None, title="hello simple", size=(400, 300))
button = wx.Button(win, label="hello")
button.Bind(wx.EVT_BUTTON, hello)
win.Show()
app.MainLoop()
