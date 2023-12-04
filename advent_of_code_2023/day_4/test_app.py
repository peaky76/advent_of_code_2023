import pytest
from .app import parse_line

@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", {
            "card": 1, 
            "winning_nums": [41, 48, 83, 86, 17], 
            "selected_nums": [83, 86, 6, 31, 17, 9, 48, 53]}),
        ("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11", {
            "card": 6, 
            "winning_nums": [31, 18, 13, 56, 72],
            "selected_nums": [74, 77, 10, 23, 35, 67, 36, 11]}),
    ],
)
def test_parse_line(test_input, expected):
    actual = parse_line(test_input)
    assert actual == expected
    
