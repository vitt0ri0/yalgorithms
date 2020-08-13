def solve(length, arr, k):
    # length = int(input())
    # arr = list(map(int, input().split()))
    # k = int(input())

    arr.sort()

    l = 0
    r = arr[-1]

    while l < r:
        cnt = 0
        m = l + (r - l) // 2

        j = 0
        for i in range(length):
            while j < length and arr[j] <= arr[i] + m:
                j += 1
            cnt += j - i - 1

        if cnt < k:
            l = m + 1
        else:
            r = m

    return l

if __name__ == '__main__':
    length = 10
    arr = [60, 88, 82, 78, 86, 38, 5, 76, 38, 90]
    k = 36

    #
    # length = int(input())
    # arr = list(map(int, input().split()))
    # k = int(input())

    res = solve(length, arr, k)
    print(res)