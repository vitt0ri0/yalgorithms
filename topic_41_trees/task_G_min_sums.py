def g_min_sums(A, B, kk):

    k = 1
    pairs = list()
    pairs.append((A[0], B[0]))
    if k == kk:
        return pairs
    indices = list()
    indices.append((0, 1))
    indices.append((1, 0))

    while k < kk:
        last_ind = indices[-1]
        a, b = last_ind
        if b == 1 and a + 1 < len(A):
            indices.append((a+1, 0))

        sums = []
        for i in range(len(indices)):
            a, b = indices[i]
            s = A[a] + B[b]
            sums.append((s, i))

        min_sum, pos = min(sums)
        a, b = indices[pos]
        if b + 1 < len(B):
            indices[pos] = (a, b+1)
        else:
            indices.pop(pos)

        k += 1
        pairs.append((A[a], B[b]))
        print(pairs[-1])

    return pairs


if __name__ == '__main__':
    A = [1, 2, 3]
    B = [1, 2, 3]
    k = 9
    res = g_min_sums(A, B, k)
    print(res)