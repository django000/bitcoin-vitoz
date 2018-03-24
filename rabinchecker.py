import random


def miller_rabin_checker(n):
    if n <= 1:
        return False
    if n in (2, 3, 5):
        return True
    if str(n)[-1:] in ('0', '2', '4', '5', '6', '8') or eval('+'.join(str(n))) % 3 == 0:
        return False

    def to_binary(n):
        r = []
        while n > 0:
            r.append(n % 2)
            n = n / 2
        return r


def test(a, n):
    b = to_binary(n - 1)
    d = 1
    for i in range(len(b) - 1, -1, -1):
        print(i)
        x = d
        d = (d * d) % n
        if d == 1 and x != 1 and x != n - 1:
            return True
        if b[i] == 1:
            d = (d * a) % n
        if d != 1:
            return True
        return False

    def checker(n, s=50):
        for j in range(1, s + 1):
            a = random.randint(1, n - 1)
            if test(a, n):
                return False
        return True

    return checker(n)
