def solution(s):

    d = dict()
    l = len(s)
    res = []
    if l <= 10:
        return res

    for i in range(l-9):
        substr = s[i:i+10]
        el = d.get(substr, None)
        if el:
            if el > 1:
                continue
            if el == 1:
                res.append(substr)
            d[substr] = el + 1
        else:
            d[substr] = 1

    res.sort()

    return res


if __name__ == '__main__':
    # s = 'GGGGGOOOOOGGGGGOOOOOOGGGGGSSSHAA'
    s = 'GGGGGGGGGGG'

    res = solution(s)

    for el in res:
        print(el)

