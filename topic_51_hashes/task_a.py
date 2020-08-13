# счастливый билет

def task_a(num):
    check = set()
    its = 0
    num = str(num)
    while True:
        s = sum(int(x)**2 for x in num)
        its += 1
        if s == 1:
            return True, its
        if s in check:
            return False, its
        else:
            check.add(s)
        num = str(s)

def test(a, b):
    mmax = -1
    for i in range(a, b):
        _, its = task_a(i)
        if its > mmax:
            mmax = its
    return mmax