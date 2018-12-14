# -*- coding: utf-8 -*-
import wx
import time
import binascii
import base_wx
from file2key import main
from ecdsa import SigningKey, NIST256p


class MainFrame(base_wx.BaseFrame):
    """docstring for MainFrame"""

    def __init__(self, parent):
        base_wx.BaseFrame.__init__(self, parent)

    def exchangeSignature(self, event):
        skA = SigningKey.generate(curve=NIST256p)
        skB = SigningKey.generate(curve=NIST256p)
        # vk = sk.get_verifying_key()
        skAM = self.m_textCtrl13.GetValue()
        skBM = self.m_textCtrl23.GetValue()
        sigAM = str(binascii.hexlify(skA.sign(skAM.encode("utf-8"))), "utf-8")
        sigBM = str(binascii.hexlify(skB.sign(skBM.encode("utf-8"))), "utf-8")

        print("The signature of A: %s" % sigAM)
        print("The signature of B: %s" % sigBM)
        self.m_textCtrl31.SetValue(sigAM)
        self.m_textCtrl32.SetValue(sigBM)
        result = False
        while not result:
            with open("mining/mine_result.txt", "r") as f:
                result = f.readline().strip() == "success"
            time.sleep(2)

        with open("mining/mine_result.txt", "w") as f:
            f.write("")

        print("A receive B's signature: %s" % sigBM)
        print("B receive A's signature: %s" % sigAM)
        self.m_textCtrl33.SetValue(sigBM)
        self.m_textCtrl34.SetValue(sigAM)

    def generateKeypairOne(self, event):
        con = self.m_textCtrl11.GetValue()
        if con == "":
            sk = "null"
            pk = "null"
        else:
            h, sk, pk = main("str", con, 2048)
        self.m_textCtrl12.SetValue(sk)
        self.m_textCtrl13.SetValue(pk)
        event.Skip()

    def generateKeypairTwo(self, event):
        con = self.m_textCtrl21.GetValue()
        if con == "":
            sk = "null"
            pk = "null"
        else:
            h, sk, pk = main("str", con, 2048)
        self.m_textCtrl22.SetValue(sk)
        self.m_textCtrl23.SetValue(pk)
        event.Skip()


if __name__ == '__main__':
    app = wx.App()
    mainFrame = MainFrame(None)
    mainFrame.Show(True)
    app.MainLoop()
