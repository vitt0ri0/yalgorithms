import math

# Наивное решение. Дробим строку на N частей и сравниваем эти части на равенство между собой.

"""
33788849	
O
Python 3.7.3	
TL
-	
0.607s
32.80Mb
43
"""

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

def checkEqual1(data):
    iterator = iter(data)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in iterator)


def compare_positions(divisor, length, the_string):
    chunk_size = int(length / divisor)
    parts = [the_string[i:i + chunk_size] for i in range(0, length, chunk_size)]

    if checkEqual1(parts):
        return divisor
    else:
        return -1


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




