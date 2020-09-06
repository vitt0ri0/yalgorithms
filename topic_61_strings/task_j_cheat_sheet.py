
"""

Время	ID	Задача	Участник	Компилятор	Вердикт	Время	Память
2020.08.19 20:00:36
14d, 22:20:04
33801328	J	oguseynov	Python 3.7.3 	TL ( task_b_11.txt )
"""

def _char_to_index(ch):
    return ord(ch) - ord("a")


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        current = self.root
        for i in range(len(key)):
            index = _char_to_index(key[i])

            if not current.children[index]:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.word_end = True

    def search(self, key):
        current = self.root
        for i in range(len(key)):
            index = _char_to_index(key[i])
            if not current.children[index]:
                return False
            current = current.children[index]

        return current is not None and current.word_end


def is_in_t(t, d):
    res = [False] * len(t)
    maxi_len = len(max(d, key=len))

    trie = Trie()
    for w in d:
        trie.insert(w)

    i = 0
    j = 0
    k = 0
    last = 0
    while (i <= len(t) and not last) or (k + j + 1 <= len(t)):
        if trie.search(t[k:k + j + 1]):
            res[k + j] = True
            last = k + j + 1
        j += 1
        i += 1
        if j == maxi_len:
            k = last
            j = 0

    if res[-1]:
        return "YES"
    return "NO"


if __name__ == "__main__":
    with open("input3.txt") as f:
        t = f.readline().strip()
        n = int(f.readline().strip())

        d = []
        for _ in range(n):
            d.append(f.readline().strip())

    print(is_in_t(t, d))