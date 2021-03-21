import pytest

from alogs_1.topic_61_strings.utils import find_divisors


class TestFindDivisors:

    @pytest.mark.parametrize('n, divisors', [
        (5, [1, 5]),
        (10, [1, 2, 5, 10])
    ])
    def test_find_divisors_1(self, n, divisors):
        res = find_divisors(n)
        assert res == divisors
