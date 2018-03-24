# !/usr/bin/env python

import re
import os
import sys
import copy
import hashlib
import binascii
import random
from config import *
from bitcoin import ecdsa_raw_sign
from bitcoin import encode, decode
from bitcoin import privkey_to_pubkey
import matplotlib.pyplot as plt
import numpy as np


def gene_file(sizes):
    for i in sizes:
        with open("statics/%sKB" % i, "wb") as f:
            f.write(os.urandom(1024 * i))


def bar_plot(xlist, ylist, width=0.46, color="dodgerblue"):
    lens = len(xlist)
    fig, ax = plt.subplots()
    ind = np.arange(lens)
    res = ax.bar(ind, ylist, width, color=color, alpha=1)
    ax.set_xticklabels(xlist)
    ax.set_xticks(ind)
    ax.set_ylim([0, 180])
    ax.set_title("Time of the key pair generation")
    ax.set_ylabel("Time in milliseconds (ms)")
    ax.set_xlabel("Modulus size of $N$ (bits)")
    for i in res:
        h = i.get_height()
        ax.text(i.get_x() + width / 2, 1.03 * h, "%s" % h, ha='center', va='bottom')
    plt.show()


def line_plot(xlist=[1024, 1536, 2048, 2560, 3072]):
    ls = ["-", "--", "-.", ":"]
    marker = ["o", "v", "^", "D", "x", "+"]
    fig, ax = plt.subplots()
    ind = np.arange(len(ylist))
    ax.set_ylim([50, 225])
    for i in xlist:
        ax.plot(ind, results[i], marker=random.choice(marker), ls=random.choice(ls), label="%s bits" % i)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels)
    ax.set_xticks(ind)
    ax.set_xticklabels(ylist)
    ax.set_xlabel("File size of $m$ (KB)")
    ax.set_ylabel("Time in milliseconds (ms)")
    ax.set_title("Time of the key pair generation")
    plt.show()


def linem_plot():
    res = []
    ls = ["-", "--", "-.", ":"]
    marker = ["o", "v", "^", "D", "x", "+"]
    fig, ax = plt.subplots()
    ind = np.arange(len(xlist))
    ax.set_ylim([0, 1000])
    res.append(ax.plot(ind, results["1KB"], marker="^", ls="-.", label="Laptop"))
    res.append(ax.plot(ind, results["1KBM"], marker="v", ls="--", label="Mobile phone"))
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels)
    ax.set_xticks(ind)
    ax.set_xticklabels(xlist)
    ax.set_xlabel("Modulus size of $N$ (bits)")
    ax.set_ylabel("Time in milliseconds (ms)")
    ax.set_title("Time of the key pair generation")
    for k in ["1KB", "1KBM"]:
        for a, b in zip(ind, results[k]):
            ax.text(a, b + 10, str(b), ha='center', va='bottom')
    plt.show()


def sign_tx(raw_tx, index, privkey, version_byte, hashcode, redem=""):
    if (py_version == 3 and isinstance(re, bytes)) or not re.match('^[0-9a-fA-F]*$', raw_tx):
        raw_tx = safe_hexlify(raw_tx)
        return binascii.unhexlify(sign_tx(raw_tx, index, privkey, hashcode))

    if version_byte in version_dict["pubkeyhash"].values():
        pubkey = privkey_to_pubkey(privkey)
        signing_tx = sign_form(raw_tx, index, mk_pkscript(version_byte, hash160(pubkey)), hashcode)
    elif version_byte in version_dict["scripthash"].values():
        assert redem != "", "Empty string found in parameter redem ."
        signing_tx = sign_form(raw_tx, index, redem, hashcode)
    else:
        raise ValueError("Unknown version_byte: '%s' ." % version_byte)

    rawsig = ecdsa_raw_sign(bytes.fromhex(txhash(signing_tx, hashcode)), privkey)
    sig = der_encode_sig(*rawsig) + dec2byte(hashcode, 1, mode="big-endian")
    json_tx = raw2json(raw_tx)

    if version_byte in version_dict["pubkeyhash"].values():
        json_tx["vin"][index]["scriptSig"]["hex"] = call_len(len(sig)) + sig + call_len(len(pubkey)) + pubkey
    elif version_byte in version_dict["scripthash"].values():
        json_tx["vin"][index]["scriptSig"]["hex"] = deal_sig(
            json_tx["vin"][index]["scriptSig"]["hex"], sig, redem, privkey)
    else:
        raise ValueError("Unknown version_byte: '%s' ." % version_byte)
    return json2raw(json_tx)


