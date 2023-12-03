import pytest
from .app import get_gears, get_part_numbers, get_part_indicators, has_adjacent_indicator, is_adjacent

def test_get_part_numbers():
    lines = ["123...",".45.67","..890."]
    expected = get_part_numbers(lines)
    actual = [
        (123, 0, 0), 
        (45, 1, 1), 
        (67, 1, 4), 
        (890, 2, 2)
    ]
    assert expected == actual

def test_get_part_indicators():
    lines = ["123.$.",".45.67","..#..."]
    expected = get_part_indicators(lines)
    actual = [(0, 4), (2, 2)]
    assert expected == actual

def test_get_gears():
    lines = ["123...",".45*67","..890."]
    expected = get_gears(lines)
    actual = [(1,3)]
    assert expected == actual

@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([(3, 3), (2, 2)], True),
        ([(3, 3), (3, 4)], True),
        ([(3, 3), (2, 3)], True), 
        ([(3, 3), (3, 2)], True),
        ([(3, 3), (4, 3)], True),
        ([(3, 3), (4, 4)], True),
        ([(3, 3), (3, 5)], False),
        ([(3, 3), (5, 3)], False),
    ],
)
def test_is_adjacent(test_input, expected):
    test_coord_1, test_coord_2 = test_input
    assert is_adjacent(test_coord_1, test_coord_2) == expected
    
@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([(0, 0, 3), [(1, 3), (2, 6), (3,3), (4, 5)]], True),
        ([(0, 5, 3), [(1, 3), (2, 6), (3,3), (4, 5)]], False),
        ([(2, 2, 2), [(1, 3), (2, 6), (3,3), (4, 5)]], True),
        ([(2, 6, 3), [(1, 3), (2, 6), (3,3), (4, 5)]], True),
        ([(3, 2, 3), [(2, 1)]], True),
        ([(3, 2, 3), [(2, 3)]], True),
        ([(3, 2, 3), [(2, 5)]], True),
        ([(3, 2, 3), [(3, 1)]], True),
        ([(3, 2, 3), [(3, 5)]], True),
        ([(3, 2, 3), [(4, 1)]], True),
        ([(3, 2, 3), [(4, 3)]], True),
        ([(3, 2, 3), [(4, 5)]], True),
        ([(3, 2, 3), [(4, 6)]], False),
        ([(3, 2, 3), [(2, 0)]], False),
    ],
)
def test_has_adjacent_indicator(test_input, expected):
    part_loc_and_len, part_indicators = test_input
    assert has_adjacent_indicator(part_loc_and_len, part_indicators) == expected