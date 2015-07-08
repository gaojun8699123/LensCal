###!/usr/bin/python
import wx

class WindowsFrame(wx.Frame): 
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'Camera and Lens',)
        Framepanel=wx.Panel(self)
        ParaBox=wx.BoxSizer()
        button1=wx.Button(Framepanel,label='first',size=(120, 50))
        ParaBox.Add(button1,proportion=1,flag=wx.LEFT,border=5)
        vbox=wx.BoxSizer(wx.HORIZONTAL)
        
        infoText=wx.TextCtrl(Framepanel,style=wx.TE_MULTILINE|wx.HSCROLL|wx.TE_WORDWRAP)
        
        vbox.Add(ParaBox)
        
        vbox.Add(infoText,proportion=1,flag=wx.EXPAND)
        Framepanel.SetSizer(vbox)
if __name__=='__main__':
    app=wx.App()
    wf=WindowsFrame()
    wf.Show()
    app.MainLoop()