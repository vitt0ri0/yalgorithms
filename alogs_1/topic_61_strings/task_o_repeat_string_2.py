import pytest

"""
33788924	
O
Python 3.7.3	
TL
-	
0.638s
4.01Mb
36	-
"""

import math

def find_divisors(n):

    a = list()
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            if not (n / i == i):
                a.append(int(n/i))
            a.append(i)
        i += 1

    a.sort()

    return a


def checkEqual2(the_range, string):
    iterator = iter(the_range)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(string[first] == string[rest] for rest in iterator)


def compare_positions(divisor, length, the_string):
    chunk_size = int(length / divisor)
    for j in range(0, chunk_size):  # for every symbol in chunk
        the_range = range(0 + j, length, chunk_size)
        res = checkEqual2(the_range, the_string)
        if not res:
            return -1
    return divisor



def find_string_repeat(the_string):
    l = len(the_string)

    divisors = find_divisors(l)

    for divisor in reversed(divisors):
        res = compare_positions(divisor, l, the_string)
        if res != -1:
            return res
    return 1


if __name__ == '__main__':
    s = input()
    res = find_string_repeat(s)
    print(res)


@pytest.mark.parametrize('string, res', [
    ('abababab', 4),
    ('aaaaaaaa', 8),
    ('abcdef', 1)
])
def test_find_string_repeat(string, res):

    result = find_string_repeat(string)
    assert result == res




