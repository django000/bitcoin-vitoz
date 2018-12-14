# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Oct 26 2018)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# Class BaseFrame
###########################################################################


class BaseFrame (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"签名交换程序Demo", pos=wx.DefaultPosition,
                          size=wx.Size(500, 600), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        gSizerMain = wx.GridSizer(3, 1, 0, 0)

        gSizerOne = wx.GridSizer(4, 1, 0, 0)

        bSizerOne1 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"合同A", wx.DefaultPosition,
                                            wx.Size(60, -1), wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText11.Wrap(-1)

        bSizerOne1.Add(self.m_staticText11, 0, wx.ALIGN_CENTER |
                       wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_textCtrl11 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, -1), 0)
        bSizerOne1.Add(self.m_textCtrl11, 0, wx.ALIGN_CENTER |
                       wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        gSizerOne.Add(bSizerOne1, 1, wx.EXPAND, 5)

        bSizerOne2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY, u"私钥A", wx.DefaultPosition,
                                            wx.Size(60, -1), wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText12.Wrap(-1)

        bSizerOne2.Add(self.m_staticText12, 0, wx.ALIGN_CENTER |
                       wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_textCtrl12 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, -1), 0)
        bSizerOne2.Add(self.m_textCtrl12, 0, wx.ALIGN_CENTER |
                       wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        gSizerOne.Add(bSizerOne2, 1, wx.EXPAND, 5)

        bSizerOne3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText13 = wx.StaticText(self, wx.ID_ANY, u"公钥A", wx.DefaultPosition,
                                            wx.Size(60, -1), wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText13.Wrap(-1)

        bSizerOne3.Add(self.m_staticText13, 0, wx.ALIGN_CENTER |
                       wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_textCtrl13 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, -1), 0)
        bSizerOne3.Add(self.m_textCtrl13, 0, wx.ALIGN_CENTER |
                       wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        gSizerOne.Add(bSizerOne3, 1, wx.EXPAND, 5)

        gSizerOne4 = wx.GridSizer(1, 1, 0, 0)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"生成密钥对", wx.DefaultPosition, wx.Size(100, -1), 0)
        gSizerOne4.Add(self.m_button1, 0, wx.ALIGN_CENTER | wx.ALIGN_CENTER_HORIZONTAL |
                       wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        gSizerOne.Add(gSizerOne4, 1, wx.EXPAND, 5)

        gSizerMain.Add(gSizerOne, 1, wx.EXPAND, 5)

        gSizerTwo = wx.GridSizer(4, 1, 0, 0)

        bSizerTwo1 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText21 = wx.StaticText(self, wx.ID_ANY, u"合同B", wx.DefaultPosition,
                                            wx.Size(60, -1), wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText21.Wrap(-1)

        bSizerTwo1.Add(self.m_staticText21, 0, wx.ALIGN_CENTER |
                       wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_textCtrl21 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, -1), 0)
        bSizerTwo1.Add(self.m_textCtrl21, 0, wx.ALIGN_CENTER |
                       wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        gSizerTwo.Add(bSizerTwo1, 1, wx.EXPAND, 5)

        bSizerTwo2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText22 = wx.StaticText(self, wx.ID_ANY, u"私钥B", wx.DefaultPosition,
                                            wx.Size(60, -1), wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText22.Wrap(-1)

        bSizerTwo2.Add(self.m_staticText22, 0, wx.ALIGN_CENTER |
                       wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_textCtrl22 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, -1), 0)
        bSizerTwo2.Add(self.m_textCtrl22, 0, wx.ALIGN_CENTER |
                       wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        gSizerTwo.Add(bSizerTwo2, 1, wx.EXPAND, 5)

        bSizerTwo3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText23 = wx.StaticText(self, wx.ID_ANY, u"公钥B", wx.DefaultPosition,
                                            wx.Size(60, -1), wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText23.Wrap(-1)

        bSizerTwo3.Add(self.m_staticText23, 0, wx.ALIGN_CENTER |
                       wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_textCtrl23 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, -1), 0)
        bSizerTwo3.Add(self.m_textCtrl23, 0, wx.ALIGN_CENTER |
                       wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        gSizerTwo.Add(bSizerTwo3, 1, wx.EXPAND, 5)

        gSizerTwo4 = wx.GridSizer(1, 1, 0, 0)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"生成密钥对", wx.DefaultPosition, wx.Size(100, -1), 0)
        gSizerTwo4.Add(self.m_button2, 0, wx.ALIGN_CENTER | wx.ALIGN_CENTER_HORIZONTAL |
                       wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        gSizerTwo.Add(gSizerTwo4, 1, wx.EXPAND, 5)

        gSizerMain.Add(gSizerTwo, 1, wx.EXPAND, 5)

        gSizerThree = wx.GridSizer(5, 1, 0, 0)

        bSizerThree1 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText31 = wx.StaticText(self, wx.ID_ANY, u"签名A", wx.DefaultPosition,
                                            wx.Size(60, -1), wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText31.Wrap(-1)

        bSizerThree1.Add(self.m_staticText31, 0, wx.ALIGN_CENTER |
                         wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_textCtrl31 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, -1), 0)
        bSizerThree1.Add(self.m_textCtrl31, 0, wx.ALIGN_CENTER |
                         wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        gSizerThree.Add(bSizerThree1, 1, wx.EXPAND, 5)

        bSizerThree2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText32 = wx.StaticText(self, wx.ID_ANY, u"签名B", wx.DefaultPosition,
                                            wx.Size(60, -1), wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText32.Wrap(-1)

        bSizerThree2.Add(self.m_staticText32, 0, wx.ALIGN_CENTER |
                         wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_textCtrl32 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, -1), 0)
        bSizerThree2.Add(self.m_textCtrl32, 0, wx.ALIGN_CENTER |
                         wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        gSizerThree.Add(bSizerThree2, 1, wx.EXPAND, 5)

        bSizerThree3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText33 = wx.StaticText(self, wx.ID_ANY, u"A收到", wx.DefaultPosition,
                                            wx.Size(60, -1), wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText33.Wrap(-1)

        bSizerThree3.Add(self.m_staticText33, 0, wx.ALIGN_CENTER |
                         wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_textCtrl33 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, -1), 0)
        bSizerThree3.Add(self.m_textCtrl33, 0, wx.ALIGN_CENTER |
                         wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        gSizerThree.Add(bSizerThree3, 1, wx.EXPAND, 5)

        bSizerThree4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText34 = wx.StaticText(self, wx.ID_ANY, u"B收到", wx.DefaultPosition,
                                            wx.Size(60, -1), wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText34.Wrap(-1)

        bSizerThree4.Add(self.m_staticText34, 0, wx.ALIGN_CENTER |
                         wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_textCtrl34 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, -1), 0)
        bSizerThree4.Add(self.m_textCtrl34, 0, wx.ALIGN_CENTER |
                         wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        gSizerThree.Add(bSizerThree4, 1, wx.EXPAND, 5)

        gSizerThree5 = wx.GridSizer(1, 1, 0, 0)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"合约执行", wx.DefaultPosition, wx.Size(100, -1), 0)
        gSizerThree5.Add(self.m_button3, 0, wx.ALIGN_CENTER | wx.ALIGN_CENTER_HORIZONTAL |
                         wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        gSizerThree.Add(gSizerThree5, 1, wx.EXPAND, 5)

        gSizerMain.Add(gSizerThree, 1, wx.EXPAND, 5)

        self.SetSizer(gSizerMain)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button1.Bind(wx.EVT_BUTTON, self.generateKeypairOne)
        self.m_button2.Bind(wx.EVT_BUTTON, self.generateKeypairTwo)
        self.m_button3.Bind(wx.EVT_BUTTON, self.exchangeSignature)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def generateKeypairOne(self, event):
        event.Skip()

    def generateKeypairTwo(self, event):
        event.Skip()

    def exchangeSignature(self, event):
        event.Skip()
