import math


def find_divisors(n):

    a = list()
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            if not (n / i == i):
                a.append(int(n/i))
            a.append(i)
        i += 1

    a.sort()

    return a

