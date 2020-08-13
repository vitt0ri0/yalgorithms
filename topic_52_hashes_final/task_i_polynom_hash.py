def hash_str(a: int, m: int, s: str):
    if len(s) == 0:
        return 0

    h = ord(s[0])
    for i in range(1, len(s)):
        h *= a
        h += ord(s[i])
        h %= m
    return h % m

def hash2(a: int, m: int, s: str):
    if len(s) == 0:
        return

    h = 0
    p = 1
    for i in reversed(range(0, len(s))):
        h += ord(s[i]) * p
        h %= m
        p *= a

    return h % m


if __name__ == '__main__':
    a = 123
    m = 100003
    s = 'hash'

    h = hash_str(a, m, s)
    h2 = hash2(a, m, s)
    print(h, h2)
