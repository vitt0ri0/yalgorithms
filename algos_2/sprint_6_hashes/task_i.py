def pol_hash(a, m, s):
    if len(s) == 0:
        return 0

    if len(s) == 1:
        return ord(s)

    sm = ord(s[0]) * a + ord(s[1])

    for i in range(2, len(s)):
        sm = sm * a + ord(s[i])
        if i % 1000 == 0:
            print(i)

    return sm % m


if __name__ == "__main__":
    with open("input.txt") as f:
        a = int(f.readline().strip())
        m = int(f.readline().strip())
        s = f.readline().strip()

    print(pol_hash(a, m, s))