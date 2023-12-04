import pytest
from .app import calculate_points, parse_line

@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", {
            "card_id": 1, 
            "winning_nums": [41, 48, 83, 86, 17], 
            "selected_nums": [83, 86, 6, 31, 17, 9, 48, 53]}),
        ("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11", {
            "card_id": 6, 
            "winning_nums": [31, 18, 13, 56, 72],
            "selected_nums": [74, 77, 10, 23, 35, 67, 36, 11]}),
    ],
)
def test_parse_line(test_input, expected):
    actual = parse_line(test_input)
    assert actual == expected
    
@pytest.mark.parametrize(
    "test_input,expected",
    [
        ({
            "card_id": 1, 
            "winning_nums": [41, 48, 83, 86, 17], 
            "selected_nums": [83, 86, 6, 31, 17, 9, 48, 53]}, 8),
        ({
            "card_id": 6, 
            "winning_nums": [31, 18, 13, 56, 72],
            "selected_nums": [74, 77, 10, 23, 35, 67, 36, 11]}, 0),
    ],
)
def test_calculate_points(test_input, expected):
    actual = calculate_points(test_input)
    assert actual == expected
