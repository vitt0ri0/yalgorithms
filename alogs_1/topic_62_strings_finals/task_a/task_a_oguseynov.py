#
def is_palindrome(s):
    return s == s[::-1]
    # j = -1
    # for i in range(len(s)//2):
    #     if s[i] != s[j]:
    #         return False
    #     j -= 1
    #
    # return True


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
            if is_palindrome(word[j:]):
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
                if is_palindrome(word[j:]):
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


if __name__ == "__main__":
    with open("input.txt") as f:
        lst = list(map(lambda x: x.strip(), f.readlines()[1:]))

    for p in palindrome_pairs(lst):
        print(*p)