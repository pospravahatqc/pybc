import unittest
from app_code.fibonachi_app import fibn

def test_pos_list_15():
    resex = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    for i in range(15):
        assert fibn(15) == resex

def test_pos_2():
    resex = [0, 1]
    for i in range(2):
        assert fibn(2) == resex

def test_pos_empty():
    resex = []
    for i in range(0):
        assert fibn(0) == resex