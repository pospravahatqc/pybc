from app_code.pairs_of_number import arnums
import pytest

PAIRSSET = [
    ([2, 6, 7, 9, 0], 0, ( )),
    ([3, 7, 10, 2, 2, 1], 1, [(3, 7)]),
    ([1, 9, 5, 5, 3, 8], 2, [(1, 9), (5, 5)]),
    ([1, 9, 5, 5, 3, 7, 7, 3, 5, 5, 9, 1], 3, [(1, 9), (3, 7), (5, 5)])
]

@pytest.mark.arnums
@pytest.mark.parametrize("number_list,count,pairs", PAIRSSET)
def test_arnums(number_list, count, pairs):
    result = arnums(*number_list)
    assert len(result) == count
    for pair in pairs:
        assert pair in result