from day2_code import fib_n
import unittest

def test_pos_list_15():
    resex = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    for i in range(15):
        assert fib_n(15) == resex

def test_pos_2():
    resex = [0, 1]
    for i in range(2):
        assert fib_n(2) == resex

def test_pos_empty():
    resex = []
    for i in range(0):
        assert fib_n(0) == resex