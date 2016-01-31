"""
Test for codingbat.com Logic-2 problems
"""
import pytest
from Logic2 import *


def test_make_bricks():
    #assert make_bricks(3, 1, 8) == True
    #assert make_bricks(3, 1, 9) == False
    #assert make_bricks(3, 2, 10) == True
    #assert make_bricks(3, 2, 9) == True
    assert make_bricks(3, 1, 8) == True
    assert make_bricks(3, 1, 9) == False
    assert make_bricks(3, 2, 10) == True
    assert make_bricks(3, 2, 8) == True
    assert make_bricks(3, 2, 9) == False
    assert make_bricks(6, 1, 11) == True
    assert make_bricks(6, 0, 11) == False
    assert make_bricks(1, 4, 11) == True
    assert make_bricks(0, 3, 10) == True
    assert make_bricks(1, 4, 12) == False
    assert make_bricks(3, 1, 7) == True
    assert make_bricks(1, 1, 7) == False
    assert make_bricks(2, 1, 7) == True
    assert make_bricks(7, 1, 11) == True
    assert make_bricks(7, 1, 8) == True
    assert make_bricks(7, 1, 13) == False
    assert make_bricks(43, 1, 46) == True
    assert make_bricks(40, 1, 46) == False
    assert make_bricks(40, 2, 47) == True
    assert make_bricks(40, 2, 50) == True
    assert make_bricks(40, 2, 52) == False
    assert make_bricks(22, 2, 33) == False
    assert make_bricks(0, 2, 10) == True
    assert make_bricks(1000000, 1000, 1000100) == True
    assert make_bricks(2, 1000000, 100003) == False
    assert make_bricks(20, 0, 19) == True
    assert make_bricks(20, 0, 21) == False
    assert make_bricks(20, 4, 51) == False
    assert make_bricks(20, 4, 39) == True
