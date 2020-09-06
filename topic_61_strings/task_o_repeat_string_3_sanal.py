import pytest


def kmp(s):
    p = [0 for _ in range(len(s))]
    for i in range(1, len(s)):
        j = p[i - 1]
        while j > 0 and s[j] != s[i]:
            j = p[j - 1]
        if s[j] == s[i]:
            j += 1
        p[i] = j
    return p


def find_string_repeat(string):
    l = len(string)

    p = kmp(string)

    r = l - p[-1]

    if r > l // 2:
        return 1
    else:
        return l//r


if __name__ == '__main__':

    string = input()



@pytest.mark.parametrize('string, res', [
    ('abababab', 4),
    ('aaaaaaaa', 8),
    ('abcdef', 1)
])
def test_find_string_repeat(string, res):
    result = find_string_repeat(string)
    assert result == res
