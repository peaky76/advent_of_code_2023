import pytest
from .app import parse_line

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
    
