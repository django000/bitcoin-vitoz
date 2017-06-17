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
                "txid": "c68b824392d8f7883a261027c94419776f7fd78e33ec1e01fb057a785713480a",
                "vout": 0,
                "type": "scripthash",
                "scriptSig": {"asm": "", "hex": ""},
                "sequence": 4294967295,
            },
        ],
        "vout": [
            {
                "value": 0.22320000,
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
    testraw = "02000000010a481357787a05fb011eec338ed77f6f771944c92710263a88f7d89243828bc60000000000ffffffff01809354010000000017a914f50c7f0e3d3d1a11e7caece8961299a755413d108700000000"
    testsign = "020000000158e52f0d54b8bd8217e1f2a10f87e68c8a64651f8620cc6dc22d970272b4f4ed000000006b483045022100fbe046f5b0b9ed4019c8c5a583345f91439b5ed057af3b9d92691d3f8706979402200a6f64d5f940ee830855749b85aca2150ea8bc5ec475251e2cc2ea621ff994170121025d37fe014e50a5126e9ddff1cbf1ddf98c06b9f5a5af5cd96028341d8959afa9ffffffff01201a56010000000017a91420c2309cd2fcdbbc6bd704465cdc82185bcfa3508700000000"
    if test.raw_tx == testraw:
        signed_tx = sign_tx(test.raw_tx, 0, "cVWmtro3acH4rSQVFAPXjo9SNAWKqd9cyJPgcKHdvftzmQ6NEnzK",
                            "0xc4", 1, "512102a0060ddf0c26be657eddf2b23146a869b9f3591e3853f41f3fa431f0082fc81151ae")
        if signed_tx == testsign:
            print("The class works well.")
        else:
            print(testsign)
            print(signed_tx)
    else:
        print(testraw)
        print(test.raw_tx)
