def task_g(st):
    d = set()
    arr = set()
    if len(st) < 11:
        return arr
    for i in range(len(st)-9):
        el = st[i:i+10]
        if el in d:
            arr.add(el)
        else:
            d.add(el)
    return arr


if __name__ == '__main__':
    # st = input()
    st = 'GGGGGGGGGGG'
    res = task_g(st)
    if res:
        res = list(res)
        res.sort()
        for el in res:
            print(el)