from pbc.tools import number_pairs
import pytest

def test_pos_list_1():
    outest1 = set([(3, 7)])
    for i in range(15):
        assert number_pairs(3, 7, 10) == outest1

def test_pos_list_2():
    outest2 = set([(2, 8), (4, 6), (1, 9), (3, 7)])
    for i in range(15):
        assert number_pairs(1, 2, 3, 4, 5, 6, 7, 8, 9) == outest2

PAIRSSET = [
    ([2, 6, 7, 9, 0], 0, ( )),
    ([3, 7, 10, 2, 2, 1], 1, [(3, 7)]),
    ([1, 9, 5, 5, 3, 8], 2, [(1, 9), (5, 5)]),
    ([1, 9, 5, 5, 3, 7, 7, 3, 5, 5, 9, 1], 3, [(1, 9), (3, 7), (5, 5)])
]

@pytest.mark.arnums
@pytest.mark.parametrize("number_list,count,pairs", PAIRSSET)
def test_arnums(number_list, count, pairs):
    result = number_pairs(*number_list)
    assert len(result) == count
    for pair in pairs:
        assert pair in result