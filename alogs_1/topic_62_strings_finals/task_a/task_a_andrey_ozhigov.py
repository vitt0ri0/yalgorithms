class Trie:
    def __init__(self):
        self.idx = -1
        self.nodes = [None for _ in range(26)]
        self.links = []


d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
     'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
     'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
     't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}


def is_palindrome(word):
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True


def add(root: Trie, word: str, idx: int):
    for i in range(len(word) - 1, -1, -1):
        if is_palindrome(word[0: i + 1]):
            root.links.append(idx)

        if root.nodes[d[word[i]] - 1] is None:
            root.nodes[d[word[i]] - 1] = Trie()

        root = root.nodes[d[word[i]] - 1]

    root.idx = idx
    root.links.append(idx)


def search(root: Trie, word: str, idx: int, result: list):
    i = 0
    while i < len(word) and root is not None:
        if 0 <= root.idx != idx and is_palindrome(word[i: len(word)]):
            result.append((idx, root.idx))

        root = root.nodes[d[word[i]] - 1]
        i += 1

    if root is not None and len(root.links) > 0:
        for i in root.links:
            if i != idx:
                result.append((idx, i))


trie = Trie()
result = []
words = []
for i in range(int(input())):
    temp = input()
    words.append(temp)
    add(trie, words[i], i)

for i in range(len(words)):
    search(trie, words[i], i, result)

for i, j in sorted(result):
    print(i + 1, j + 1)