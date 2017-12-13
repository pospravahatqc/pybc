from pbc.tools import fib
import pytest

def test_pos_list_15():
    resex = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    for i in range(15):
        assert fib(15) == resex

def test_pos_2():
    resex = [0, 1]
    for i in range(2):
        assert fib(2) == resex

def test_pos_empty():
    resex = []
    for i in range(0):
        assert fib(0) == resex


FIBOSET = [
    ( 2, 2, [0, 1]),
    ( 3, 3, [0, 1, 1]),
    ( 5, 5, [0, 1, 1, 2, 3]),
    ( 15, 15, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377])
]

@pytest.mark.arnums
@pytest.mark.parametrize("number_list,count,pairs", FIBOSET)
def test_fibn(number_list, count, pairs):
    result = fib(number_list)
    assert len(result) == count
    for pair in pairs:
        assert pair in result