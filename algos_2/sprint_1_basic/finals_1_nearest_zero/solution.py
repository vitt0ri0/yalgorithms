def solution(arr, n):
    res = [-1] * n
    leng = -1
    for i, el in enumerate(arr):
        if el == 0:
            leng = 0

        if leng != -1:
            res[i] = leng
            leng += 1

    for i, el in enumerate(reversed(arr)):
        pos = n - i - 1
        if el == 0:
            leng = 0
        if res[pos] > leng or res[pos] == -1:
            res[pos] = leng
        leng += 1

    return res


def test():
    arr = [int(x) for x in "0 7 9 4 8 20".split()]
    arr.reverse()
    # print("0 7 9 4 8 20".split())
    print(arr)
    n = len(arr)

    print(solution(arr, n))


if __name__ == '__main__':
    import sys
    n = int(input())
    arr = sys.stdin.readline().strip()
    arr = [int(x) for x in arr.split()]

    res = solution(arr, n)
    print(" ".join(str(x) for x in res))











