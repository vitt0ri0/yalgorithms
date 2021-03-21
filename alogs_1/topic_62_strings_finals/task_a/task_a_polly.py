#

all_words = None
hashes = []
p = 537
mod = 10**9 + 7
pows = [1]
for i in range(10000):
    pows.append(pows[-1] * p % mod)
def mypow(x, a):
    return pows[a]


def get_hash(idx, lf, rg):
    return (hashes[idx][rg] + mod - hashes[idx][lf] * mypow(p, rg - lf) % mod) % mod


def is_palindrome(word_id, pos, is_rev=False):
    n = len(all_words[word_id])
    if is_rev:
        h1 = get_hash(word_id * 2 + 1, pos, n)
        h2 = get_hash(word_id * 2, 0, n - pos)
    else:
        h1 = get_hash(word_id * 2, pos, n)
        h2 = get_hash(word_id * 2 + 1, 0, n - pos)
    return h1 == h2


def calc_hash(word):
    n = len(word)
    arr = [0 for i in range(n + 1)]
    for i, ch in enumerate(word):
        arr[i + 1] = (arr[i] * p % mod + ord(ch) + 1) % mod
    return arr



def calc_hashes():
    for word in all_words:
        hashes.append(calc_hash(word))
        hashes.append(calc_hash(word[::-1]))



class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word_end = -1
        self.palindrome_suffixes = []


def make_trie(words):
    trie = TrieNode()
    for i, word in enumerate(words):
        word = word[::-1]
        current = trie
        for j, c in enumerate(word):
            if is_palindrome(word_id=i, pos=j, is_rev=True): #word[j:]
                current.palindrome_suffixes.append(i)

            if c in current.children:
                current = current.children[c]
            else:
                current.children[c] = TrieNode()
                current = current.children[c]
        current.word_end = i

    return trie


def palindrome_pairs(words):
    trie = make_trie(words)

    result = []
    for i, word in enumerate(words):
        current = trie
        for j, c in enumerate(word):
            if current.word_end != -1:
                if is_palindrome(word_id=i, pos=j): #word[j:]
                    result.append([i + 1, current.word_end + 1])

            if c not in current.children:
                break

            current = current.children[c]

        else:
            if current.word_end != -1 and current.word_end != i:
                result.append([i + 1, current.word_end + 1])

            for j in current.palindrome_suffixes:
                result.append([i + 1, j + 1])

    return sorted(result, key=lambda x: (x[0], x[1]))

filename = 'input.txt'
filename = '01'
# filename = '02'


if __name__ == "__main__":
    with open(filename) as f:
        lst = list(map(lambda x: x.strip(), f.readlines()[1:]))
    all_words = lst[:]
    calc_hashes()
    for p in palindrome_pairs(lst):
        print(*p)