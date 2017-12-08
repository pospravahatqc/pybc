from app_code.pairs_of_number import arnums
import unittest

def test_pos_list_1():
    outest1 = set([(3, 7)])
    for i in range(15):
        assert arnums(3, 7, 10) == outest1

def test_pos_list_2():
    outest2 = set([(2, 8), (4, 6), (1, 9), (3, 7)])
    for i in range(15):
        assert arnums(1, 2, 3, 4, 5, 6, 7, 8, 9) == outest2
