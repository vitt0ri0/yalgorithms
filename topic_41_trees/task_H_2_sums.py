import heapq as q

h = []


def push(el):
    q.heappush(h, el)


def pop():
    q.heappop(h)


def solve(A, k):

    l = len(A)
    for i in range(l):
        for j in range(i+1, l):
            diff = abs(A[i] - A[j])
            if len(h) > k:
                larg = q.nlargest(1, h)[0]
                h.remove(larg)
            push(diff)

    if len(h) == k:
        return q.nlargest(2, h)[0]
    return q.nlargest(2, h)[1]

if __name__ == '__main__':
    A = [1, 3, 1]
    res = solve(A, 1)
    print(res)
    #
    # length = int(input())
    # arr = list(map(int, input().split()))
    # k = int(input())

    # 1 1 1
    # 2 2
    # 3
    # k = 4 : answer == 2
   #
   #  h = [1 1 1 2]
   #
   #
   #  h = [1, 2, 1, 3, 2]
   #     1
   #    2  1
   #  3     2
   # 5
