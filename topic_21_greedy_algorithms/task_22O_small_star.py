def divide(dividend, divisor):
    if divisor == 1:
        return dividend
    if divisor == -1:
        return -dividend
    neg = True
    if dividend >= 0 and divisor >= 0 or dividend <= 0 and divisor <= 0:
        neg = False
    dividend = abs(dividend)
    divisor = abs(divisor)
    if divisor > dividend:
        return 0
    res = shift = 0

    print(dividend, divisor, shift)
    while dividend >= divisor:

        shift += 1
        print(f'divisor {divisor}')
        divisor = (divisor << 1)
        print(f'divisor {divisor}')

    while shift >= 0:
        print(f'shift: {shift}')
        if dividend >= divisor:

            res += (1 << shift)

            dividend -= divisor

        divisor = (divisor >> 1)
        shift -= 1
        print(f'divisor {divisor}, shift: {shift}')

    return -res if neg else res

if __name__ == '__main__':
    dividend = 40
    divisor = 19

    print(divide(dividend, divisor))