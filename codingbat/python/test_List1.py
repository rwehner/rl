"""
Test for codingbat.com List-1 problems
"""
import pytest
from List1 import *

def test_first_last6():
    assert first_last6([1, 2, 6]) == True
    assert first_last6([6, 1, 2, 3]) == True
    assert first_last6([13, 6, 1, 2, 3]) == False

def test_same_first_last():
    assert same_first_last([1, 2, 3]) == False
    assert same_first_last([1, 2, 3, 1]) == True
    assert same_first_last([1, 2, 1]) == True
