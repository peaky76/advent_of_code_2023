import pytest
from .app import parse_grab, parse_input


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("3 blue, 4 red", (4, 0, 3)),
        ("3 green, 4 blue, 1 red", (1, 3, 4)),
        ("5 blue, 4 red, 13 green", (4, 13, 5)),
        ("3 green, 6 red", (6, 3, 0)),
        ("6 red, 1 blue, 3 green", (6, 3, 1)),
    ],
)
def test_parse_grab(test_input, expected):
    assert parse_grab(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            {"id": 1, "rgb": [(4, 0, 3), (1, 2, 6), (0, 2, 0)]},
        ),
        (
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            {"id": 2, "rgb": [(0, 2, 1), (1, 3, 4), (0, 1, 1)]},
        ),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            {"id": 3, "rgb": [(20, 8, 6), (4, 13, 5), (1, 5, 0)]},
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            {"id": 4, "rgb": [(3, 1, 6), (6, 3, 0), (14, 3, 15)]},
        ),
        (
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            {"id": 5, "rgb": [(6, 3, 1), (1, 2, 2)]},
        ),
    ],
)
def test_find_first_number(test_input, expected):
    assert parse_input(test_input) == expected
