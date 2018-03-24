import time
import base58
import hashlib
from config import version_dict
from random import randrange
from ecdsa import SigningKey, SECP256k1
from common import bin_sha256, dec_to_bytes, hash256, change_base, safe_hexlify, hash160

q = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141


def is_complex(a, n):
    b = list(bin(n - 1)[2:])
    d = 1
    for i in range(len(b) - 1, -1, -1):
        x = d
        d = (d * d) % n
        if d == 1 and x != 1 and x != n - 1:
            return True
        if int(b[i]) == 1:
            d = (d * a) % n
        if d != 1:
            return True
        return False


def is_prime(n, s=50):
    if n < 2:
        return False
    elif n in (2, 3, 5):
        return True
    elif str(n)[-1:] in ('0', '2', '4', '5', '6', '8') or eval('+'.join(str(n))) % 3 == 0:
        return False
    else:
        for _ in range(s):
            a = randrange(1, n)
            if is_complex(a, n):
                return False
        return True


def get_hash(typ, con, lam):
    m = hashlib.sha256()
    if typ == "file":
        with open(con, 'rb') as f:
            m.update(f.read())
    else:
        m.update(bytearray(con, "ascii"))
    salt = randrange(2 ** (1024 - 1), 2 ** 1024)
    m.update(bytearray.fromhex(("{:0%sx}" % (lam // 4)).format(salt)))
    res = bin_sha256(m.hexdigest())
    return res


def generate_prime(keysize):
    while True:
        num = randrange(2 ** (keysize - 1), 2 ** keysize)
        if is_prime(num):
            break
    return num


def generate_pq(lam):
    while True:
        i = generate_prime(lam)
        j = generate_prime(lam)
        inverse = get_inverse(i, j)
        if (inverse != 0):
            break
    return i, j, inverse


def get_inverse(p, q):
    phiN = (p - 1) * (q - 1)
    k = phiN % 3
    if k == 0:
        return 0
    elif k == 1:
        return phiN - phiN // 3
    else:
        return phiN // 3 + 1


def get_wif(version_byte, sk):
    if version_byte in version_dict["main"].values():
        res = "80%x01" % sk
    else:
        res = "ef%x01" % sk
    res += hash256(res)[:8]
    return change_base(res, 256, 58)


def decode_wif(wifkey):
    res = safe_hexlify(change_base(wifkey, 58, 256))
    assert hash256(res[:-8])[:8] == res[-8:]
    return int(res[2:-10], 16)


def privkey_to_pubkey(sk):
    sk = dec_to_bytes(sk) if isinstance(sk, int) else sk
    sk = SigningKey.from_string(dec_to_bytes(sk), curve=SECP256k1)
    pk = sk.verifying_key.to_string()
    return "04" + "".join(["{:02x}".format(i) for i in pk])


def pubkey_to_compk(pk):
    pk_x = pk[2:66]
    pk_y = pk[66:130]
    if int(pk_y[-1], 16) % 2 == 0:
        return '02' + pk_x
    else:
        return '03' + pk_x


def pubkey_to_address(version_byte, instr):
    res = version_byte[2:] + hash160(instr)
    res += hash256(res)[:8]
    if version_byte == version_dict["main"]["pubkeyhash"]:
        return "1" + change_base(res, 256, 58)
    else:
        return change_base(res, 256, 58)


def check_address(address):
    res = safe_hexlify(change_base(address, 58, 256))
    if address.startswith("1"):
        res = "00" + res
    return True if hash256(res[:-8])[:8] == res[-8:] else False


def main(typ, con, lam):
    h = get_hash(typ, con, lam)
    i, j, inverse = generate_pq(lam // 2)
    N = i * j
    sk = pow(int(h, 16), inverse, N) % q
    pk = privkey_to_pubkey(sk)
    return sk, pk
    # compk = pubkey_to_compk(pk)
    # print("h: {0}\nsk: {1}\npk: {2}".format(h, sk, pk))


def test(ffile, lam):
    res = list()
    for i in lam:
        sum = 0
        for _ in range(100):
            s = time.time()
            main("file", "statics/%s" % ffile, i)
            sum += time.time() - s
        res.append(sum / 100)
    return res


# if __name__ == '__main__':
    # main("file", "statics/1KB", 1024)
    # print(test("1KB", 1536))

    # typ, con, lam = input("Please enter the type, content, and lambda: ").split()
    # main(typ, con, int(lam))

    # def check_addrsk(address, sk, head):
    #     if len(sk) != 52:
    #         return False
    #     addr_comp = pubkey_to_address(privkey_to_compk(k), head)
    #     if address == addr_comp:
    #         return True
    #     else:
    #         return False
