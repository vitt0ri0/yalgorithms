def factorize(n):
    res = factorize_all(n)
    return res[-1]


def factorize_all(n):
    res = [1]
    x, y, z = 0, 0, 0
    while len(res) < n:
        a = res[x] * 2
        b = res[y] * 3
        c = res[z] * 5
        num = min(a, b, c)

        if a == num:
            x += 1
        if b == num:
            y += 1
        if c == num:
            z += 1
        res.append(num)

    return res


if __name__ == '__main__':
    res = factorize_all(30)
    print(res)
