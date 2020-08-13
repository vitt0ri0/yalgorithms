from collections import OrderedDict
def find(s):
    d = OrderedDict()

    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1

    for k, v in d.items():
        if v == 1:
            return k
    return None


if __name__ == '__main__':
    s = 'buubbllee'
    # s = input()

    res = find(s)

    if res:
        print('YES')
        print(res)
    else:
        print('NO')

