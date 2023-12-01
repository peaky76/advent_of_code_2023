import pytest
from .app import find_first_number, find_last_number

@pytest.mark.parametrize("test_input,expected", [
    ("1qwerty2uiop3",  1), 
    ("oneqwertytwo", 1), 
    ("76xkqjzqtwonfour", 7),
    ("7fivefive", 7),
    ("512ninexrqpvktwoner", 5),
    ])
def test_find_first_number(test_input, expected):
    assert find_first_number(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [
    ("1qwerty2uiop3",  3), 
    ("oneqwertytwo", 2), 
    ("76xkqjzqtwonfour", 4),
    ("7fivefive", 5),
    ("512ninexrqpvktwoner", 1),
    ])
def test_find_last_number(test_input, expected):
    assert find_last_number(test_input) == expected