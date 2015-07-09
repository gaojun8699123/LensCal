#!/usr/bin/python
import wx
class testEvent(wx.PyCommandEvent): #1 �����¼� 
    def __init__(self,evtType,id):
        wx.PyCommandEvent.__init__(self,evtType,id)
        self.eventArgs=""
        
    def GetEventArgs(self):
        return self.eventArgs
    
    def SetEventArgs(self,args):
        self.eventArgs=args
        
myEVT_MY_TEST=wx.NewEventType()     #2 ����һ���¼����� 
EVT_MY_TEST=wx.PyEventBinder(myEVT_MY_TEST,1)       #3 ����һ����������   

class WindowsFrame(wx.Frame): 
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'Camera and Lens',)
        Framepanel=wx.Panel(self)
        ParaBox=wx.BoxSizer()
        self.button1=wx.Button(Framepanel,label='first',size=(120, 50))
        ParaBox.Add(self.button1,proportion=1,flag=wx.LEFT,border=5)
        self.Bind(wx.EVT_BUTTON,self.OnButtonClick,self.button1)
        self.Bind(EVT_MY_TEST,self.OnHandle)    # 4���¼�������
        

        vbox=wx.BoxSizer(wx.HORIZONTAL)
        
        infoText=wx.TextCtrl(Framepanel,style=wx.TE_MULTILINE|wx.HSCROLL|wx.TE_WORDWRAP)
        
        vbox.Add(ParaBox)
        
        vbox.Add(infoText,proportion=1,flag=wx.EXPAND)
        Framepanel.SetSizer(vbox)
    
    def OnButtonClick(self,event):
        self.OnDoTest()
        
    def OnHandle(self,event):#8 �¼�������
        dlg = wx.MessageDialog(self, event.GetEventArgs(),'A Message Box',wx.OK | wx.ICON_INFORMATION)  
        dlg.ShowModal()    
        dlg.Destroy()  
          
    def OnDoTest(self):  
        evt = testEvent(myEVT_MY_TEST, self.button1.GetId()) #5 �����Զ����¼�����     
        evt.SetEventArgs("test event")   # 6������ݵ��¼�   
        self.GetEventHandler().ProcessEvent(evt)  #7 �����¼�        
if __name__=='__main__':
    app=wx.App()
    wf=WindowsFrame()
    wf.Show()
    app.MainLoop()