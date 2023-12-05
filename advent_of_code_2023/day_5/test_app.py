import pytest
from .app import create_map_function, parse_line, parse_seeds_line, parse_title


def test_create_map_function():
    mappings = [(0, 10, 1), (11, 20, 2), (21, 30, 3)]
    map_function = create_map_function(mappings)
    assert map_function(0) == 1
    assert map_function(15) == 17
    assert map_function(25) == 28
    assert map_function(35) == 35

@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("50 98 2", (98, 99, -48)),
        ("42 0 7", (0, 6, 42)),
        ("18 25 70", (25, 94, -7)),
    ],
)
def test_parse_line(test_input, expected):
    actual = parse_line(test_input)
    assert actual == expected

def test_parse_seeds_line_not_as_range():
    actual = parse_seeds_line("seeds: 79 14 55 13")
    expected = [79, 14, 55, 13]
    assert actual == expected

def test_parse_seeds_line_as_range():
    actual = parse_seeds_line("seeds: 79 14 55 13", as_range=True)
    expected = [79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]
    assert actual == expected

def test_parse_title():
    actual = parse_title("water-to-light map")
    expected = ("water", "light")
    assert actual == expected
    
