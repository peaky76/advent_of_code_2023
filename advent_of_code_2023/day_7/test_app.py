import pytest
from .app import hand_grouping, rank_cards, rank_equal_hands

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
    
def test_rank_cards():
    actual = rank_cards(['5', 'A', '7', '3', 'K', '2', 'T', 'Q', '6'])
    expected = ['A', 'K', 'Q', 'T', '7', '6', '5', '3', '2']
    assert actual == expected

def test_rank_equal_hands():
    actual = rank_equal_hands(["33332", "2AAAA", "QKQQQ"])
    expected = ["QKQQQ", "33332", "2AAAA"]
    assert actual == expected