def deal_sig(befsig, newsig, redem, privkey):
    if not befsig:
        return op_dict["OP_0"][2:] + call_len(len(newsig)) + newsig + call_len(len(redem)) + redem
    else:
        assert befsig[:2] == op_dict["OP_0"][2:]
        partsig = decode_re_sig(befsig[2:])
        assert partsig[-1] == redem
        partpk = decode_re_sig(redem[2:-4])
        index = partpk.index(privkey_to_pubkey(privkey))
        partsig.insert(index, newsig)
        res = op_dict["OP_0"][2:]
        for _, item in enumerate(partsig):
            res += call_len(len(item)) + item
        return res


def decode_re_sig(instr):
    part = []
    pos = 0
    lens = len(instr)
    while pos < lens:
        inlen, inb = read_var_len(instr[pos:pos + 10])
        pos += inb
        part.append(instr[pos:pos + inlen])
        pos += inlen
    return part


def sign_form(raw_tx, index, pkscript, hashcode):
    if isinstance(raw_tx, (str, bytes)):
        return json2raw(sign_form(raw2json(raw_tx), index, pkscript, hashcode))
    nraw_tx = copy.deepcopy(raw_tx)
    for _, perin in enumerate(nraw_tx["vin"]):
        perin["scriptSig"]["hex"] = ""
    nraw_tx["vin"][index]["scriptSig"]["hex"] = pkscript
    if hashcode == SIGHASH_NONE:
        nraw_tx["vout"] = []
    elif hashcode == SIGHASH_SINGLE:
        nraw_tx["vout"] = nraw_tx["vout"][index:index + 1]
    elif hashcode == SIGHASH_ANYONECANPAY:
        nraw_tx["vin"] = nraw_tx["vin"][index:index + 1]
    else:
        pass
    return nraw_tx


