# !/usr/bin/env python

from config import *
from common import *


class Transaction(object):
    """Transaction module"""

    def __init__(self):
        super(Transaction, self).__init__()
        # self.str2byte = lambda instr: bytearray([int(instr[2*i:2*i+2], 16) for i in range(len(instr)//2)])

    def creat_tx(self, data, mode="json", envir="testnet"):
        self.envir = envir
        if mode == "json":
            self.json_tx = data
            self.raw_tx = json2raw(self.json_tx)
        elif mode == "hex":
            self.raw_tx = data
            self.json_tx = raw2json(self.raw_tx)
        else:
            raise ValueError("The Transaction can't be initialized with mode '%s'. " % self.mode)
        self.txid = big2little(hash256(self.raw_tx))

    def update_tx(self, key, value):
        if key == "json_tx":
            if isinstance(value, dict):
                self.json_tx = value
                self.raw_tx = json2raw(self.json_tx)
            else:
                raise TypeError("Unknown type of the value found.")
        elif key in self.json_tx.keys():
            self.json_tx[key] = value
            self.raw_tx = json2raw(self.json_tx)
        elif key == "raw_tx":
            self.raw_tx = value
            self.json_tx = raw2json(self.raw_tx)
        else:
            raise AttributeError("Unknown parameter found: '%s'." % key)
        self.txid = big2little(hash256(self.raw_tx))

    def read_tx(self, key):
        if key == "json_tx":
            return self.json_tx
        elif key == "raw_tx":
            return self.raw_tx
        elif key in self.json_tx.keys():
            return self.json_tx[key]
        else:
            raise AttributeError("Unknown parameter found: '%s'." % key)

    def delete_tx(self):
        self.json_tx = self.raw_tx = self.txid = ""


if __name__ == '__main__':
    testjson = {
        "version": 2,
        "locktime": 0,
        "vin": [
            {
                "txid": "f1e4f2dc7cdaae0d7968f63be5a1946d5937d0005132d5acae6a03df0767b0b6",
                "vout": 0,
                "type": "pubkeyhash",
                "scriptSig": {"asm": "", "hex": ""},
                "sequence": 4294967295,
            },
        ],
        "vout": [
            {
                "value": 1.10000000,
                "n": 0,
                "scriptPubKey": {"asm": "", "hex": "a914f50c7f0e3d3d1a11e7caece8961299a755413d1087"},
                "scriptRedem": "5121023748130bb04b235410c792899091f30416012fa70e51bf0e6501fccc17babd8b51ae",
                "type": "scripthash",
                "address": "2NFavWYMF2SYqzCLghkRLP9ETPSfQQDvq9B",
            }
        ]
    }
    test = Transaction()
    test.creat_tx(testjson)
    testraw = "0200000001b6b06707df036aaeacd5325100d037596d94a1e53bf668790daeda7cdcf2e4f10000000000ffffffff0180778e060000000017a914f50c7f0e3d3d1a11e7caece8961299a755413d108700000000"
    testsign = "0200000001b6b06707df036aaeacd5325100d037596d94a1e53bf668790daeda7cdcf2e4f1000000006a47304402207fc675aa7104879545dc416935ffe4fa1d098ab2b2c55e2e39e88e8725e54ab002201b0c8bf5c2880ce3ad31b4517cdce117357e8aa2518aa130591f68c02f3b80e9012102a0060ddf0c26be657eddf2b23146a869b9f3591e3853f41f3fa431f0082fc811ffffffff0180778e060000000017a914f50c7f0e3d3d1a11e7caece8961299a755413d108700000000"
    if test.raw_tx == testraw:
        signed_tx = sign_tx(test.raw_tx, 0, "cVWmtro3acH4rSQVFAPXjo9SNAWKqd9cyJPgcKHdvftzmQ6NEnzK", "0x6f", 1)
        if signed_tx == testsign:
            print("The class works well.")
        else:
            print(testsign)
            print(signed_tx)
    else:
        print(testraw)
        print(test.raw_tx)
