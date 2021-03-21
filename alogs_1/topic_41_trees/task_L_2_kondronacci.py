# def factorize(n):
#     res = factorize_all(n)
#     return res[-1]
import heapq as q
# Sanal
mult_nums = {
    2: [2, 3, 5],
    3: [3, 5],
    5: [5]
}
l = []

def push(el):
    q.heappush(l, el)


def pop():
    q.heappop(l)


def condronacci_all(n):
    l = []
    elem = (1, 2)
    row = [elem]

    push(elem)


    while len(row) > 0:
        next_row = []
        for elem, mult in row:
            mults = mult_nums[mult]
            for el in mults:
                res = elem * el
                res
                next_row.append((elem * el, el))
        print(next_row)
        row = next_row


    return res


if __name__ == '__main__':
    res = condronacci_all(30)
    print(res)
