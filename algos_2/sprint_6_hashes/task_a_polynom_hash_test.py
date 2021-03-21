import pytest

from algos_2.sprint_6_hashes.task_a_polynom_hash import hash2, hash_gorner


@pytest.mark.parametrize('a, m, s, res', [
    (123, 100003, 'a', 97),
    (123, 100003, 'hash', 6080),
    (123, 100003, 'HaSH', 56156),
])
def test_hash2(a, m, s, res):
    assert hash2(a, m, s) == res


@pytest.mark.parametrize('a, m, s, res', [
    (123, 100003, 'a', 97),
    (123, 100003, 'hash', 6080),
    (123, 100003, 'HaSH', 56156),
])
def test_hash_str(a, m, s, res):
    assert hash_gorner(a, m, s) == res

