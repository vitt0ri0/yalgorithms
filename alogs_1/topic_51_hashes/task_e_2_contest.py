def task_e(arr):
    presum = dict()

    sum = 0
    maxlen = 0

    for pos in range(len(arr)):
        el = arr[pos]
        sum += el

        if el == 0 and maxlen == 0:
            maxlen = 1
        if sum == 0:
            maxlen = pos+1
        res = presum.get(sum, None)

        if res:
            m = max(maxlen, pos-res)
            maxlen = m
        else:
            presum[sum] = pos

    return maxlen


if __name__ == '__main__':
    arr = [0, 0, 1, 0, 1, 1, 1, 0, 0, 0]
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = -1
    # n = input()
    # arr = list(map(int, arr))
    res = task_e(arr)
    print(res)
