"""
Test for codingbat.com Logic-2 problems
"""
import pytest
from Logic2 import *


def test_make_bricks():
    assert make_bricks(3, 1, 8) is True
    assert make_bricks(3, 1, 9) is False
    assert make_bricks(3, 2, 10) is True
    assert make_bricks(3, 2, 8) is True
    assert make_bricks(3, 2, 9) is False
    assert make_bricks(6, 1, 11) is True
    assert make_bricks(6, 0, 11) is False
    assert make_bricks(1, 4, 11) is True
    assert make_bricks(0, 3, 10) is True
    assert make_bricks(1, 4, 12) is False
    assert make_bricks(3, 1, 7) is True
    assert make_bricks(1, 1, 7) is False
    assert make_bricks(2, 1, 7) is True
    assert make_bricks(7, 1, 11) is True
    assert make_bricks(7, 1, 8) is True
    assert make_bricks(7, 1, 13) is False
    assert make_bricks(43, 1, 46) is True
    assert make_bricks(40, 1, 46) is False
    assert make_bricks(40, 2, 47) is True
    assert make_bricks(40, 2, 50) is True
    assert make_bricks(40, 2, 52) is False
    assert make_bricks(22, 2, 33) is False
    assert make_bricks(0, 2, 10) is True
    assert make_bricks(1000000, 1000, 1000100) is True
    assert make_bricks(2, 1000000, 100003) is False
    assert make_bricks(20, 0, 19) is True
    assert make_bricks(20, 0, 21) is False
    assert make_bricks(20, 4, 51) is False
    assert make_bricks(20, 4, 39) is True


def test_lone_sum():
    assert lone_sum(1, 2, 3) == 6
    assert lone_sum(3, 2, 3) == 2
    assert lone_sum(3, 3, 3) == 0
    assert lone_sum(9, 2, 2) == 9
    assert lone_sum(2, 2, 9) == 9
    assert lone_sum(2, 9, 2) == 9
    assert lone_sum(2, 9, 3) == 14
    assert lone_sum(4, 2, 3) == 9
    assert lone_sum(1, 3, 1) == 3
