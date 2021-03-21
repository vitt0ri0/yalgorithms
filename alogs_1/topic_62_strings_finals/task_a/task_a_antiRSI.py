from functools import reduce

filename = 'input.txt'
filename = '01'
# filename = '02'


def ispalin(s):
    return s == s[::-1]


def palindromePairs(words):
    result = []
    root = {}
    for i, word in enumerate(words):
        curr = root
        for idx, ch in enumerate(word):
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
            tmp = word[idx + 1:]
            if tmp and ispalin(tmp):
                curr.setdefault("ids", []).append(i)
        curr["isword"] = i
    for j, word in enumerate(words):
        w = word[::-1]
        curr = root
        fail = False
        for idx, ch in enumerate(w):
            if ch not in curr:
                fail = True
                break
            curr = curr[ch]
            i = curr.get("isword")
            if i is not None and i != j and ispalin(w[idx + 1:]):
                result.append([i + 1, j + 1])
        if not fail and "ids" in curr:
            result.extend([i + 1, j + 1] for i in curr["ids"] if i != j)
    if "" in words:
        idx = words.index("")
        result.extend(
            reduce(lambda x, y: x + y,
                   ([[i, idx], [idx, i]] for i, w in enumerate(words) if w and ispalin(w))))

    for pair in sorted(result):
        print(*pair)


if __name__ == '__main__':
    f = open(filename)
    n = int(f.readline().strip())
    words = []
    for _ in range(n):
        words.append(f.readline().strip())

    palindromePairs(words)