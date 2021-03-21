
def factorization(n: int):
    # max = n // 2 + 1
    res = []
    if n < 2:
        return res
    while (n % 2 == 0):
        n = n // 2
        res.append(2)
        if n == 1:
            break

    for i in range(3, n + 1, 2):
        while (n % i == 0):
            n = n // i
            res.append(i)
            if n == 1:
                break
    return res

if __name__ == '__main__':
    n = int(input())
    print(' '.join(map(str, factorization(n))))


def debug_func():
    for i in range(2, 40):
        # print(i)
        print(i, ': ', ' '.join(map(str, factorization(i))))
