from app_code.fibonachi_app import fibn
import pytest

FIBOSET = [
    ( 2, 2, [0, 1]),
    ( 3, 3, [0, 1, 1]),
    ( 5, 5, [0, 1, 1, 2, 3]),
    ( 15, 15, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377])
]

@pytest.mark.arnums
@pytest.mark.parametrize("number_list,count,pairs", FIBOSET)
def test_fibn(number_list, count, pairs):
    result = fibn(number_list)
    assert len(result) == count
    for pair in pairs:
        assert pair in result