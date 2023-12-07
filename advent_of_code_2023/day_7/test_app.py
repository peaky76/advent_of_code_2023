import pytest
from .app import hand_grouping

@pytest.mark.parametrize(
    "test_input,expected",
    [
       ('AAAAA', (5,)),
       ('AA8AA', (4, 1)),
       ('23332', (3, 2)),
       ('TTT98', (3, 1, 1)),
       ('23432', (2, 2, 1)),
       ('A23A4', (2, 1, 1, 1)),
       ('23456', (1, 1, 1, 1, 1))
    ],
)
def test_hand_grouping(test_input, expected):
    actual = hand_grouping(test_input)
    assert actual == expected
    
