def hash_gorner(a: int, m: int, s: str):
    """
    Gorner Method

    21 мар 2021, 15:55:27
    49701543
    A
    Python 3.7.3
    OK
    -
    417ms
    4.16Mb
    -
    """
    if len(s) == 0:
        return 0

    h = ord(s[0])
    # here we do not store P for power of A, but just multiply A directly on resulting hash
    for i in range(1, len(s)):
        h *= a
        h += ord(s[i])
        h %= m
    return h % m


def hash2(a: int, m: int, s: str):
    """
    21 мар 2021, 15:53:33
    49701480
    A
    Python 3.7.3
    TL
    -
    0.595s
    3.95Mb
    7	-
    """
    if len(s) == 0:
        return

    h = 0  # resulting hash
    p = 1  # power of a
    for i in reversed(range(0, len(s))):
        # count resulting hash
        h += ord(s[i]) * p
        # count modulo
        h %= m
        # every iteration we multiply on A to get new power of A
        p *= a
    h %= m

    return h


def input_output():
    # basement
    a = int(input())
    # modulo
    m = int(input())
    # string
    s = input()

    res = hash_gorner(a, m, s)

    print(res)


if __name__ == '__main__':
    input_output()
