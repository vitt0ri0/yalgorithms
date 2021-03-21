def task(arr, find):
    arr.sort()
    d = dict()

    res = []
    for i in range(len(arr)):
        elem_i = arr[i]
        for j in range(i+1, len(arr)):
            elem_j = arr[j]
            sum = arr[i] + arr[j]
            el = d.get(find - sum, None)

            if el:
                first, second = el
                appendix = [elem_i, arr[j], arr[first], arr[second]]
                appendix.sort()
                res.append(appendix)

        for k in range(i):
            d[elem_i + arr[k]] = (i, k)

    res.sort()
    return res


if __name__ == '__main__':

    find = 10
    arr = [2, 3, 2, 4, 1, 10, 3, 0]

    find2 = 0
    arr2 = [1, 0, -1, 0, 2, -2]

    res = task(arr2, find2)
    print(res)
