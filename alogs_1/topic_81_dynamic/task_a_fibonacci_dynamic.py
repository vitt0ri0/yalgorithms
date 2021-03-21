#
def fibonacci(n):
    a = 1
    b = 1
    mod = 10**9 + 7

    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n + 1):
            c = a + b
            c %= mod
            a = b
            b = c
        return b


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())
    # n = 10**6

    print(fibonacci(n))
