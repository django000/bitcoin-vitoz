# -*- coding: utf-8 -*-
import os
import binascii

with open("mining/mine_result.txt", "w") as f:
    f.write("success\n" + str(binascii.hexlify(os.urandom(1024 * 10)), "utf-8"))
