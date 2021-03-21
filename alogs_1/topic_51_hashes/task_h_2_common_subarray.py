def task(a1, a2):
    dp = [0] * (len(a2) + 1)
    res = 0

    for i in reversed(range(len(a1))):
        for j in range(len(a2)):

            if a1[i] == a2[j]:
                dp[j] = dp[j+1] + 1
            else:
                dp[j] = 0

            res = max(dp[j], res)

    return res


if __name__ == '__main__':
    a1 = '1 2 3 2 1'
    a11 = '1 2 3 4 5 9 0'
    a1 = list(map(int, a11.split()))

    a2 = '3 2 1 5 6'
    a22 = '0 4 5 9 1'
    a2 = list(map(int, a22.split()))

    res = task(a1, a2)

    print(res)
