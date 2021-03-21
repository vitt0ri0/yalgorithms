def debug_func():
    for i in range(2, 40):
        # print(i)
        print(i, ': ')
        factorization(i)
        print()
        # print(i, ': ', ' '.join(map(str, factorization(i))))



import math

def factorization(n: int):

    res = []

    while n % 2 == 0:
        res.append(2)
        n = n // 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            res.append(i)
            n = n // i

    if n > 2:
        res.append(n)
    return res


if __name__ == '__main__':
    n = 37
    print(' '.join(map(str, factorization(n))))

    # debug_func()



