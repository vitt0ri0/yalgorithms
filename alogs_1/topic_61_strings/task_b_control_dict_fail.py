def count_hash(s):
    d = dict()
    for c in s:
        el = d.get(c, None)
        if el:
            d[c] += 1
        else:
            d[c] = 1
    return d

def solution(word1, word2):
    hash1 = count_hash(word1)
    hash2 = count_hash(word2)

    diff_neg = 0
    diff_pos = 0
    myset = set(word1 + word2)
    for char in myset:
        value1 = hash1.get(char, 0)
        value2 = hash2.get(char, 0)
        diff = value1 - value2
        if diff < 0:
            diff_neg += abs(diff)
        elif diff > 0:
            diff_pos += diff

    return diff_neg in (0, 1) and diff_pos in (0, 1)


def context():
    w1 = input()
    w2 = input()
    res = solution(w1, w2)
    verdict = 'OK' if res else 'FAIL'
    print(verdict)

def mytests():
    mytest('abc', 'abc')
    mytest('fog', 'dog')
    mytest('ab', 'abc')
    mytest('abcd', 'abc')
    mytest('mama', 'papa')
    mytest('', '')
    mytest('  ', '')


def mytest(word1, word2):
    res = solution(word1, word2)
    print(f'w1: {word1}, w2: {word2}, res: {res}')


if __name__ == '__main__':
    context()
