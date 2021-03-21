def task_e(arr):
    if len(arr) < 2:
        return 0
    prev1 = arr[0]
    prev2 = None
    counter = 0
    i = 1
    mmax = 0
    while i < len(arr):
        el = arr[i]
        el2 = arr[i-1]
        if counter:
            a = (el, el2) == (prev2, prev1)
            b = (el, el2) == (prev1, prev2)
            if a or b:
                counter += 1
                prev2 = el
                prev1 = el2
                i += 1
            else:
                counter = 0
                prev1 = el
        elif el != prev1:
            counter = 1
            prev2 = prev1
            prev1 = el
            i += 1
        else:
            prev1 = el

        if counter > mmax:
            mmax = counter
        i += 1
    return mmax


if __name__ == '__main__':
    arr = [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0]
    n = input()
    arr = list(map(int, input().split()))
    res = task_e(arr)
    print(res)