def der_encode_sig(v, r, s):
    b1, b2 = safe_hexlify(encode(r, 256)), safe_hexlify(encode(s, 256))
    if len(b1) and b1[0] in '89abcdef':
        b1 = '00' + b1
    if len(b2) and b2[0] in '89abcdef':
        b2 = '00' + b2
    left = '02' + encode(len(b1) // 2, 16, 2) + b1
    right = '02' + encode(len(b2) // 2, 16, 2) + b2
    return '30' + encode(len(left + right) // 2, 16, 2) + left + right


def txhash(raw_tx, hashcode):
    if isinstance(raw_tx, str) and re.match("^[0-9a-fA-F]+$", raw_tx):
        if hashcode:
            return hash256(raw_tx + dec2byte(hashcode, 4))
        else:
            return big2little(hash256(raw_tx))
    else:
        raise TypeError("Invalid raw_tx found. ")


def mk_redem(m, *args):
    n = len(args)
    assert m <= n
    res = op_dict["OP_%s" % m][2:]
    for _, pubkey in enumerate(args):
        res += call_len(len(pubkey)) + pubkey
    res += op_dict["OP_%s" % n][2:] + op_dict["OP_CHECKMULTISIG"][2:]
    return res


def mk_pkscript(version_byte, pk_hash160):
    res = "{0}14{1}".format(op_dict["OP_HASH160"][2:], pk_hash160)
    if version_byte in version_dict["scripthash"].values():
        return "{0}{1}".format(res, op_dict["OP_EQUAL"][2:])
    elif version_byte in version_dict["pubkeyhash"].values():
        return "{0}{1}{2}{3}".format(op_dict["OP_DUP"][2:], res, op_dict["OP_EQUALVERIFY"][2:], op_dict["OP_CHECKSIG"][2:])
    else:
        raise ValueError("Unknown version_byte: '%s' ." % version_byte)


def json2raw(json_tx):
    raw_tx = dec2byte(json_tx["version"], 4)
    raw_tx += dec2var_byte(len(json_tx["vin"]))
    for i, perin in enumerate(json_tx["vin"]):
        raw_tx += big2little(perin["txid"])
        raw_tx += dec2byte(perin["vout"], 4)

        raw_tx += dec2var_byte(len(perin["scriptSig"]["hex"]) // 2)
        raw_tx += perin["scriptSig"]["hex"]
        raw_tx += dec2byte(perin["sequence"], 4)

    raw_tx += dec2var_byte(len(json_tx["vout"]))
    for j, perout in enumerate(json_tx["vout"]):
        value = int(perout["value"] * (10**8)) if isinstance(perout["value"], float) else perout["value"]
        raw_tx += dec2byte(value, 8)
        raw_tx += dec2var_byte(len(perout["scriptPubKey"]["hex"]) // 2)
        raw_tx += perout["scriptPubKey"]["hex"]

    raw_tx += dec2byte(json_tx["locktime"], 4)
    return raw_tx


def raw2json(raw_tx):
    json_tx = {
        "version": byte2dec(raw_tx[:8]),
        "locktime": byte2dec(raw_tx[-8:]),
        "vin": [],
        "vout": []
    }
    ins, inb = read_var_string(raw_tx[8:26])
    nraw_tx = raw_tx[8 + inb:-8]
    for i in range(ins):
        perin = {
            "txid": big2little(nraw_tx[:64]),
            "vout": byte2dec(nraw_tx[64:72])
        }
        siglen, inb = read_var_string(nraw_tx[72:90])
        sigp = 72 + inb + siglen * 2
        perin["scriptSig"] = {"asm": "", "hex": nraw_tx[72 + inb:sigp]}
        perin["sequence"] = byte2dec(nraw_tx[sigp:8 + sigp])
        json_tx["vin"].append(perin)
        nraw_tx = nraw_tx[8 + sigp:]

    outs, inb = read_var_string(nraw_tx[:16])
    nraw_tx = nraw_tx[inb:]
    for j in range(outs):
        perout = {
            "n": j,
            "value": byte2dec(nraw_tx[:16]) / (10**8)
        }
        scrlen, inb = read_var_string(nraw_tx[16:34])
        scrp = 16 + inb + scrlen * 2
        perout["scriptPubKey"] = {"asm": "", "hex": nraw_tx[16 + inb:scrp]}
        perout["type"] = "pubkeyhash" if scrlen == 25 else "scripthash"
        json_tx["vout"].append(perout)
        nraw_tx = nraw_tx[scrp:]
    return json_tx


def change_base(instr, bef, aft, minlen=0):
    if bef == aft:
        try:
            return code_strings[bef][0] * (minlen - len(instr)) + instr if minlen > len(instr) else instr
        except Exception as e:
            raise e
    else:
        return encode(decode(instr, bef), aft, minlen)


def safe_hexlify(byte):
    return str(binascii.hexlify(byte), "utf-8")


def hash160(instr):
    return bin_ripemd160(bin_sha256(instr))


def hash256(instr):
    return bin_sha256(bin_sha256(instr))


def bin_ripemd160(instr):
    res = hashlib.new("ripemd160")
    res.update(bytearray.fromhex(instr))
    return res.hexdigest()


def bin_sha256(instr):
    return hashlib.sha256(bytearray.fromhex(instr)).hexdigest()


def dec2byte(num, byte=None, mode="little-endian"):
    if byte is None:
        res = "{:x}".format(num)
        res = "0" + res if len(res) % 2 == 1 else res
    else:
        res = ("{:0%sx}" % (2 * byte)).format(num)
    return big2little(res) if mode == "little-endian" else res


def byte2dec(byte, num=None, mode="little-endian"):
    res = big2little(byte) if mode == "little-endian" else byte
    if num is None:
        return int(res, 16)
    else:
        return ("%0" + "%sd" % (2 * num)) % int(res, 16)


def big2little(bigstr):
    return "".join([bigstr[2 * i:2 * i + 2] for i in range(len(bigstr) // 2)][::-1])


def dec2var_byte(num):
    num = int(num)
    if num < 253:
        return dec2byte(num)
    elif num < 65536:
        return dec2byte(253) + dec2byte(num, 2)
    elif num < 4294967296:
        return dec2byte(254) + dec2byte(num, 4)
    else:
        return dec2byte(255) + dec2byte(num, 8)


def read_var_string(instr):
    tmp = int(instr[:2], 16)
    if tmp < 253:
        return tmp, 2
    else:
        inb = pow(2, tmp - 251)
        return byte2dec(instr[2:2 + inb]), inb + 2


def call_len(num):
    num = int(num) // 2
    if num <= 75:
        return dec2byte(num)
    elif num < 256:
        return dec2byte(76) + dec2byte(num)
    elif num < 65536:
        return dec2byte(77) + dec2byte(num, 2)
    else:
        return dec2byte(78) + dec2byte(num, 4)


def read_var_len(instr):
    tmp = int(instr[:2], 16)
    if tmp <= 75:
        return tmp * 2, 2
    else:
        inb = pow(2, tmp - 75)
        return byte2dec(instr[2:2 + inb]) * 2, inb + 2


def dec_to_bytes(num):
    res = bytearray()
    while num > 0:
        res.extend([num % 256])
        num //= 256
    for i in range(32 - len(res)):
        res.extend([0])
    return res[::-1]
